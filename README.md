# Expense-Tracker-with-Visuals
A Python-based expense tracker that analyzes expenses, generates visual insights, and helps users monitor their spending.
# Expense Tracker with Visuals

## Part 1: Load and Inspect Expense Data

In this part, expense data is loaded from a CSV file using **Pandas**.

The program performs basic data analysis by:

* Loading the `expenses.csv` file
* Displaying the first 10 expenses
* Checking the dataset shape
* Displaying column names
* Checking for missing values
* Calculating total expenses

### Tools Used

* Python
* Pandas
* CSV

### Dataset Columns

* Date
* Category
* Amount
* Description

### Result

The program successfully loads and analyzes the expense dataset and calculates the total amount spent.
# Part 2: Category-wise Expense Analysis

In this part, the expense data is analyzed based on different categories.

### What This Part Does

* Groups expenses according to their category
* Calculates the total spending for each category
* Displays category-wise expenses
* Identifies the category with the highest spending

### Python Concept Used

* `groupby()`
* `sum()`
* `idxmax()`
* `max()`

### Result

The program successfully calculates total expenses for each category and identifies the highest spending category.
