from __future__ import annotations


class Plugin:
    """
    Base class for all Neuron plugins.
    """

    @property
    def name(self) -> str:
        return self.__class__.__name__

    async def startup(self) -> None:
        """
        Called when the application starts.
        """

    async def shutdown(self) -> None:
        """
        Called when the application stops.
        ```