"""Errors raised while loading runtime configuration."""

from __future__ import annotations


class ConfigurationError(Exception):
    """Raised when a configuration file cannot be read or violates expectations."""
