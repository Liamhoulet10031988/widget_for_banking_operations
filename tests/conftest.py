import pytest


@pytest.fixture
def operations_fixture() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 3, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def empty_operations_fixture() -> list[dict]:
    return []
