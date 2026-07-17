from __future__ import annotations

from typing import Any

from .exceptions import (
    ServiceAlreadyRegisteredError,
    ServiceNotFoundError,
)


class Container:
    """
    Dependency Injection Container.

    Stores singleton services and provides
    service resolution throughout the application.
    """

    def __init__(self) -> None:
        self._services: dict[type[Any], Any] = {}

    def register(
        self,
        interface: type[Any],
        instance: Any,
    ) -> None:
        """
        Register a service.

        Raises
        ------
        ServiceAlreadyRegisteredError
            If the service is already registered.
        """

        if interface in self._services:
            raise ServiceAlreadyRegisteredError(
                f"{interface.__name__} is already registered."
            )

        self._services[interface] = instance

    def resolve(
        self,
        interface: type[Any],
    ) -> Any:
        """
        Resolve a service.

        Raises
        ------
        ServiceNotFoundError
            If the service has not been registered.
        """

        try:
            return self._services[interface]
        except KeyError as exc:
            raise ServiceNotFoundError(
                f"{interface.__name__} is not registered."
            ) from exc

    def __contains__(
        self,
        interface: type[Any],
    ) -> bool:
        return interface in self._services

    def __len__(self) -> int:
        return len(self._services)