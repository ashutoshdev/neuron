import pytest

from neuron.lifecycle import LifecycleManager
from neuron.lifecycle import LifecycleState


@pytest.mark.asyncio
async def test_lifecycle():

    manager = LifecycleManager()

    assert manager.state == LifecycleState.CREATED

    await manager.start()

    assert manager.state == LifecycleState.RUNNING

    await manager.stop()

    assert manager.state == LifecycleState.STOPPED