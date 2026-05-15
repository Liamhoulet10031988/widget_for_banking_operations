from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations_fixture: list[dict]) -> None:
    result = filter_by_state(operations_fixture)
    assert all(item["state"] == "EXECUTED" for item in result)
    assert len(result) == 2


def test_filter_by_state_canceled(operations_fixture: list[dict]) -> None:
    result = filter_by_state(operations_fixture, "CANCELED")
    assert all(item["state"] == "CANCELED" for item in result)
    assert len(result) == 2


def test_filter_by_state_no_matches(operations_fixture: list[dict]) -> None:
    assert filter_by_state(operations_fixture, "PENDING") == []


def test_filter_by_state_empty(empty_operations_fixture: list[dict]) -> None:
    assert filter_by_state(empty_operations_fixture) == []


def test_sort_by_date_desc(operations_fixture: list[dict]) -> None:
    result = sort_by_date(operations_fixture)
    assert result == sorted(operations_fixture, key=lambda item: item["date"], reverse=True)


def test_sort_by_date_asc(operations_fixture: list[dict]) -> None:
    result = sort_by_date(operations_fixture, reverse=False)
    assert result == sorted(operations_fixture, key=lambda item: item["date"])


def test_sort_by_date_empty() -> None:
    assert sort_by_date([]) == []


def test_sort_by_date_same_dates() -> None:
    operations = [
        {"id": 1, "date": "2024-01-01T10:00:00.000000"},
        {"id": 2, "date": "2024-01-01T10:00:00.000000"},
    ]

    assert sort_by_date(operations) == operations
