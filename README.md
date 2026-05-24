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
## Обновление для ветки feature/homework_11_1

### Новый модуль generators

В проект добавлен модуль `src/generators.py`.

Он содержит функции для обработки больших объемов данных транзакций с помощью генераторов.

### filter_by_currency

Функция `filter_by_currency` принимает список транзакций и код валюты, а затем по очереди возвращает только те транзакции, которые соответствуют нужной валюте.

Пример:

```python
from src.generators import filter_by_currency


usd_transactions = filter_by_currency(transactions, "USD")

print(next(usd_transactions))
print(next(usd_transactions))
```

### transaction_descriptions

Функция-генератор `transaction_descriptions` принимает список транзакций и по очереди возвращает описание каждой операции.

Пример:

```python
from src.generators import transaction_descriptions


descriptions = transaction_descriptions(transactions)

print(next(descriptions))
print(next(descriptions))
```

### card_number_generator

Функция-генератор `card_number_generator` генерирует номера карт в формате `XXXX XXXX XXXX XXXX` в заданном диапазоне.

Пример:

```python
from src.generators import card_number_generator


for card_number in card_number_generator(1, 5):
    print(card_number)
```

## Тестирование

Для нового функционала добавлен модуль тестов `tests/test_generators.py`.

В нем проверяются:

- `filter_by_currency`;
- `transaction_descriptions`;
- `card_number_generator`.

В `tests/conftest.py` добавлены новые фикстуры с тестовыми транзакциями.

В тестах используются:

- `@pytest.fixture` — для подготовки тестовых данных;
- `@pytest.mark.parametrize` — для проверки нескольких вариантов входных данных в одном тесте.

## Обновление для ветки feature/homework_11_2

### Новый модуль decorators

В проект добавлен модуль `src/decorators.py`.

В нем реализован декоратор `log`, который позволяет автоматически логировать:

- время вызова функции;
- имя функции;
- переданные аргументы;
- результат выполнения;
- информацию об ошибках.

### Использование декоратора `log`

Если `filename` не передан, лог выводится в консоль:

```python
from src.decorators import log


@log()
def add(a, b):
    return a + b
```

Если `filename` передан, лог записывается в файл:

```python
from src.decorators import log


@log(filename="app.log")
def multiply(a, b):
    return a * b
```

### Тестирование

Для нового функционала добавлен файл `tests/test_decorators.py`.

В тестах проверяются:

- успешный вывод логов в консоль;
- логирование ошибок в консоль;
- успешная запись логов в файл;
- запись ошибок в файл;
- сохранение имени и `docstring` через `wraps`.

Для проверки вывода в консоль используется фикстура `capsys`.

Для проверки записи в файл используется встроенная фикстура `tmp_path`, которая создает временный путь для тестового файла.

Запуск тестов:

```bash
poetry run pytest
```

Проверка покрытия:

```bash
poetry run pytest --cov=src --cov-report=term-missing --cov-report=html:coverage_html
```
