import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f7f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.dashboard-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.dashboard-subtitle {
    color: #666;
    font-size: 17px;
    margin-bottom: 30px;
}

.metric-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    border: 1px solid #eeeeee;
}

.metric-title {
    color: #777;
    font-size: 15px;
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
    margin-top: 8px;
}

.section-title {
    font-size: 23px;
    font-weight: 650;
    margin-top: 25px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- LOAD DATA ----------------

df = pd.read_csv("expenses.csv")

df["Date"] = pd.to_datetime(df["Date"])


# ---------------- SIDEBAR ----------------

st.sidebar.title("💰 Expense Tracker")

st.sidebar.write("Filter your expenses")

categories = ["All"] + sorted(df["Category"].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Select Category",
    categories
)

if selected_category != "All":
    filtered_df = df[df["Category"] == selected_category]
else:
    filtered_df = df.copy()


# ---------------- HEADER ----------------

st.markdown(
    '<div class="dashboard-title">💰 Expense Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Track, analyze and understand your spending in one place.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- CALCULATIONS ----------------

total_expenses = filtered_df["Amount"].sum()

category_expenses = filtered_df.groupby("Category")["Amount"].sum()

if len(category_expenses) > 0:
    highest_category = category_expenses.idxmax()
    highest_amount = category_expenses.max()
else:
    highest_category = "N/A"
    highest_amount = 0

budget = 50000
remaining_budget = budget - total_expenses


# ---------------- SUMMARY CARDS ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">💰 Total Expenses</div>
            <div class="metric-value">₹{total_expenses:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">🛍️ Highest Category</div>
            <div class="metric-value">{highest_category}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">📊 Highest Spending</div>
            <div class="metric-value">₹{highest_amount:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">💵 Budget Remaining</div>
            <div class="metric-value">₹{remaining_budget:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- CHARTS ----------------

st.markdown(
    '<div class="section-title">📊 Spending Overview</div>',
    unsafe_allow_html=True
)

chart1, chart2 = st.columns(2)


# BAR CHART

with chart1:

    st.subheader("Category-wise Expenses")

    fig, ax = plt.subplots(figsize=(7, 5))

    category_expenses.plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("")
    ax.set_ylabel("Amount (₹)")
    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    st.pyplot(fig)


# PIE CHART

with chart2:

    st.subheader("Expense Distribution")

    fig2, ax2 = plt.subplots(figsize=(7, 5))

    category_expenses.plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax2
    )

    ax2.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig2)


# ---------------- BUDGET STATUS ----------------

st.markdown(
    '<div class="section-title">🚨 Budget Status</div>',
    unsafe_allow_html=True
)

budget_used = min(total_expenses / budget, 1.0)

st.progress(budget_used)

if total_expenses > budget:
    st.error(
        f"⚠️ Budget exceeded by ₹{total_expenses - budget:,.0f}"
    )
else:
    st.success(
        f"✅ You have ₹{remaining_budget:,.0f} remaining from your ₹{budget:,.0f} budget."
    )
# ---------------- MONTHLY EXPENSES ----------------

st.markdown(
    '<div class="section-title">📅 Monthly Expenses</div>',
    unsafe_allow_html=True
)

monthly_expenses = (
    filtered_df
    .groupby(filtered_df["Date"].dt.to_period("M"))["Amount"]
    .sum()
)

monthly_expenses.index = monthly_expenses.index.astype(str)

fig3, ax3 = plt.subplots(figsize=(10, 5))

monthly_expenses.plot(
    kind="bar",
    ax=ax3
)

ax3.set_xlabel("Month")
ax3.set_ylabel("Amount (₹)")
ax3.set_title("Monthly Expense Overview")
plt.xticks(rotation=0)

plt.tight_layout()

st.pyplot(fig3)

# ---------------- DATA TABLE ----------------

st.markdown(
    '<div class="section-title">📋 Expense Details</div>',
    unsafe_allow_html=True
)

st.dataframe(
    filtered_df.sort_values("Date", ascending=False),
    use_container_width=True,
    hide_index=True
)


# ---------------- FOOTER ----------------

st.markdown("---")

st.caption(
    "Expense Tracker with Visuals • Built using Python, Pandas, Matplotlib & Streamlit"
)