from __future__ import annotations

from neuron.core import ComponentState
from neuron.events import EventBus
from neuron.plugins import PluginManager


class Runtime:
    """
    Coordinates execution inside Neuron.

    The Runtime is responsible for managing the execution
    environment and framework-level services.
    """

    def __init__(self) -> None:
        self._state = ComponentState.CREATED
        self._events = EventBus()
        self._plugins = PluginManager()

    @property
    def state(self) -> ComponentState:
        """Current runtime state."""
        return self._state

    @property
    def events(self) -> EventBus:
        """Framework event bus."""
        return self._events

    @property
    def plugins(self) -> PluginManager:
        """Framework plugin manager."""
        return self._plugins

    async def start(self) -> None:
        """
        Start the runtime.
        """
        self._state = ComponentState.STARTING

        # Future:
        # - Start scheduler
        # - Initialize resources
        # - Start worker pools

        await self._plugins.startup()

        self._state = ComponentState.RUNNING

    async def stop(self) -> None:
        """
        Stop the runtime.
        """
        self._state = ComponentState.STOPPING

        await self._plugins.shutdown()

        # Future:
        # - Stop workers
        # - Release resources

        self._state = ComponentState.STOPPED

    def __repr__(self) -> str:
        return (
            f"Runtime(state={self._state.value!r})"
        )