class DependencyError(Exception):
    """
    Base exception for dependency injection errors.
    """


class ServiceNotFoundError(DependencyError):
    """
    Raised when a requested service is not registered.
    """


class ServiceAlreadyRegisteredError(DependencyError):
    """
    Raised when attempting to register a service that already exists.
    """