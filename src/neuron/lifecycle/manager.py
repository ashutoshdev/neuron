from neuron.core import ComponentState


class LifecycleManager:
    """
    Controls the application lifecycle.
    """

    def __init__(self) -> None:
        self._state = ComponentState.CREATED

    @property
    def state(self) -> ComponentState:
        return self._state

    async def start(self) -> None:
        self._state = ComponentState.STARTING

        # Future startup tasks

        self._state = ComponentState.RUNNING

    async def stop(self) -> None:
        self._state = ComponentState.STOPPING

        # Future shutdown tasks

        self._state = ComponentState.STOPPED