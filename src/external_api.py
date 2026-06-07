import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_KEY = os.getenv("EXCHANGE_API_KEY")


def get_amount_in_rub(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount

    headers = {"apikey": API_KEY}
    params = {
        "to": "RUB",
        "from": currency_code,
        "amount": amount,
    }

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code != 200:
        return 0.0

    result = response.json()
    return float(result.get("result", 0.0))
