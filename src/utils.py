import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)

if not logger.handlers:
    if not os.path.exists("logs"):
        os.mkdir("logs")

    file_handlers = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handlers.setFormatter(formatter)

    logger.addHandler(file_handlers)
    logger.propagate = False


def get_transactions_from_json(path: str) -> list[dict]:
    """Функция возвращает список транзакций из JSON файла"""
    logger.info(f"Открытие JSON-файла: {path} ")
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []
    except json.decoder.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON-файла: {path}")
        return []
    if not isinstance(data, list):
        logger.warning(f"Данный в файле {path} не являются списком")
        return []

    logger.info(f"JSON-файл {path} успешно прочитан")

    return data
