from __future__ import annotations

from .exceptions import PluginAlreadyRegisteredError
from .plugin import Plugin


class PluginManager:
    """
    Manages framework plugins.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(
        self,
        plugin: Plugin,
    ) -> None:

        if plugin.name in self._plugins:
            raise PluginAlreadyRegisteredError(
                f"{plugin.name} is already registered."
            )

        self._plugins[plugin.name] = plugin

    async def startup(self) -> None:
        for plugin in self._plugins.values():
            await plugin.startup()

    async def shutdown(self) -> None:
        for plugin in reversed(tuple(self._plugins.values())):
            await plugin.shutdown()

    @property
    def plugins(self) -> tuple[Plugin, ...]:
        return tuple(self._plugins.values())

    def __len__(self) -> int:
        return len(self._plugins)

    def __contains__(self, name: str) -> bool:
        return name in self._plugins