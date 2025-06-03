import streamlit as st
from data_loader import load_data, sample_data
import pandas as pd
from datetime import date
from analysis import full_analysis

st.set_page_config(page_title="Financial Recommender", page_icon=":moneybag:", layout="wide")

st.title("Financial Recommender")
st.divider()
st.write("CHOOSE FORM OF INPUT")

uploaded_file = None  
    

col_spacer1, col1, col2, col3, col_spacer2 = st.columns([5, 2, 3, 5, 2])

with col1:
    if st.button("Upload CSV", key="upload_csv"):
        st.session_state.input_type = "upload"

with col2:
    if st.button("Enter Data Manually", key="enter_data"):
        st.session_state.input_type = "manual"

with col3:
    if st.button("Use Sample Data", key="use_sample_data"):
        st.session_state.input_type = "sample"


mode = st.session_state.get("input_type", "")
if mode == "upload":
        uploaded_file = st.file_uploader("Upload your CSV", type=["csv"])
        st.caption("Make sure your CSV has the following columns: Date, Category, Income/Expense, Amount")
        if uploaded_file:
            st.success("File uploaded successfully!")
            records = load_data(uploaded_file)
            st.session_state.show_uploader = False
            

if mode == "manual":
     
    st.subheader("Create Your Own Dataset")
    n_rows = 5  
    default_data = pd.DataFrame({
        "S_no": list(range(1, n_rows + 1)),
        "Date": [date.today()] * n_rows,
        "Category": ["" for _ in range(n_rows)],
        "Income/Expense": ["Expense"] * n_rows,
        "Amount": [0.0] * n_rows,
    })

    
    edited = st.data_editor(
        default_data,
        use_container_width=True,
        column_config={
            "Income/Expense": st.column_config.SelectboxColumn(
                "Income/Expense",
                options=["Income", "Expense"],
                required=True,
            ),
            "Amount": st.column_config.NumberColumn(
                "Amount",
                step=0.01,
                min_value=0.0,
                required=True,
            ),
            "Date": st.column_config.DateColumn(
                "Date",
                required=True
            ),
        },
        num_rows="dynamic",  
        key="user_dataset"
    )


    if st.button("Save Table"):
        st.dataframe(edited)
        file_path = "custom_data.csv"
        edited.to_csv(file_path, index=False)
        st.success("Dataset saved!")
        st.header("Running Analysis on Custom Data")
        user_data = pd.read_csv(file_path, parse_dates=["Date"])
        analysis = full_analysis(user_data)
        analysis.run_all()

    


if mode == "sample":
     st.write("Using sample data")
     sample_data()