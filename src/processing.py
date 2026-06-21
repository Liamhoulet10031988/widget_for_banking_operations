import re
from collections import Counter


def filter_by_state(
    list_of_dictionaries: list[dict],
    state: str = "EXECUTED",
) -> list[dict]:
    """Фильтрует список словарей по значению ключа state."""
    filtered_dictionaries = []

    for dictionary in list_of_dictionaries:
        if dictionary.get("state") == state:
            filtered_dictionaries.append(dictionary)

    return filtered_dictionaries


def sort_by_date(
    list_of_dictionaries: list[dict],
    reverse: bool = True,
) -> list[dict]:
    """Сортирует список словарей по дате."""
    return sorted(
        list_of_dictionaries,
        key=lambda dictionary: dictionary["date"],
        reverse=reverse,
    )


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Возвращает операции, в описании которых есть строка поиска."""
    pattern = re.compile(re.escape(search), flags=re.IGNORECASE)

    return [
        operation
        for operation in data
        if pattern.search(str(operation.get("description", "")))
    ]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """Возвращает количество операций по указанным категориям."""
    descriptions = [
        str(operation.get("description", ""))
        for operation in data
    ]
    counter = Counter(descriptions)

    return {
        category: counter.get(category, 0)
        for category in categories
    }
