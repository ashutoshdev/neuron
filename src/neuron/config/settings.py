from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Settings:
    """
    Global application settings.
    """

    app_name: str = "Neuron App"
    debug: bool = False