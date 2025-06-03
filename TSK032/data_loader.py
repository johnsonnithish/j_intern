import pandas as pd
from analysis import full_analysis
import streamlit as st
def sample_data():
    records = pd.read_csv(
        "expense_data_1.csv",
        usecols=["Date", "Category", "Income/Expense", "Amount"],
        converters={"Date": pd.to_datetime},
        dtype={
            "Income/Expense": "category",
            "Category": "category"
        }
    )
    analysis = full_analysis(records)
    analysis.run_all()
    return records

def load_data(uploaded_file):
    records = pd.read_csv(uploaded_file)
    column_map = {
    "date": ["date", "transaction date", "timestamp"],
    "account": ["account", "account name", "source"],
    "category": ["category", "type", "label", "expense category"],
    "income/expense": ["income/expense", "direction", "flow", "type"],
    "amount": ["amount", "value", "total", "transaction amount"]
    }
    
    norm_cols = [c.lower().strip() for c in records.columns]
    mapped={}
    for target_col, options in column_map.items():
        for col in norm_cols:
            if col in options:
                mapped[target_col] = records.columns[norm_cols.index(col)]
                break
    if set(mapped.keys()) != set(column_map.keys()):
            missing = set(column_map.keys()) - set(mapped.keys())
            st.error(f"Missing expected column(s): {', '.join(missing)}")
            st.stop()
    records = records.rename(columns=mapped)

        
    records["date"] = pd.to_datetime(records["date"], errors="coerce")
    records["category"] = records["category"].str.strip().str.title()
    records["income/expense"] = records["income/expense"].str.lower()

    st.success("File processed successfully!")
    st.dataframe(records.head())
    analysis = full_analysis(records)
    analysis.run_all()
    return records