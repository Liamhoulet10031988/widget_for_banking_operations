import pytest

from src.decorators import log


def test_log_console_success(capsys) -> None:
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add started" in captured.out
    assert "finished successfully" in captured.out
    assert "result=5" in captured.out


def test_log_console_error(capsys) -> None:
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()

    assert "divide started" in captured.out
    assert "ZeroDivisionError" in captured.out
    assert "args=(10, 0)" in captured.out


def test_log_file_success(tmp_path) -> None:
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b

    result = multiply(2, 4)
    content = log_file.read_text(encoding="utf-8")

    assert result == 8
    assert "multiply started" in content
    assert "finished successfully" in content
    assert "result=8" in content


def test_log_file_error(tmp_path) -> None:
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(4, 0)

    content = log_file.read_text(encoding="utf-8")

    assert "divide started" in content
    assert "ZeroDivisionError" in content
    assert "args=(4, 0)" in content


def test_log_preserves_function_name_and_docstring() -> None:
    @log()
    def sample():
        """Тестовая функция."""
        return "ok"

    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Тестовая функция."
