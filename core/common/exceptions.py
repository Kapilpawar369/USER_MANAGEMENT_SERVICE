# core/common/exceptions.py
# Purpose: Custom exceptions and helper exception classes.
# Imported by: services/* modules and can be used in exception handlers.

class NotFoundError(Exception):
    """Raised when a response is not found."""


class BadRequestError(Exception):
    """Raised when request data is invalid."""


class ConflictError(Exception):
    """Raised when a response already exists (e.g., duplicate email)."""
