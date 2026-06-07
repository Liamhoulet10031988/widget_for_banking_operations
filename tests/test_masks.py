import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    ("card_number", "expected"),
    [
        (1234567890123456, "1234 56** **** 3456"),
        (123456789012345, "Введите корректный номер карты"),
        (12345678901234567, "Введите корректный номер карты"),
    ],
)
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    ("account_number", "expected"),
    [
        (12345678901234567890, "**7890"),
        (1234567890, "Введите корректный номер счета"),
    ],
)
def test_get_mask_account(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected
