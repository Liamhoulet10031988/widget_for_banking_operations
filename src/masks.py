"""Модуль реализации масок для банковских карт и счетов."""


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)

    if len(card_number_str) == 16 and card_number_str.isdigit():
        first_part = card_number_str[:4]
        second_part = card_number_str[4:6]
        last_part = card_number_str[-4:]
        return f"{first_part} {second_part}** **** {last_part}"
    return "Введите корректный номер карты"


def get_mask_account(acc_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    acc_number_str = str(acc_number)

    if len(acc_number_str) == 20 and acc_number_str.isdigit():
        return f"**{acc_number_str[-4:]}"
    return "Введите корректный номер счета"
