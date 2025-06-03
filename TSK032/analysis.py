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

    def needs(self):
        self.needs_l = ['food', 'transport', 'entertainment', 'utilities', 'rent', 'groceries', 'education']
        needs_df = (
            self.records[self.records["Category"].str.lower().isin(self.needs_l)]
            .groupby([self.records["Date"].dt.to_period("M"), "Category"], observed=True)["Amount"]
            .sum()
            .reset_index()
        )
        needs_df["Date"] = needs_df["Date"].dt.to_timestamp().dt.strftime("%B %Y")
        return needs_df["Amount"].sum()


    def wants(self):
        wants_df = (
            self.records[
                ~self.records["Category"].str.lower().isin(self.needs_l + ["savings"])
            ]
            .groupby([self.records["Date"].dt.to_period("M"), "Category"], observed=True)["Amount"]
            .sum()
            .reset_index()
        )
        wants_df["Date"] = wants_df["Date"].dt.to_timestamp().dt.strftime("%B %Y")
        return wants_df["Amount"].sum()
    
    def savings(self):
        savings_df = (
            self.records[self.records["Category"].str.lower() == "savings"]
            .groupby([self.records["Date"].dt.to_period("M"), "Category"], observed=True)["Amount"]
            .sum()
            .reset_index()
        )
        savings_df["Date"] = savings_df["Date"].dt.to_timestamp().dt.strftime("%B %Y")
        return savings_df["Amount"].sum()
    
    def category_split_pie(self):
        needs_amt = self.needs()
        wants_amt = self.wants()
        savings_amt = self.savings()
        labels = ['Needs', 'Wants', 'Savings']
        sizes = [needs_amt, wants_amt, savings_amt]
        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title("Spending Distribution")
        ax.axis('equal') 
        st.subheader("Needs vs Wants vs Savings")
        st.pyplot(fig)

    def run_all(self):
        st.header("Analysis Summary")
        self.incvexp_plot()
        self.top_categories_table()
        self.monthly_totals_chart()
        self.category_split_pie()
