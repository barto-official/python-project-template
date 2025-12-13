#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  apply-repo-policy.sh -o OWNER -r REPO [-b BRANCH] [-t TOKEN]

Options:
  -o  GitHub org/user (owner)
  -r  Repository name
  -b  Branch to protect (default: repo default branch)
  -t  Token (optional if GITHUB_TOKEN is set)

Env:
  GITHUB_TOKEN  Personal access token or GitHub App user token

Examples:
  GITHUB_TOKEN=... ./scripts/apply-repo-policy.sh -o myorg -r myrepo
  ./scripts/apply-repo-policy.sh -o myorg -r myrepo -b main -t ghp_...
EOF
}

OWNER=""
REPO=""
BRANCH=""
TOKEN="${GITHUB_TOKEN:-}"

while getopts ":o:r:b:t:h" opt; do
  case "$opt" in
    o) OWNER="$OPTARG" ;;
    r) REPO="$OPTARG" ;;
    b) BRANCH="$OPTARG" ;;
    t) TOKEN="$OPTARG" ;;
    h) usage; exit 0 ;;
    \?) echo "Unknown option: -$OPTARG" >&2; usage; exit 2 ;;
    :)  echo "Missing argument for -$OPTARG" >&2; usage; exit 2 ;;
  esac
done

if [[ -z "$OWNER" || -z "$REPO" ]]; then
  echo "ERROR: OWNER and REPO are required." >&2
  usage
  exit 2
fi

if [[ -z "$TOKEN" ]]; then
  echo "ERROR: Provide a token via -t or GITHUB_TOKEN." >&2
  exit 2
fi

API="https://api.github.com"
HDR_ACCEPT="Accept: application/vnd.github+json"
HDR_AUTH="Authorization: Bearer ${TOKEN}"
HDR_VER="X-GitHub-Api-Version: 2022-11-28"

policy_dir=".github/repo-policy"
repo_security_json="${policy_dir}/repo-security.json"
codeql_json="${policy_dir}/codeql-default-setup.json"
branch_protection_json="${policy_dir}/branch-protection.json"

require_file() {
  local f="$1"
  if [[ ! -f "$f" ]]; then
    echo "ERROR: Missing required file: $f" >&2
    exit 2
  fi
}

require_file "$repo_security_json"
require_file "$codeql_json"
require_file "$branch_protection_json"

api_call() {
  local method="$1"
  local url="$2"
  local data_file="${3:-}"

  if [[ -n "$data_file" ]]; then
    curl -sS -L -X "$method" \
      -H "$HDR_ACCEPT" -H "$HDR_AUTH" -H "$HDR_VER" \
      "$url" \
      --data-binary @"$data_file"
  else
    curl -sS -L -X "$method" \
      -H "$HDR_ACCEPT" -H "$HDR_AUTH" -H "$HDR_VER" \
      "$url"
  fi
}

# Determine default branch if BRANCH not provided
if [[ -z "$BRANCH" ]]; then
  repo_json="$(api_call GET "${API}/repos/${OWNER}/${REPO}")"
  BRANCH="$(python3 - <<PY
import json, sys
obj=json.loads(sys.stdin.read())
print(obj.get("default_branch",""))
PY
<<<"$repo_json")"
  if [[ -z "$BRANCH" ]]; then
    echo "ERROR: Could not determine default_branch." >&2
    exit 1
  fi
fi

echo "Applying policy to ${OWNER}/${REPO} (branch: ${BRANCH})"

echo "1) Configure repo security_and_analysis"
api_call PATCH "${API}/repos/${OWNER}/${REPO}" "$repo_security_json" >/dev/null

echo "2) Enable vulnerability alerts (Dependabot alerts + dependency graph)"
# PUT /repos/{owner}/{repo}/vulnerability-alerts :contentReference[oaicite:4]{index=4}
api_call PUT "${API}/repos/${OWNER}/${REPO}/vulnerability-alerts" >/dev/null

echo "3) Enable automated security fixes (Dependabot security updates)"
# PUT /repos/{owner}/{repo}/automated-security-fixes :contentReference[oaicite:5]{index=5}
api_call PUT "${API}/repos/${OWNER}/${REPO}/automated-security-fixes" >/dev/null

echo "4) Configure CodeQL default setup (code scanning)"
# PATCH /repos/{owner}/{repo}/code-scanning/default-setup :contentReference[oaicite:6]{index=6}
api_call PATCH "${API}/repos/${OWNER}/${REPO}/code-scanning/default-setup" "$codeql_json" >/dev/null

echo "5) Apply branch protection"
# PUT /repos/{owner}/{repo}/branches/{branch}/protection :contentReference[oaicite:7]{index=7}
api_call PUT "${API}/repos/${OWNER}/${REPO}/branches/${BRANCH}/protection" "$branch_protection_json" >/dev/null

echo "Done."
