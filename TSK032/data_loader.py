import pandas as pd

def load_data():
    records = pd.read_csv(
        "expense_data_1.csv",
        usecols=["Date", "Account", "Category", "Income/Expense", "Amount"],
        converters={"Date": pd.to_datetime},
        dtype={
            "Income/Expense": "category",
            "Category": "category"
        }
    )
    return records
