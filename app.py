import streamlit as st
import pandas as pd

# પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૧. લોગો અને ટાઇટલ (Justdial સ્ટાઈલ)
col_l, col_r = st.columns([1, 4])
with col_l:
    # જો લોગોમાં એરર આવે તો આ લાઇન કોમેન્ટ કરી દેવી
    try:
        st.image("logo.png", width=120)
    except:
        st.write("🚩")
with col_r:
    st.title("લોહાણા ક્લિક (Lohana Clic)")
    st.markdown("##### Everything in just one click!")

st.divider()

# ૨. સર્ચ બાર (Justdial જેવું)
search_query = st.text_input("🔍 પ્રોડક્ટ્સ અને સર્વિસ શોધો...", placeholder="દા.ત. રેસ્ટોરન્ટ, ડોક્ટર, બિઝનેસ...")

# ૩. કેટેગરી ગ્રીડ (Justdial જેવું સ્ટ્રક્ચર)
st.subheader("કેટેગરી પસંદ કરો")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if st.button("🍽️ રેસ્ટોરન્ટ"): st.write("રેસ્ટોરન્ટ સર્ચ...")
with c2:
    if st.button("🏨 હોટેલ્સ"): st.write("હોટેલ્સ સર્ચ...")
with c3:
    if st.button("💄 બ્યુટી સ્પા"): st.write("બ્યુટી સ્પા સર્ચ...")
with c4:
    if st.button("🎓 એજ્યુકેશન"): st.write("એજ્યુકેશન સર્ચ...")

st.divider()

# ૪. ફોર્મ (ટેબ દ્વારા અલગ પાડ્યું)
tab1, tab2 = st.tabs(["🔍 સર્ચ ડિરેક્ટરી", "📝 નવું રજીસ્ટ્રેશન"])

with tab1:
    st.subheader("ફેમિલી કોડ દ્વારા સર્ચ કરો")
    code = st.text_input("તમારો ફેમિલી કોડ:")
    if code:
        st.info("અહીં તમારી ફેમિલીની વિગત દેખાશે...")

with tab2:
    st.subheader("નવું રજીસ્ટ્રેશન")
    with st.form("reg_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("નામ")
            mobile = st.text_input("મોબાઈલ")
        with col2:
            city = st.text_input("શહેર")
            family_code = st.text_input("ફેમિલી કોડ")
        
        if st.form_submit_button("સબમિટ"):
            st.success("માહિતી નોંધાઈ ગઈ છે!")

# સમજૂતી માટે ડાયાગ્રામ
