import pandas as pd
from analysis import full_analysis
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
    records = pd.read_csv(
        uploaded_file,
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