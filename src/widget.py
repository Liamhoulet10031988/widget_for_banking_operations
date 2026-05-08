from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_details: str) -> str:
    """Маскирует номер карты или счета в строке с платежными данными."""
    parts = payment_details.split()

    payment_number = parts[-1]
    payment_name = " ".join(parts[:-1])

    if len(payment_number) == 16:
        masked_number = get_mask_card_number(int(payment_number))
    elif len(payment_number) == 20:
        masked_number = get_mask_account(int(payment_number))
    else:
        return "Некорректный формат номера"

    return f"{payment_name} {masked_number}"


def get_date(date: str) -> str:
    """Преобразует дату в формат ДД.ММ.ГГГГ."""
    result_date = date[0:10]
    result_final = result_date.split("-")
    result_final.reverse()
    result_date = ".".join(result_final)

    return result_date
