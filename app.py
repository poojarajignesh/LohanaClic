import streamlit as st
import pandas as pd

# લિંક મૂકતી વખતે ખાતરી કરો કે તે "..." ની વચ્ચે જ હોય
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR0PbPYpqGEfCH3hpyN95F5Mv7UGOYnaokIpqphhO7RCesuqXjDjW8B6h3PjqTRPqQXI5qi8O6gRWlN/pub?gid=0&single=true&output=csv"

st.title("🚩 લોહાણા સમાજ ડિરેક્ટરી")

@st.cache_data
def load_data():
    # અહીં SHEET_URL જ લખવું, કોઈ લખાણ નહીં
    return pd.read_csv(SHEET_URL)

try:
    df = load_data()
    
    # લોગ-ઈન (ફેમિલી કોડ) બોક્સ
    user_family_code = st.text_input("તમારો ફેમિલી કોડ દાખલ કરો:")
    
    if user_family_code:
        # અહીં ખાસ ચેક કરો કે તમારી Google Sheet માં કોલમનું નામ 'Family_Code' છે કે નહીં
        # જો તમારી શીટમાં કોલમનું નામ અલગ હોય તો તે અહીં લખજો
        filtered_df = df[df['Family_Code'].astype(str) == user_family_code]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.error("આ કોડ સાથે ડેટા મળ્યો નથી.")
            
except Exception as e:
    st.error(f"ડેટા લોડ કરવામાં ભૂલ છે: {e}")
