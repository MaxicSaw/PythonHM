# Homework

This project provides a widget for displaying and processing bank operations data, including filtering and sorting.

Installation:

```bash
git clone <repository_url>
```
```bash
pip install -r requirements.txt
```

# Usage:

Run main.py:
```bash
python main.py
``` 

Follow the interactive menu to:

* Load transactions from JSON, CSV, or XLSX files

* Filter transactions by status (EXECUTED, CANCELED, PENDING)

* Sort transactions by date (ascending/descending)

* Filter by currency (RUB only or all)

* Search in transaction descriptions

* View category statistics

### Main Features
Core Modules

* Interactive command-line interface
* Transaction processing pipeline
* Integrated display of masked transaction data
* Statistical analysis by categories

### Newly Added Functions:
* process_transactions() - Main transaction processing workflow 
* print_transaction() - Formats and displays transaction details 
* get_user_choice() - Handles user input with validation 
* filter_transactions_by_description() - Regex-based description search 
* count_transactions_by_category() - Category statistics counter

### Existing Functions (Enhanced):
* filter_by_state() - Now case-insensitive 
* sort_by_date() - Supports both ascending/descending
* mask_account_card() - Improved account/card detection 
* calculate_transaction_amount() - Added currency conversion

## Function Details

Data Processing (processing.py)
```python
filter_by_state(operations, state='EXECUTED')  # Case-insensitive filtering
sort_by_date(operations, reverse=True)         # Date sorting
count_transactions_by_category(transactions, categories)  # New category counter
```
Data Masking (masks.py, widget.py)
```python
mask_account_card(data)                # Automatically detects account/card
get_mask_card_number(card_number)      # Shows first 6/last 4 digits (XXXXXX****XX)
get_mask_account(account_number)       # Shows last 4 digits (****XXXX)
```
Utilities (regex_utils.py, external_api.py)
```python
filter_transactions_by_description(transactions, pattern)  # Regex search
calculate_transaction_amount(transaction)  # Automatic RUB conversion
```
Generators (generators.py)
```python
card_number_generator(start, end)      # Test card number generator
filter_by_currency(transactions, code) # Currency filter
transaction_descriptions(transactions) # Description extractor
```
@log Decorator (decorators.py)
```python
from src.decorators import log

@log  # Console logging
def my_function(x, y):
    return x + y

@log(filename="app.log")  # File logging
def another_function():
    raise ValueError("Error example")
```

## Features:

Logs function start/end

Records arguments and results

Captures exceptions

Console or file output

# Testing:

### New Test Coverage
Main application workflow

User input handling

Transaction display formatting

Category statistics calculation

Regex-based search functionality

Running Tests:
```bash
# Install dependencies
pip install pytest pytest-cov
```
```bash
# Run all tests
pytest tests/
```
```bash
# With coverage report
pytest --cov=src tests/
```
```bash
# HTML coverage report
pytest --cov=src --cov-report html
open htmlcov/index.html
```
# Data Formats
### Supported input formats:

JSON (via utils.py)

CSV (via transaction_reader.py)

Excel (via transaction_reader.py)

### Sample transaction structure:
```json
{
  "date": "2023-05-15T14:30:00",
  "description": "Payment",
  "from": "Visa 1234567812345678",
  "to": "Счет 1234567890123456",
  "operationAmount": {
    "amount": "100.00",
    "currency": {"code": "USD"}
  },
  "state": "EXECUTED"
}
```