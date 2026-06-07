def filter_by_currency(transactions: list[dict], currency_code: str):
    """Фильтрует транзакции по коду валюты."""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        currency = operation_amount.get("currency", {})

        if currency.get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]):
    """Возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
