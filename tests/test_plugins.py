import pytest

from neuron.plugins import (
    Plugin,
    PluginAlreadyRegisteredError,
    PluginManager,
)


class DemoPlugin(Plugin):

    def __init__(self):
        self.started = False
        self.stopped = False

    async def startup(self):
        self.started = True

    async def shutdown(self):
        self.stopped = True


@pytest.mark.asyncio
async def test_plugin_lifecycle():

    manager = PluginManager()

    plugin = DemoPlugin()

    manager.register(plugin)

    await manager.startup()

    assert plugin.started

    await manager.shutdown()

    assert plugin.stopped


def test_duplicate_plugin():

    manager = PluginManager()

    plugin = DemoPlugin()

    manager.register(plugin)

    with pytest.raises(PluginAlreadyRegisteredError):
        manager.register(plugin)