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