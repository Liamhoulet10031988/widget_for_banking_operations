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