"""Модуль реализации масок для банковских карт и счетов."""
import logging
import os

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)

if not logger.handlers:
    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.propagate = False


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    logger.info("Начата маскировка номера карты")

    if len(card_number_str) == 16 and card_number_str.isdigit():
        first_part = card_number_str[:4]
        second_part = card_number_str[4:6]
        last_part = card_number_str[-4:]
        logger.info("Номер карты успешно замаскирован")
        return f"{first_part} {second_part}** **** {last_part}"

    logger.warning("Передан некорректный номер карты")
    return "Введите корректный номер карты"


def get_mask_account(acc_number: int) -> str:
    """Функция маскировки номера банковского счета"""
    acc_number_str = str(acc_number)

    if len(acc_number_str) == 20 and acc_number_str.isdigit():
        return f"**{acc_number_str[-4:]}"
    return "Введите корректный номер счета"
