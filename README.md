# Widget for Banking Operations

Проект предназначен для обработки данных о банковских операциях клиента.

В проекте реализованы функции для:
- маскировки номеров банковских карт и счетов;
- форматирования даты;
- фильтрации операций по статусу;
- сортировки операций по дате.

## Цель проекта

Цель проекта — закрепить работу с функциями, списками словарей, аннотациями типов, сортировкой, фильтрацией, Git, GitHub и GitFlow.

## Структура проекта

```text
widget_for_banking_operations/
├── src/
│   ├── masks.py
│   ├── widget.py
│   └── processing.py
├── main.py
├── pyproject.toml
├── poetry.lock
└── README.md
```

## Установка проекта

Клонируйте репозиторий:

```bash
git clone https://github.com/Liamhoulet10031988/widget_for_banking_operations.git
```

Перейдите в папку проекта:

```bash
cd widget_for_banking_operations
```

Установите зависимости:

```bash
poetry install
```

Активируйте виртуальное окружение:

```bash
poetry shell
```

## Использование функций

### filter_by_state

Функция `filter_by_state` фильтрует список банковских операций по значению ключа `state`.

По умолчанию функция возвращает операции со статусом `EXECUTED`.

Пример:

```python
from src.processing import filter_by_state


operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(operations))
print(filter_by_state(operations, "CANCELED"))
```

### sort_by_date

Функция `sort_by_date` сортирует список банковских операций по дате из ключа `date`.

По умолчанию сортировка выполняется по убыванию: сначала идут самые новые операции.

Пример:

```python
from src.processing import sort_by_date


operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_by_date(operations))
print(sort_by_date(operations, reverse=False))
```

## Запуск проекта

Для запуска демонстрации работы функций используйте команду:

```bash
python main.py
```

## Проверка кода

Для проверки качества кода можно использовать команды:

```bash
poetry run flake8
```

```bash
poetry run mypy .
```

```bash
poetry run isort .
```

## Описание основных функций

### get_mask_card_number

Функция маскирует номер банковской карты.

### get_mask_account

Функция маскирует номер банковского счета.

### mask_account_card

Функция принимает строку с типом карты или счета и номером, а возвращает строку с замаскированным номером.

### get_date

Функция преобразует дату из формата `YYYY-MM-DDTHH:MM:SS` в формат `ДД.ММ.ГГГГ`.

### filter_by_state

Функция возвращает новый список операций, у которых значение ключа `state` совпадает с переданным значением.

### sort_by_date

Функция возвращает новый список операций, отсортированный по дате.

## Обновление для ветки feature/homework_10_2

### Тестирование

Для проекта добавлены автоматические тесты с использованием `pytest`.

Тесты расположены в папке `tests`:

```text
tests/
├── conftest.py
├── test_masks.py
├── test_widget.py
└── test_processing.py
```

В тестах используются:
- фикстуры;
- параметризация;
- проверка покрытия кода тестами.

### Запуск тестов

```bash
poetry run pytest
```

Команда запускает все тесты проекта и показывает результат их выполнения в терминале.

### Проверка покрытия кода

```bash
poetry run pytest --cov=src --cov-report=term-missing --cov-report=html:coverage_html
```

Команда:
- запускает тесты;
- считает процент покрытия кода тестами;
- выводит краткий отчет в терминал;
- создает HTML-отчет в папке `coverage_html/`.

HTML-отчет `coverage_html/index.html`.

### Дополнительная проверка качества кода

```bash
poetry run flake8
poetry run mypy .
poetry run isort .
```

