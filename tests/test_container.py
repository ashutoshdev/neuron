import pytest

from neuron.dependency import (
    Container,
    ServiceAlreadyRegisteredError,
    ServiceNotFoundError,
)


class Database:
    pass


def test_register_service():

    container = Container()

    db = Database()

    container.register(Database, db)

    assert container.resolve(Database) is db


def test_duplicate_registration():

    container = Container()

    db = Database()

    container.register(Database, db)

    with pytest.raises(ServiceAlreadyRegisteredError):
        container.register(Database, db)


def test_missing_service():

    container = Container()

    with pytest.raises(ServiceNotFoundError):
        container.resolve(Database)


def test_contains():

    container = Container()

    db = Database()

    container.register(Database, db)

    assert Database in container


def test_length():

    container = Container()

    assert len(container) == 0

    container.register(Database, Database())

    assert len(container) == 1