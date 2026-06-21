from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


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


def test_process_bank_search_found() -> None:
    operations = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]

    result = process_bank_search(operations, "перевод")

    assert result == [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
    ]


def test_process_bank_search_not_found() -> None:
    operations = [
        {"description": "Открытие вклада"},
    ]

    assert process_bank_search(operations, "карта") == []


def test_process_bank_search_with_special_symbol() -> None:
    operations = [
        {"description": "Оплата услуг?"},
        {"description": "Перевод организации"},
    ]

    assert process_bank_search(operations, "услуг?") == [
        {"description": "Оплата услуг?"},
    ]


def test_process_bank_operations() -> None:
    operations = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    categories = [
        "Перевод организации",
        "Открытие вклада",
        "Перевод с карты на карту",
    ]

    assert process_bank_operations(operations, categories) == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 0,
    }
