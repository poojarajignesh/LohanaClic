import streamlit as st
import pandas as pd

# ૧. Page Setup
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. Custom CSS for Look & Feel
st.markdown("""
    <style>
    .stButton>button { background-color: #002d72; color: white; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; }
    .orange-button>button { background-color: #ff8200 !important; color: white !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ૩. Data Loading
@st.cache_data
def load_data():
    try:
        return pd.read_csv("Business Categories.xlsx - Sheet1.csv")
    except:
        return pd.DataFrame(columns=['Main_Category', 'Sub_Category', 'City'])

df = load_data()

# ૪. Header with Logo
col1, col2 = st.columns([1, 10])
with col1:
    st.image("logo.png", width=200)

# ૫. Search System
st.subheader("🔍 વ્યવસાય શોધો")
c1, c2, c3 = st.columns(3)

with c1:
    main_cat = st.selectbox("મેઈન કેટેગરી", ["બધા"] + df['Main_Category'].unique().tolist())
with c2:
    if main_cat != "બધા":
        sub_cats = df[df['Main_Category'] == main_cat]['Sub_Category'].unique().tolist()
    else:
        sub_cats = df['Sub_Category'].unique().tolist()
    sub_cat = st.selectbox("સબ-કેટેગરી", ["બધા"] + sub_cats)
with c3:
    city = st.selectbox("શહેર", ["બધા"] + df['City'].unique().tolist())

if st.button("સર્ચ કરો"):
    filtered_df = df
    if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
    if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
    if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
    
    if not filtered_df.empty:
        st.dataframe(filtered_df)
    else:
        st.warning("કોઈ રિઝલ્ટ મળ્યું નથી.")

# ૬. Category Icons
st.divider()
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]
cols = st.columns(4)
for i, cat in enumerate(categories):
    with cols[i % 4]:
        st.button(cat)

# ૭. Registration Section
st.divider()
st.markdown('<div class="orange-button">', unsafe_allow_html=True)
st.button("+ નવું સભ્ય રજીસ્ટ્રેશન")
st.markdown('</div>', unsafe_allow_html=True)

with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("પૂરું નામ")
        father_name = st.text_input("પિતાનું નામ")
    with col2:
        blood_group = st.selectbox("બ્લડ ગ્રુપ", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        mobile = st.text_input("મોબાઈલ નંબર")
    
    if st.form_submit_button("માહિતી સબમિટ કરો"):
        st.success(f"આભાર {full_name}, તમારી વિગત નોંધાઈ ગઈ છે!")
