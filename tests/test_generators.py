import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_returns_usd_transactions(transactions_fixture: list[dict]) -> None:
    result = list(filter_by_currency(transactions_fixture, "USD"))

    assert len(result) == 3
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_first_two_elements(transactions_fixture: list[dict]) -> None:
    usd_transactions = filter_by_currency(transactions_fixture, "USD")

    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_no_matches(transactions_fixture: list[dict]) -> None:
    assert list(filter_by_currency(transactions_fixture, "EUR")) == []


def test_transaction_descriptions(transactions_fixture: list[dict]) -> None:
    descriptions = transaction_descriptions(transactions_fixture)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_empty() -> None:
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    ("start", "stop", "expected"),
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (1, 1, ["0000 0000 0000 0001"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_empty_range() -> None:
    assert list(card_number_generator(5, 1)) == []
