import streamlit as st
import pandas as pd

# તમારી CSV લિંક
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR0PbPYpqGEfCH3hpyN95F5Mv7UGOYnaokIpqphhO7RCesuqXjDjW8B6h3PjqTRPqQXI5qi8O6gRWlN/pub?gid=0&single=true&output=csv"

st.title("🚩 લોહાણા સમાજ ડિરેક્ટરી")

@st.cache_data
def load_data():
    return pd.read_csv(SHEET_URL)

df = load_data()

# સર્ચ બોક્સ
query = st.text_input("સભ્યનું નામ શોધો:")
if query:
    df = df[df['Name'].str.contains(query, case=False)]

# ડેટા ટેબલ
st.dataframe(df)
