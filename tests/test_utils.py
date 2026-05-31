import json

from src.utils import get_transactions_from_json


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
