# Python Programming Practical Tasks

A collection of practical Python programming exercises covering loops, conditional statements, NumPy arrays, and Object-Oriented Programming through a simple Bank Account System.

This project contains three small, beginner-friendly programs. Each program focuses on a core Python topic and is written with clear variable names and comments so that it is easy to read, run, and explain.

## Learning Objectives

- Use `for` loops to repeat a task a fixed number of times.
- Use `if` / `elif` / `else` statements to make decisions.
- Take user input and validate it.
- Calculate totals, averages, and percentages.
- Create NumPy arrays and convert their data types.
- Understand Object-Oriented Programming: classes, objects, constructors, attributes, and methods.
- Format output neatly, including monetary values to two decimal places.

## Technologies Used

| Technology | Purpose |
| ---------- | ------- |
| Python 3 | Programming language used for all tasks |
| NumPy | Array creation and data type conversion (Task 2) |

## Project Structure

```text
python-programming-practical-tasks/
│
├── task1_sales_tax.py      # Task 1: Sales employee tax calculator
├── task2_numpy_array.py    # Task 2: NumPy array data type conversion
├── task3_bank_account.py   # Task 3: Bank account system using OOP
├── README.md               # Project documentation
├── requirements.txt        # Required Python packages
└── .gitignore              # Files and folders ignored by Git
```

## Task Descriptions

### Task 1 — Sales Employee Tax Calculator

**File:** `task1_sales_tax.py`

A mobile phone shop has 5 sales employees. The program uses a `for` loop to ask for the daily sales amount (in Rs.) of each employee, then calculates the tax using these rules:

| Sales Amount | Tax Rate |
| ------------ | -------- |
| Less than Rs. 50,000 | 5% |
| Rs. 50,000 to Rs. 100,000 | 10% |
| Greater than Rs. 100,000 | 15% |

For each employee, the program displays the sales amount and the tax amount. After all 5 employees have been entered, it displays the **total sales** and the **average sales**.

**Input validation:**

- If the user enters something that is not a number, the program shows an error and asks again.
- If the user enters a negative amount, the program shows an error and asks again.

### Task 2 — NumPy Array Data Type Conversion

**File:** `task2_numpy_array.py`

The program:

1. Creates a NumPy array containing `[78, 85, 92, 67, 88]`.
2. Displays the original integer array and its data type.
3. Converts the array to the `float` data type using `astype()`.
4. Displays the converted float array and its data type.

### Task 3 — Bank Account System using OOP

**File:** `task3_bank_account.py`

A simple bank account system built with two classes:

| Class | Attributes | Methods |
| ----- | ---------- | ------- |
| `Customer` | `name`, `customer_id` | `display_customer_info()` |
| `Account` | `account_number`, `customer`, `balance` | `deposit()`, `withdraw()`, `display_balance()`, `display_account_info()` |

Each `Account` object stores a `Customer` object, which links the account to its owner.

**Rules:**

- Deposit and withdrawal amounts must be greater than zero.
- A withdrawal cannot be greater than the available balance.
- A success or error message is shown for every transaction.

The program includes a demonstration that creates a customer and an account, deposits and withdraws money, and shows what happens with invalid transactions.

## Installation

1. Make sure **Python 3** is installed:

   ```bash
   python --version
   ```

2. Clone the repository and open the project folder:

   ```bash
   git clone https://github.com/ah0890/python-programming-practical-tasks.git
   cd python-programming-practical-tasks
   ```

3. *(Optional but recommended)* Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (Command Prompt): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`

## Installing NumPy

NumPy is only needed for Task 2. Install it using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Or install it directly:

```bash
pip install numpy
```

To check that NumPy is installed:

```bash
python -c "import numpy; print(numpy.__version__)"
```

## How to Run Each Program

Run each program from the project folder:

```bash
python task1_sales_tax.py
python task2_numpy_array.py
python task3_bank_account.py
```

> On some systems (macOS / Linux), you may need to use `python3` instead of `python`.

## Expected Output Examples

### Task 1 Output

Example input: `49999`, `50000`, `100000`, `100001`, `25000`

```text
=============================================
      SALES EMPLOYEE TAX CALCULATOR
