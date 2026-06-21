from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import get_transactions_from_csv, get_transactions_from_excel, get_transactions_from_json
from src.widget import get_date, mask_account_card


def load_transactions_by_user_choice() -> list[dict]:
    """Спрашивает пользователя, из какого файла загрузить операции."""
    while True:
        print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Программа: Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        user_choice = input("\nПользователь: ").strip()

        if user_choice == "1":
            print("\nПрограмма: Для обработки выбран JSON-файл.")
            return get_transactions_from_json("data/operations.json")
        if user_choice == "2":
            print("\nПрограмма: Для обработки выбран CSV-файл.")
            return get_transactions_from_csv("data/transactions.csv")
        if user_choice == "3":
            print("\nПрограмма: Для обработки выбран XLSX-файл.")
            return get_transactions_from_excel("data/transactions_excel.xlsx")

        print("\nПрограмма: Такого пункта нет. Введите 1, 2 или 3.\n")


def get_user_status() -> str:
    """Запрашивает статус операции и возвращает его в верхнем регистре."""
    available_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input(
            "\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\n"
            "Пользователь: "
        ).strip().upper()

        if status in available_statuses:
            print(f'\nПрограмма: Операции отфильтрованы по статусу "{status}".')
            return status

        print(f'\nПрограмма: Статус операции "{status}" недоступен.')


def ask_sorting(transactions: list[dict]) -> list[dict]:
    """Спрашивает пользователя, нужно ли сортировать операции по дате."""
    answer = input("\nПрограмма: Отсортировать операции по дате? Да/Нет\n\nПользователь: ").strip().lower()

    if answer != "да":
        return transactions

    sort_order = input(
        "\nПрограмма: Отсортировать по возрастанию или по убыванию?\n\n"
        "Пользователь: "
    ).strip().lower()

    reverse = sort_order not in {"по возрастанию", "возрастанию"}
    return sort_by_date(transactions, reverse=reverse)


def get_amount_and_currency(transaction: dict) -> tuple[str, str]:
    """Возвращает сумму и код валюты из JSON-, CSV- или XLSX-операции."""
    operation_amount = transaction.get("operationAmount")

    if isinstance(operation_amount, dict):
        amount = operation_amount.get("amount", "")
        currency = operation_amount.get("currency", {})

        if isinstance(currency, dict):
            return str(amount), str(currency.get("code", ""))

        return str(amount), ""

    return str(transaction.get("amount", "")), str(transaction.get("currency_code", ""))


def get_currency_code(transaction: dict) -> str:
    """Возвращает код валюты операции."""
    _, currency_code = get_amount_and_currency(transaction)
    return currency_code


def ask_rub_filter(transactions: list[dict]) -> list[dict]:
    """Спрашивает пользователя, нужно ли оставить только рублевые операции."""
    answer = input(
        "\nПрограмма: Выводить только рублевые транзакции? Да/Нет\n\n"
        "Пользователь: "
    ).strip().lower()

    if answer != "да":
        return transactions

    return [
        transaction
        for transaction in transactions
        if get_currency_code(transaction) == "RUB"
    ]


def ask_description_search(transactions: list[dict]) -> list[dict]:
    """Спрашивает пользователя, нужно ли искать операции по слову в описании."""
    answer = input(
        "\nПрограмма: Отфильтровать список транзакций по определенному слову "
        "в описании? Да/Нет\n\n"
        "Пользователь: "
    ).strip().lower()

    if answer != "да":
        return transactions

    search = input("\nПрограмма: Введите слово для поиска в описании:\n\nПользователь: ").strip()

    if not search:
        return transactions

    return process_bank_search(transactions, search)


def is_empty_value(value: object) -> bool:
    """Проверяет пустые значения из JSON, CSV и XLSX."""
    return value is None or str(value).strip() == "" or str(value).lower() == "nan"


def mask_payment_data(value: object) -> str:
    """Маскирует карту или счет, если значение можно замаскировать."""
    if is_empty_value(value):
        return "Не указано"

    try:
        return mask_account_card(str(value))
    except (IndexError, ValueError):
        return str(value)


def get_transaction_direction(transaction: dict) -> str:
    """Возвращает направление операции в удобном для чтения виде."""
    sender = transaction.get("from")
    receiver = transaction.get("to")

    if not is_empty_value(sender) and not is_empty_value(receiver):
        return f"{mask_payment_data(sender)} -> {mask_payment_data(receiver)}"

    if not is_empty_value(receiver):
        return mask_payment_data(receiver)

    return "Не указано"


def print_transactions(transactions: list[dict]) -> None:
    """Выводит итоговый список операций."""
    if not transactions:
        print("\nПрограмма: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print("\nПрограмма: Распечатываю итоговый список транзакций...")
    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:
        date = str(transaction.get("date", ""))
        formatted_date = get_date(date) if date else "Дата не указана"
        description = str(transaction.get("description", "Описание не указано"))
        amount, currency_code = get_amount_and_currency(transaction)

        print()
        print(f"{formatted_date} {description}")
        print(get_transaction_direction(transaction))
        print(f"Сумма: {amount} {currency_code}")


def main() -> None:
    """Запускает интерактивную программу обработки банковских операций."""
    transactions = load_transactions_by_user_choice()

    if not transactions:
        print("\nПрограмма: Не удалось загрузить операции из выбранного файла.")
        return

    status = get_user_status()
    transactions = filter_by_state(transactions, status)
    transactions = ask_sorting(transactions)
    transactions = ask_rub_filter(transactions)
    transactions = ask_description_search(transactions)
    print_transactions(transactions)


if __name__ == "__main__":
    main()
