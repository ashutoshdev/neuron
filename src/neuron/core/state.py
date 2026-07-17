from enum import Enum


class ComponentState(str, Enum):
    """
    Common lifecycle states for framework components.
    """

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"