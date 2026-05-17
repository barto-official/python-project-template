from __future__ import annotations

from enum import IntEnum


class ExitCode(IntEnum):
    SUCCESS = 0
    INTERNAL_ERROR = 1
    INVALID_INPUT = 2
    DOMAIN_ERROR = 3
    CONFIGURATION_ERROR = 4
    EXTERNAL_ERROR = 5
    RETRIABLE_ERROR = 6
    PERMISSION_ERROR = 7
    NOT_FOUND = 8
    CONFLICT = 9
    INTERRUPTED = 130