=============================================

Employee 1
---------------------------------------------
Enter sales amount (Rs.): 49999
Sales Amount : Rs. 49,999.00
Tax Amount   : Rs. 2,499.95

Employee 2
---------------------------------------------
Enter sales amount (Rs.): 50000
Sales Amount : Rs. 50,000.00
Tax Amount   : Rs. 5,000.00

Employee 3
---------------------------------------------
Enter sales amount (Rs.): 100000
Sales Amount : Rs. 100,000.00
Tax Amount   : Rs. 10,000.00

Employee 4
---------------------------------------------
Enter sales amount (Rs.): 100001
Sales Amount : Rs. 100,001.00
Tax Amount   : Rs. 15,000.15

Employee 5
---------------------------------------------
Enter sales amount (Rs.): 25000
Sales Amount : Rs. 25,000.00
Tax Amount   : Rs. 1,250.00

=============================================
                 SUMMARY
=============================================
Total Sales   : Rs. 325,000.00
Average Sales : Rs. 65,000.00
=============================================
```

Invalid input example:

```text
Enter sales amount (Rs.): abc
Invalid input! Please enter a number.
Enter sales amount (Rs.): -500
Sales amount cannot be negative. Please try again.
Enter sales amount (Rs.): 45000
```

### Task 2 Output

```text
========================================
   NUMPY ARRAY DATA TYPE CONVERSION
========================================

Original Array : [78 85 92 67 88]
Data Type      : int64

Converted Array: [78. 85. 92. 67. 88.]
Data Type      : float64
========================================
```

> The dot after each number (for example `78.`) shows that the values are now floats. On some Windows systems, the original data type may appear as `int32`.

### Task 3 Output

```text
=============================================
          BANK ACCOUNT SYSTEM
=============================================

--- Account Created ---
Customer Name  : Ali Khan
Customer ID    : C001
Account Number : ACC-1001
Current Balance: Rs. 5,000.00

--- Deposit Rs. 2,500 ---
Success: Rs. 2,500.00 deposited.
Current Balance: Rs. 7,500.00

--- Withdraw Rs. 3,000 ---
Success: Rs. 3,000.00 withdrawn.
Current Balance: Rs. 4,500.00

--- Withdraw Rs. 10,000 (more than balance) ---
Error: Insufficient balance. Available balance is Rs. 4,500.00.
Current Balance: Rs. 4,500.00

--- Deposit Rs. 0 (invalid amount) ---
Error: Deposit amount must be greater than zero.

--- Withdraw Rs. -500 (invalid amount) ---
Error: Withdrawal amount must be greater than zero.

--- Final Account Details ---
Customer Name  : Ali Khan
Customer ID    : C001
Account Number : ACC-1001
Current Balance: Rs. 4,500.00
=============================================
```

## Python Concepts Demonstrated

| Concept | Task 1 | Task 2 | Task 3 |
| ------- | :----: | :----: | :----: |
| Variables and constants | ✔ | ✔ | ✔ |
| User input (`input()`) | ✔ | | |
| Type conversion (`float()`) | ✔ | | |
| `for` loop | ✔ | | |
| `while` loop | ✔ | | |
| `if` / `elif` / `else` | ✔ | | ✔ |
| Exception handling (`try` / `except`) | ✔ | | |
| f-strings and number formatting | ✔ | | ✔ |
| Importing a library | | ✔ | |
| NumPy arrays and `dtype` | | ✔ | |
| Data type conversion (`astype()`) | | ✔ | |
| Classes and objects | | | ✔ |
| Constructors (`__init__`) | | | ✔ |
| Attributes and methods | | | ✔ |
| Object inside another object (composition) | | | ✔ |
| Input validation | ✔ | | ✔ |
