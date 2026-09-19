import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load expense data
df = pd.read_csv("expenses.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Page title
st.title("💰 Expense Tracker Dashboard")
st.write("Track and analyze your expenses easily.")

# Total expenses
total_expenses = df["Amount"].sum()

# Highest spending category
category_expenses = df.groupby("Category")["Amount"].sum()
highest_category = category_expenses.idxmax()
highest_amount = category_expenses.max()

# Budget
budget = 50000
remaining_budget = budget - total_expenses

# Summary
st.subheader("Expense Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Total Expenses", f"₹{total_expenses}")
col2.metric("Highest Category", highest_category)
col3.metric("Remaining Budget", f"₹{remaining_budget}")

# Category-wise chart
st.subheader("Category-wise Expenses")

fig, ax = plt.subplots()
category_expenses.plot(kind="bar", ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Amount (₹)")
ax.set_title("Expenses by Category")
plt.xticks(rotation=45)

st.pyplot(fig)

# Expense data
st.subheader("Expense Data")
st.dataframe(df)

# Budget alert
st.subheader("Budget Status")

if total_expenses > budget:
    st.error("You have exceeded your budget!")
else:
    st.success(f"You have ₹{remaining_budget} remaining in your budget.")