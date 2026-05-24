import streamlit as st
import pandas as pd

# તમારી CSV લિંક
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR0PbPYpqGEfCH3hpyN95F5Mv7UGOYnaokIpqphhO7RCesuqXjDjW8B6h3PjqTRPqQXI5qi8O6gRWlN/pub?gid=0&single=true&output=csv"

st.title("🚩 લોહાણા સમાજ ડિરેક્ટરી")
import streamlit as st
import pandas as pd

# ડેટા લોડ કરવાનું ફંક્શન
@st.cache_data
def load_data():
    return pd.read_csv("તમારી_CSV_લિંક")

df = load_data()

st.title("🚩 લોહાણા સમાજ ડિરેક્ટરી")

# લોગ-ઈન બોક્સ
user_family_code = st.text_input("તમારો ફેમિલી કોડ/મોબાઈલ નંબર દાખલ કરો:")

if user_family_code:
    # હવે અહીં એ કોડ આવશે જે તમે પૂછ્યો હતો
    filtered_df = df[df['Family_Code'].astype(str) == user_family_code]
    
    if not filtered_df.empty:
        st.success("તમારી ફેમિલીનો ડેટા:")
        st.dataframe(filtered_df)
    else:
        st.error("આ કોડ સાથે કોઈ ડેટા મળ્યો નથી.")

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
