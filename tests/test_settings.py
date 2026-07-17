from neuron.config import Settings


def test_default_settings():
    settings = Settings()

    assert settings.app_name == "Neuron App"
    assert settings.debug is False