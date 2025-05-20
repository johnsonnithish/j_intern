import streamlit as st
from data_loader import load_data, sample_data
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
            records = load_data(uploaded_file)
            st.session_state.show_uploader = False
            st.success("File uploaded successfully!")

if mode == "manual":
     st.write("Enter your data manually")

if mode == "sample":
     st.write("Using sample data")
     sample_data()