# Homework

This project provides a widget to **display and process bank operations data**. It includes functions for filtering, sorting, masking, and analyzing transaction data through both functional and generator-based approaches.

---

##  Installation

1. **Clone the repository**:

```bash
git clone <repository_url>
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` includes at least the following:

```
masks
pytest
pytest-cov
```

---

##  Usage

The main script is located at:

```
src/main.py
```

It imports and demonstrates usage of functions from:
- `src/processing.py`
- `src/masks.py`
- `src/generators.py`

To run the script:

```bash
python src/main.py
```

You can modify the `test_data` inside `main.py` to test your own transaction samples.

---

##  Functions Overview

###  Data Processing (processing.py)
- `filter_by_state(operations, state='EXECUTED')`  
  Filters a list of operations dictionaries by the `state` key.

- `sort_by_date(operations, reverse=True)`  
  Sorts a list of operation dictionaries by the `date` key (descending by default).

---

###  Data Masking (masks.py)
- `mask_account_card(data)`  
  Automatically detects whether `data` is a card or account and applies masking.

- `get_mask_card_number(card_number)`  
  Masks a card number, leaving only the first 6 and last 4 digits visible.

- `get_mask_account(account_number)`  
  Masks an account number, leaving only the last 4 digits visible.

- `get_data(date_string)`  
  Converts date strings to the format `DD.MM.YYYY`.

---

###  Generators (generators.py)
- `filter_by_currency(transactions, currency_code)`  
  Yields only transactions with a matching currency.

- `transaction_descriptions(transactions)`  
  Yields the description field from each transaction.

- `card_number_generator(start, end)`  
  Generates card numbers in the format `0000 0000 0000 0000` for testing.

---

##  Testing

This project includes a comprehensive test suite using **pytest**. Tests cover:

###  Test Coverage:

#### `masks.py`
- Masks card numbers with different lengths.
- Handles edge cases like empty strings or `None`.

#### `widget.py`
- Detects input types (card/account).
- Masks and formats data appropriately.
- Handles invalid date formats gracefully.

#### `processing.py`
- Filters by operation state.
- Sorts by date in both ascending and descending order.
- Handles missing/invalid date values.

#### `generators.py`
- Filters transactions by currency.
- Extracts transaction descriptions.
- Generates valid formatted card numbers within range.

---

##  Running Tests

Make sure you have `pytest` and `pytest-cov` installed:

```bash
pip install pytest pytest-cov
```

Then run:

```bash
pytest
```

###  Coverage Report

To generate a code coverage report:

```bash
pytest --cov=.
```

To generate a visual HTML report:

```bash
pytest --cov=. --cov-report html
```

This will create an `htmlcov/` directory with `index.html` — open it in your browser to see detailed coverage results.

---

##  Notes

- Use GitFlow: create feature branches off `develop`
- Keep commits atomic and meaningful
- Follow PEP 8 and use linters (e.g. flake8, pylint)


Этот проект лицензирован по [лицензии MIT](LICENSE).
