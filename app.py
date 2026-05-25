import streamlit as st
import pandas as pd
from datetime import datetime

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. કસ્ટમ CSS
st.markdown("""
    <style>
    .birthday-box { background-color: #fff3e0; padding: 15px; border-radius: 10px; border-left: 5px solid #ff8200; margin-bottom: 20px; }
    .stButton>button { background-color: #002d72; color: white; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        return df
    except:
        return None

df = load_data()

# ૪. લોગો
st.image("logo.png", width=200)

# ૫. જન્મદિવસ સ્ટ્રીપ (ઓટોમેટિક)
if df is not None and 'BirthDate' in df.columns:
    today = datetime.now().strftime("%d-%m")
    birthday_people = df[df['BirthDate'] == today]['Name'].tolist()
    if birthday_people:
        st.markdown(f'<div class="birthday-box">🎂 **આજે જન્મદિવસ:** {", ".join(birthday_people)} ને જન્મદિવસની ખૂબ ખૂબ શુભેચ્છાઓ!</div>', unsafe_allow_html=True)

# ૬. સર્ચ સિસ્ટમ
st.subheader("🔍 વ્યવસાય શોધો")
if df is not None:
    c1, c2, c3 = st.columns(3)
    with c1: main_cat = st.selectbox("મેઈન કેટેગરી", ["બધા"] + df['Main_Category'].unique().tolist())
    with c2: sub_cat = st.selectbox("સબ-કેટેગરી", ["બધા"] + df['Sub_Category'].unique().tolist())
    with c3: city = st.selectbox("શહેર", ["બધા"] + df['City'].unique().tolist())

    if st.button("સર્ચ કરો"):
        st.info("સર્ચ રિઝલ્ટ અહીં જોવા મળશે...")

# ૭. રજીસ્ટ્રેશન ફોર્મ
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form"):
    col1, col2 = st.columns(2)
    with col1: name = st.text_input("પૂરું નામ")
    with col2: mobile = st.text_input("મોબાઈલ નંબર")
    if st.form_submit_button("માહિતી સબમિટ કરો"):
        st.success("આભાર!")
