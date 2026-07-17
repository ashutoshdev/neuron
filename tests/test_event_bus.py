import pytest

from neuron.events import Event
from neuron.events import EventBus


@pytest.mark.asyncio
async def test_publish():

    bus = EventBus()

    called = False

    async def handler(event):
        nonlocal called
        called = True

    bus.subscribe(
        "startup",
        handler,
    )

    await bus.publish(
        Event(name="startup")
    )

    assert called