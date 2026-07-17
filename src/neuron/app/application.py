from __future__ import annotations

from neuron.config import Settings
from neuron.dependency import Container
from neuron.events import EventBus
from neuron.lifecycle import LifecycleManager
from neuron.plugins import PluginManager
from neuron.runtime import Runtime


class AIApp:
    """
    Root application object.

    Every Neuron application starts here.
    """

    def __init__(
        self,
        *,
        settings: Settings | None = None,
    ) -> None:
        # Core services
        self._settings = settings or Settings()
        self._lifecycle = LifecycleManager()
        self._runtime = Runtime()
        self._container = Container()

        # Register framework services
        self._container.register(Settings, self._settings)
        self._container.register(LifecycleManager, self._lifecycle)
        self._container.register(Runtime, self._runtime)
        self._container.register(EventBus, self._runtime.events)
        self._container.register(PluginManager, self._runtime.plugins)

    @property
    def settings(self) -> Settings:
        """Application settings."""
        return self._settings

    @property
    def lifecycle(self) -> LifecycleManager:
        """Application lifecycle manager."""
        return self._lifecycle

    @property
    def runtime(self) -> Runtime:
        """Application runtime."""
        return self._runtime

    @property
    def events(self) -> EventBus:
        """Application event bus."""
        return self._runtime.events

    @property
    def plugins(self) -> PluginManager:
        """Application plugin manager."""
        return self._runtime.plugins

    @property
    def container(self) -> Container:
        """Dependency injection container."""
        return self._container

    async def start(self) -> None:
        """Start the application."""
        await self._lifecycle.start()
        await self._runtime.start()

    async def stop(self) -> None:
        """Stop the application."""
        await self._runtime.stop()
        await self._lifecycle.stop()

    def __repr__(self) -> str:
        return (
            f"AIApp("
            f"name={self.settings.app_name!r}, "
            f"state={self.lifecycle.state.value!r}"
            f")"
        )