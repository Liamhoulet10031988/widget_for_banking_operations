import json


def get_transactions_from_json(path: str) -> list[dict]:
    """Функция возвращает список транзакций из JSON файла"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
    if not isinstance(data, list):
        return []

    return data
