from __future__ import annotations

from collections.abc import Awaitable, Callable

from .event import Event

EventHandler = Callable[[Event], Awaitable[None]]


class EventBus:
    """
    Simple asynchronous event bus.
    """

    def __init__(self) -> None:
        self._subscribers: dict[
            str,
            list[EventHandler],
        ] = {}

    def subscribe(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:

        self._subscribers.setdefault(
            event_name,
            []
        ).append(handler)

    async def publish(
        self,
        event: Event,
    ) -> None:

        handlers = self._subscribers.get(
            event.name,
            []
        )

        for handler in handlers:
            await handler(event)