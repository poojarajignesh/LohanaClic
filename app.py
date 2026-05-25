import streamlit as st
import pandas as pd

# સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

st.title("🚩 લોહાણા ક્લિક (Lohana Clic)")

# ડેટા લોડિંગ
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR0PbPYpqGEfCH3hpyN95F5Mv7UGOYnaokIpqphhO7RCesuqXjDjW8B6h3PjqTRPqQXI5qi8O6gRWlN/pub?gid=0&single=true&output=csv"

@st.cache_data
def load_data():
    return pd.read_csv(SHEET_URL)

df = load_data()

# મેનુ
menu = st.sidebar.radio("મેનુ", ["સભ્ય ડિરેક્ટરી", "ડેટાબેંક રજીસ્ટ્રેશન"])

if menu == "સભ્ય ડિરેક્ટરી":
    st.subheader("🔍 ફેમિલી ડિરેક્ટરી")
    f_code = st.text_input("ફેમિલી કોડ નાખો:")
    if f_code:
        result = df[df['Family_Code'].astype(str) == f_code]
        st.dataframe(result)

elif menu == "ડેટાબેંક રજીસ્ટ્રેશન":
    st.subheader("📋 લોહાણા પરિવાર ડેટાબેંક ફોર્મ")
    with st.form("databank_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("નામ")
            father_name = st.text_input("પિતાનું નામ")
            dob = st.date_input("જન્મ તારીખ")
        with col2:
            blood = st.selectbox("બ્લડ ગ્રુપ", ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])
            city = st.text_input("ગામ/શહેર")
            family_code = st.text_input("ફેમિલી આઈડી")
        
        submit = st.form_submit_button("માહિતી સબમિટ કરો")
        if submit:
            st.success("આભાર! તમારી વિગત નોંધાઈ ગઈ છે.")
