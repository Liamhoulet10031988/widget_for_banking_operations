from src.widget import get_date, mask_account_card


def main() -> None:
    """Точка входа для проверки работы функций."""
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(get_date("2024-03-11T02:26:18.671407"))


if __name__ == "__main__":
    main()