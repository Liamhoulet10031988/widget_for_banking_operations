from unittest.mock import Mock, patch

from src.external_api import get_amount_in_rub


def test_get_amount_in_rub_for_rub(rub_transaction: dict) -> None:
    assert get_amount_in_rub(rub_transaction) == 100.50


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_for_usd(mock_get: Mock, usd_transaction: dict) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 987.65}

    result = get_amount_in_rub(usd_transaction)

    assert result == 987.65
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_for_eur(mock_get: Mock, eur_transaction: dict) -> None:
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 1999.99}

    result = get_amount_in_rub(eur_transaction)

    assert result == 1999.99
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_get_amount_in_rub_bad_status(mock_get: Mock, usd_transaction: dict) -> None:
    mock_get.return_value.status_code = 500

    assert get_amount_in_rub(usd_transaction) == 0.0
