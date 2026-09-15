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