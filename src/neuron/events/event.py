from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4


@dataclass(slots=True)
class Event:
    """
    Base class for all framework events.
    """

    name: str
    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )
    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )