# main_app.py
import streamlit as st
import matplotlib.pyplot as plt

from data_loader import load_data
from analysis import (
    prepare_aggregates,
    get_top3_per_month,
    get_needs_data,
    get_others_data
)

records = load_data()
by_spend, monthly_income = prepare_aggregates(records)


st.title("Monthly Spending Overview")
st.dataframe(records, hide_index=True)


spend_summary = by_spend["Amount"].sum()
fig, ax = plt.subplots()
spend_summary.plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax)
ax.set_ylabel("")
ax.set_title("Income vs Expense Distribution")
st.pyplot(fig)


top3 = get_top3_per_month(records, monthly_income)
st.subheader("Top 3 Spending Categories per Month")
st.dataframe(top3, hide_index=True)


needs = ["Food", "Transportation", "Household", "Education"]

st.subheader("Monthly NEED Spending")
needs_df, needs_amt = get_needs_data(records, needs)
st.dataframe(needs_df, hide_index=True)

st.subheader("Monthly OTHER Spending")
others_df, other_amt = get_others_data(records, needs)
st.dataframe(others_df, hide_index=True)


savings = 0
if "Savings" not in records["Category"].unique():
    st.caption("No savings category found in the records.")


st.subheader("Category wise Spending")
labels = ['Needs', 'Others', 'Savings']
sizes = [needs_amt, other_amt, savings]

fig2, ax2 = plt.subplots()
ax2.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
ax2.set_title("Needs vs Other Spending Distribution")
ax2.axis("equal")
st.pyplot(fig2)
