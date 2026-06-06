import streamlit as st
import pandas as pd

df = pd.read_csv(
    "Telco-Customer-Churn.csv"
)

customer_id = st.text_input(
    "Customer ID"
)

if customer_id:
    result = df[
        df["customerID"] == customer_id
    ]

    st.dataframe(result)