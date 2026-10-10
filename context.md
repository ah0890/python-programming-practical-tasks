# Project Context

This file records the background, decisions, and current state of this project so that work can continue smoothly in future sessions. Update it whenever something important changes.

**Last updated:** 2026-10-10

## Project Summary

- **Name:** python-programming-practical-tasks
- **Type:** Beginner-level academic Python project (to be explained in a viva)
- **Repository:** https://github.com/ah0890/python-programming-practical-tasks
- **Branch:** `main`
- **Description:** A collection of practical Python programming exercises covering loops, conditional statements, NumPy arrays, and Object-Oriented Programming through a simple Bank Account System.

## Files

| File | Purpose |
| ---- | ------- |
| `task1_sales_tax.py` | Task 1: Sales tax for 5 employees using a `for` loop and `if/elif/else` |
| `task2_numpy_array.py` | Task 2: NumPy integer array converted to float with `astype()` |
| `task3_bank_account.py` | Task 3: `Customer` and `Account` classes (OOP) |
| `README.md` | Full project documentation |
| `requirements.txt` | `numpy` |
| `.gitignore` | Python, virtual environment, IDE, and OS files |
| `context.md` | This file |

## Development Workflow Rules

These are the owner's rules and must be followed:

- Work **one step at a time**. Stop after each step and wait for confirmation.
- **Never** run `git init`, `git commit`, `git push`, or create repositories. The owner commits and pushes manually.
- After each step, give: what was done, files changed, how to test, the exact commit message, and the exact git commands.
- Do not rewrite or manipulate Git history.
- Keep code beginner-friendly: clear names, simple comments, no unnecessary complexity or dependencies.

## Current Status

**All 7 planned steps are complete.** Working tree is clean and pushed.

| Step | Description | Status |
| ---- | ----------- | ------ |
| 1 | Project setup (README, requirements, .gitignore) | Done |
| 2 | Task 1: sales tax calculator | Done |
| 3 | Task 1: reject negative sales amounts | Done (committed as "task1_sales_tax.py updated") |
| 4 | Task 2: NumPy array conversion | Done |
| 5 | Task 3: OOP bank account system | Done |
| 6 | Full README documentation | Done |
| 7 | Final code review | Done |

### Git History

```text
2aa706d Use float for total sales to fix type checker warning
a5d945d task1_sales_tax.py updated
a142f99 Add project documentation
1590ae5 Add OOP bank account system
e940fc2 Add NumPy array data type conversion
55c9bf9 Add sales employee tax calculator
4fa74e0 Initial project setup
97b1fbc Initial commit
```

## Key Implementation Decisions

### Task 1 — Sales Tax

- Tax boundaries (exact, as required):
  - `sales < 50000` → 5%
  - `sales <= 100000` → 10% (so 50,000 and 100,000 are both 10%)
  - otherwise → 15%
- Number of employees is stored in the constant `NUMBER_OF_EMPLOYEES = 5` and used by both the loop and the average.
- `total_sales` starts at `0.0` (not `0`) to keep the Mypy type checker happy.
- Input validation: non-numbers and negative numbers are rejected and the user is asked again. Zero is allowed (an employee may sell nothing).
- Known and accepted: `nan` / `inf` are accepted by `float()`. Not handled, to keep the code simple.

### Task 2 — NumPy

- `marks = np.array([78, 85, 92, 67, 88])` → `marks.astype(float)`.
- Shows `dtype` before (`int64`) and after (`float64`). On some Windows/older NumPy versions the original may show as `int32`.

### Task 3 — Bank Account

- `Account` stores a `Customer` object (composition).
- `deposit()` / `withdraw()` reject amounts `<= 0`; `withdraw()` rejects amounts greater than the balance. Errors use `return` so the balance never changes.
- Known and accepted: the opening balance passed to `Account(...)` is not validated (it is not a transaction).
- Demo uses customer "Ali Khan" (C001), account "ACC-1001", opening balance Rs. 5,000; final balance Rs. 4,500.

## Environment Notes

- Python 3.14.5 (global). NumPy is **not** installed globally.
- A local virtual environment `.venv/` (ignored by Git) has NumPy 2.5.3 installed. Use `.venv\Scripts\python` (or activate it) to run Task 2.
- VS Code has the Mypy extension, which creates `.mypy_cache/` (it contains its own `.gitignore`, so Git ignores it).
- Windows Git shows "LF will be replaced by CRLF" warnings. These are harmless.

## Lessons Learned

- **Stale editor tabs:** VS Code once showed an old version of `task1_sales_tax.py` after the file was changed on disk. Saving that old tab overwrote newer code, which is why the Step 3 change was lost several times. Always reopen the file from Explorer before saving if it may have been changed outside the editor.
- Committing with `git add <single file>` means other modified files are left out. Check `git status` after every commit.

## Viva Quick Notes

- **Why `elif sales <= 100000` is enough:** the first `if` already handled everything below 50,000.
- **`continue` / `break`:** `continue` restarts the input loop after a bad entry; `break` exits it once the input is valid.
- **`astype()`:** returns a new array; the original is unchanged.
- **`self`:** refers to the specific object the method is working on.
- **`__init__`:** the constructor; runs automatically when an object is created.
- **Composition:** `self.customer.display_customer_info()` calls a method on the `Customer` object stored inside the `Account`.

## Change Log

| Date | Change |
| ---- | ------ |
| 2026-10-10 | Steps 1–7 completed; Mypy type warning fixed in Task 1; `context.md` created |
