import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", page_icon="🚩")

# ૨. લોગો અને ટાઇટલ
st.image("logo.png", width=150)
st.title("🚩 લોહાણા ક્લિક (Lohana Clic)")
st.subheader("તમારા સમાજની, તમારી આંગળીએ")

# ૩. ડેટા લોડિંગ
SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR0PbPYpqGEfCH3hpyN95F5Mv7UGOYnaokIpqphhO7RCesuqXjDjW8B6h3PjqTRPqQXI5qi8O6gRWlN/pub?gid=0&single=true&output=csv"

@st.cache_data
def load_data():
    return pd.read_csv(SHEET_URL)

df = load_data()
df.columns = df.columns.str.strip()

# ૪. મુખ્ય ફીચર્સ (Sidebar)
menu = st.sidebar.radio("મેનુ પસંદ કરો", ["સભ્ય ડિરેક્ટરી", "સભ્ય રજીસ્ટ્રેશન"])

if menu == "સભ્ય ડિરેક્ટરી":
    st.subheader("🔍 તમારી ફેમિલીની વિગત શોધો")
    family_code = st.text_input("તમારો ફેમિલી કોડ દાખલ કરો:")
    
    if family_code:
        filtered_df = df[df['Family_Code'].astype(str) == family_code]
        if not filtered_df.empty:
            st.dataframe(filtered_df)
        else:
            st.warning("આ કોડ સાથે કોઈ ડેટા મળ્યો નથી.")

elif menu == "સભ્ય રજીસ્ટ્રેશન":
    st.subheader("📝 નવું સભ્ય રજીસ્ટ્રેશન")
    with st.form("reg_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("પૂરું નામ")
            mobile = st.text_input("મોબાઈલ નંબર")
            dob = st.date_input("જન્મ તારીખ")
        with col2:
            blood_group = st.selectbox("બ્લડ ગ્રુપ", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
            city = st.text_input("શહેર")
            family_code = st.text_input("ફેમિલી આઈડી (કોમન કોડ)")
        
        submit = st.form_submit_button("માહિતી સબમિટ કરો")
        if submit:
            st.success(f"આભાર {name}! તમારી વિગત નોંધાઈ ગઈ છે.")
            # અહીં ડેટા શીટમાં મોકલવા માટેનું લોજિક આવશે (આગળના સ્ટેપમાં કરીશું)
