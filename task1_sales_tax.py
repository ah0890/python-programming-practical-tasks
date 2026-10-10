# Task 1: Sales Employee Tax Calculator
# A mobile phone shop has 5 sales employees. This program asks for the
# daily sales amount (in Rs.) of each employee, calculates the tax on it,
# and finally shows the total and average sales.

NUMBER_OF_EMPLOYEES = 5

total_sales = 0.0

print("=" * 45)
print("      SALES EMPLOYEE TAX CALCULATOR")
print("=" * 45)

# Repeat once for each employee (1 to 5)
for employee in range(1, NUMBER_OF_EMPLOYEES + 1):
    print(f"\nEmployee {employee}")
    print("-" * 45)

    # Keep asking until the user enters a valid, non-negative number
    while True:
        try:
            sales = float(input("Enter sales amount (Rs.): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if sales < 0:
            print("Sales amount cannot be negative. Please try again.")
        else:
            break

    # Calculate tax according to the sales amount
    if sales < 50000:
        tax = sales * 0.05
    elif sales <= 100000:
        tax = sales * 0.10
    else:
        tax = sales * 0.15

    # Add this employee's sales to the running total
    total_sales = total_sales + sales

    print(f"Sales Amount : Rs. {sales:,.2f}")
    print(f"Tax Amount   : Rs. {tax:,.2f}")

# Calculate the average after all employees have been entered
average_sales = total_sales / NUMBER_OF_EMPLOYEES

print("\n" + "=" * 45)
print("                 SUMMARY")
print("=" * 45)
print(f"Total Sales   : Rs. {total_sales:,.2f}")
print(f"Average Sales : Rs. {average_sales:,.2f}")
print("=" * 45)
