from neuron import AIApp
from neuron.config import Settings
from neuron.events import EventBus
from neuron.lifecycle import LifecycleManager
from neuron.runtime import Runtime


def test_create_application():

    app = AIApp()

    assert isinstance(app.settings, Settings)
    assert isinstance(app.lifecycle, LifecycleManager)
    assert isinstance(app.runtime, Runtime)
    assert isinstance(app.events, EventBus)


def test_container_registration():

    app = AIApp()

    assert app.container.resolve(Settings) is app.settings
    assert app.container.resolve(Runtime) is app.runtime
    assert app.container.resolve(LifecycleManager) is app.lifecycle
    assert app.container.resolve(EventBus) is app.events