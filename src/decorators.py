from datetime import datetime
from functools import wraps


def write_log(message, filename=None):
    if filename:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
    else:
        print(message)


def log(filename=None):
    """Логирует вызов функции, результат выполнения и ошибки."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            start_message = (
                f"[{start_time}] {func.__name__} started "
                f"with args={args}, kwargs={kwargs}"
            )
            write_log(start_message, filename)

            try:
                result = func(*args, **kwargs)
            except Exception as error:
                error_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_message = (
                    f"[{error_time}] {func.__name__} error: "
                    f"{type(error).__name__}. Inputs: args={args}, kwargs={kwargs}"
                )
                write_log(error_message, filename)
                raise

            finish_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            finish_message = (
                f"[{finish_time}] {func.__name__} finished successfully "
                f"with result={result}"
            )
            write_log(finish_message, filename)
            return result

        return wrapper

    return decorator
