import pytest

from neuron.runtime import Runtime
from neuron.runtime import RuntimeState


@pytest.mark.asyncio
async def test_runtime():

    runtime = Runtime()

    assert runtime.state == RuntimeState.CREATED

    await runtime.start()

    assert runtime.state == RuntimeState.RUNNING

    await runtime.stop()

    assert runtime.state == RuntimeState.STOPPED