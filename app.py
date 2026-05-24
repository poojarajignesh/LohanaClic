import streamlit as st
import pandas as pd

# તમારી CSV લિંક
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR0PbPYpqGEfCH3hpyN95F5Mv7UGOYnaokIpqphhO7RCesuqXjDjW8B6h3PjqTRPqQXI5qi8O6gRWlN/pub?gid=0&single=true&output=csv"

st.title("🚩 લોહાણા સમાજ ડિરેક્ટરી")

@st.cache_data
def load_data():
    return pd.read_csv(SHEET_URL)

try:
    df = load_data()
    # કોલમના નામમાં કોઈ વધારાની જગ્યા (Space) ન હોય તે તપાસો
    df.columns = df.columns.str.strip()
    
    user_family_code = st.text_input("તમારો ફેમિલી કોડ દાખલ કરો:")
    
    if user_family_code:
        # ફેમિલી કોડ વડે ફિલ્ટર કરો
        filtered_df = df[df['Family_Code'].astype(str) == user_family_code]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.warning("આ ફેમિલી કોડ સાથે કોઈ સભ્ય મળ્યા નથી.")
            
except Exception as e:
    st.error(f"માહિતી લોડ કરવામાં સમસ્યા છે: {e}")
