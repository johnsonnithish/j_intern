def prepare_aggregates(records):
    by_spend = records.groupby("Income/Expense", observed=True)
    monthly_income = (
        records[records["Income/Expense"] == "Income"]
        .groupby(records["Date"].dt.to_period("M"))["Amount"]
        .sum()
        .rename("Monthly_Income")
    )
    return by_spend, monthly_income

def get_top3_per_month(records, monthly_income):
    monthly_by_cat = records.groupby(
        [records["Date"].dt.to_period("M"), "Category"], observed=True
    )["Amount"].sum().reset_index()

    top3 = (
        monthly_by_cat
        .sort_values(['Date', 'Amount'], ascending=[True, False])
        .groupby('Date')
        .head(3)
        .merge(monthly_income, left_on="Date", right_index=True, how="left")
    )

    top3["Percent"] = (top3["Amount"] / top3["Monthly_Income"] * 100).round(2)
    top3["Date"] = top3["Date"].dt.to_timestamp().dt.strftime("%B %Y")
    return top3[["Date", "Category", "Amount", "Percent"]]

def get_needs_data(records, needs):
    df = (
        records[records["Category"].isin(needs)]
        .groupby([records["Date"].dt.to_period("M"), "Category"], observed=True)["Amount"]
        .sum()
        .reset_index()
    )
    df["Date"] = df["Date"].dt.to_timestamp().dt.strftime("%B %Y")
    return df, df["Amount"].sum()

def get_others_data(records, needs):
    df = (
        records[~records["Category"].isin(needs)]
        .groupby([records["Date"].dt.to_period("M"), "Category"], observed=True)["Amount"]
        .sum()
        .reset_index()
    )
    df["Date"] = df["Date"].dt.to_timestamp().dt.strftime("%B %Y")
    return df, df["Amount"].sum()
