from __future__ import annotations


class MyToolError(Exception):
    """Base class for expected application errors."""


class InvalidUsageError(MyToolError):
    """User provided invalid CLI/application input."""


class DomainError(MyToolError):
    """Domain rule violation."""


class ValidationFailureError(DomainError):
    """Input/data validation failed."""


class NotFoundError(MyToolError):
    """Required resource was not found."""


class ConflictError(MyToolError):
    """Operation conflicts with current state."""


class PermissionDeniedError(MyToolError):
    """Operation is not permitted."""


class ExternalError(MyToolError):
    """External system failed."""


class RetriableExternalError(ExternalError):
    """External failure may be temporary."""


class FatalExternalError(ExternalError):
    """External failure is not expected to succeed by retrying."""
