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
* # Part 3: Expense Visualization

In this part, expense data is visualized using a bar chart.

### What This Part Does

* Displays category-wise expenses in a bar chart
* Compares spending across different categories
* Uses Matplotlib for data visualization
* Adds chart title and labels for better understanding

### Tool Used

* Python
* Pandas
* Matplotlib

### Result

A bar chart is generated to clearly show spending patterns across different expense categories.
# Part 4: Date-wise Expense Analysis

In this part, the expense data is analyzed based on dates.

### What This Part Does

* Converts the Date column into datetime format
* Groups expenses by date
* Calculates total spending for each day
* Identifies the highest spending day

### Python Concepts Used

* `pd.to_datetime()`
* `groupby()`
* `sum()`
* `idxmax()`
* `max()`

### Result

The program successfully analyzes daily spending and identifies the highest spending day.



### Result

The program successfully calculates total expenses for each category and identifies the highest spending category.
# Part 5: Budget Alert

In this part, a budget alert feature is added to the expense tracker.

### What This Part Does

* Sets a spending budget
* Calculates total expenses
* Compares expenses with the budget
* Shows an alert when the budget is exceeded
* Displays the remaining budget when expenses are within the limit

### Result

For the current dataset:

* Budget: ₹50,000
* Total Expenses: ₹49,560
* Remaining Budget: ₹440

The budget alert feature successfully monitors spending against the set budget.
