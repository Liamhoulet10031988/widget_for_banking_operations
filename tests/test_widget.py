import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Нечто 123", "Некорректный формат номера"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
