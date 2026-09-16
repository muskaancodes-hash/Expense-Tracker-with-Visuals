import pandas as pd

# Load expense data
df = pd.read_csv("expenses.csv")

print("===== EXPENSE TRACKER =====")

# Show first 10 expenses
print("\nFirst 10 Expenses:")
print(df.head(10))

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Total expenses
print("\nTotal Expenses:")
print("₹", df["Amount"].sum())
# Category-wise expense analysis
print("\n===== CATEGORY-WISE EXPENSES =====")

category_expenses = df.groupby("Category")["Amount"].sum()

print(category_expenses)

highest_category = category_expenses.idxmax()
highest_amount = category_expenses.max()

print("\nHighest Spending Category:")
print(highest_category, "→ ₹", highest_amount)
# Expense visualization
import matplotlib.pyplot as plt

print("\n===== EXPENSE CHART =====")

category_expenses.plot(kind="bar", figsize=(10, 6))

plt.title("Category-wise Expenses")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Date-wise expense analysis
print("\n===== DATE-WISE EXPENSES =====")

df["Date"] = pd.to_datetime(df["Date"])

date_expenses = df.groupby("Date")["Amount"].sum()

print(date_expenses)

print("\nHighest Spending Day:")
highest_day = date_expenses.idxmax()
highest_day_amount = date_expenses.max()

print(highest_day, "→ ₹", highest_day_amount)
# Budget alert
print("\n===== BUDGET ALERT =====")

budget = 50000
total_expenses = df["Amount"].sum()

print("Budget: ₹", budget)
print("Total Expenses: ₹", total_expenses)

if total_expenses > budget:
    print("Alert: You have exceeded your budget!")
else:
    remaining = budget - total_expenses
    print("Budget remaining: ₹", remaining)