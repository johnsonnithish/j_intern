import streamlit as st
import matplotlib.pyplot as plt
import io

class full_analysis:
    def __init__(self, records):
        self.records = records

    def incvexp_plot(self):
        by_spend = self.records.groupby("Income/Expense", observed=True)
        spend_summary = by_spend["Amount"].sum()
        fig, ax = plt.subplots(figsize=(4, 4))
        spend_summary.plot(kind="pie", autopct="%1.1f%%", startangle=90, ax=ax)
        ax.set_ylabel("")
        ax.set_title("Income vs Expense Distribution")
        buf = io.BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight")
        st.image(buf, width=300)

    def top_categories_table(self):
        top_cats = (
            self.records[self.records["Income/Expense"] == "Expense"]
            .groupby("Category")["Amount"]
            .sum()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )
        st.subheader("Top 5 Expense Categories")
        st.dataframe(top_cats)

    def monthly_totals_chart(self):
        monthly = (
            self.records
            .groupby(self.records["Date"].dt.to_period("M"))["Amount"]
            .sum()
            .reset_index()
        )
        monthly["Date"] = monthly["Date"].dt.to_timestamp()
        st.subheader("Monthly Total Spending")
        st.line_chart(monthly.set_index("Date"))

    def run_all(self):
        st.header("📊 Analysis Summary")
        self.incvexp_plot()
        self.top_categories_table()
        self.monthly_totals_chart()
