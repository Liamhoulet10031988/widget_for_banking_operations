import json

import pandas as pd

from src.utils import get_transactions_from_csv, get_transactions_from_excel, get_transactions_from_json


def test_get_transactions_from_json_valid_list(tmp_path) -> None:
    file_path = tmp_path / "operations.json"
    data = [{"id": 1}, {"id": 2}]
    file_path.write_text(json.dumps(data), encoding="utf-8")

    assert get_transactions_from_json(str(file_path)) == data


def test_get_transactions_from_json_file_not_found() -> None:
    assert get_transactions_from_json("missing_file.json") == []


def test_get_transactions_from_json_empty_file(tmp_path) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    assert get_transactions_from_json(str(file_path)) == []


def test_get_transactions_from_json_invalid_json(tmp_path) -> None:
    file_path = tmp_path / "broken.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    assert get_transactions_from_json(str(file_path)) == []


def test_get_transactions_from_json_dict_instead_of_list(tmp_path) -> None:
    file_path = tmp_path / "wrong_type.json"
    file_path.write_text(json.dumps({"id": 1}), encoding="utf-8")

    assert get_transactions_from_json(str(file_path)) == []


def test_get_transactions_from_csv_valid_file(tmp_path) -> None:
    file_path = tmp_path / "transactions.csv"
    file_path.write_text(
        "id;state;date\n"
        "1;EXECUTED;2024-01-01T10:00:00\n"
        "2;CANCELED;2024-01-02T10:00:00\n",
        encoding="utf-8",
    )

    result = get_transactions_from_csv(str(file_path))

    assert result == [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T10:00:00"},
    ]


def test_get_transactions_from_csv_file_not_found() -> None:
    assert get_transactions_from_csv("missing_file.csv") == []


def test_get_transactions_from_excel_valid_file(tmp_path) -> None:
    file_path = tmp_path / "transactions.xlsx"
    data = pd.DataFrame(
        [
            {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
            {"id": 2, "state": "CANCELED", "date": "2024-01-02T10:00:00"},
        ]
    )
    data.to_excel(file_path, index=False)

    result = get_transactions_from_excel(str(file_path))

    assert result == [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02T10:00:00"},
    ]


def test_get_transactions_from_excel_file_not_found() -> None:
    assert get_transactions_from_excel("missing_file.xlsx") == []
