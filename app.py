import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. કસ્ટમ CSS (ડિઝાઈન અને કલર માટે)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #002d72;
        color: white;
        border-radius: 10px;
        width: 100%;
        height: 50px;
        font-weight: bold;
    }
    .orange-button>button {
        background-color: #ff8200 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ (કેટેગરી માટે)
@st.cache_data
def load_business_data():
    try:
        return pd.read_csv("Business Categories.xlsx - Sheet1.csv")
    except:
        return pd.DataFrame(columns=['Main_Category', 'Sub_Category', 'City'])

df = load_business_data()

# ૪. હેડર: મોટો લોગો
col1, col2 = st.columns([1, 10])
with col1:
    try:
        st.image("logo.png", width=200)
    except:
        st.write("Logo Missing")

# ૫. સર્ચ સિસ્ટમ (Justdial Style)
st.subheader("સર્ચ અને ફિલ્ટર")
col_s1, col_s2, col_s3 = st.columns(3)

with col_s1:
    main_cat = st.selectbox("મેઈન કેટેગરી", ["બધા"] + df['Main_Category'].unique().tolist())
with col_s2:
    if main_cat != "બધા":
        sub_cats = df[df['Main_Category'] == main_cat]['Sub_Category'].unique().tolist()
    else:
        sub_cats = df['Sub_Category'].unique().tolist()
    sub_cat = st.selectbox("સબ-કેટેગરી", ["બધા"] + sub_cats)
with col_s3:
    city = st.selectbox("શહેર", ["બધા"] + df['City'].unique().tolist())

if st.button("સર્ચ કરો"):
    st.info("સર્ચ રિઝલ્ટ અહીં જોવા મળશે...")

st.divider()

# ૬. કેટેગરી ગ્રીડ
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]
cols = st.columns(4)
for i, cat in enumerate(categories):
    with cols[i % 4]:
        st.button(cat)

# ૭. રજીસ્ટ્રેશન બટન અને ફોર્મ
st.markdown('<div class="orange-button">', unsafe_allow_html=True)
st.button("+ નવું સભ્ય રજીસ્ટ્રેશન")
st.markdown('</div>', unsafe_allow_html=True)

st.subheader("📝 સભ્ય રજીસ્ટ્રેશન વિગત")
with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("પૂરું નામ")
        father_name = st.text_input("પિતાનું નામ")
        dob = st.date_input("જન્મ તારીખ")
    with col2:
        blood_group = st.selectbox("બ્લડ ગ્રુપ", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        city = st.text_input("ગામ / શહેર")
        mobile = st.text_input("મોબાઈલ નંબર")

    occupation = st.text_input("ધંધો / નોકરી / વ્યવસાયનું નામ")
    address = st.text_area("સરનામું")

    if st.form_submit_button("માહિતી સબમિટ કરો"):
        st.success(f"આભાર {full_name}, તમારી વિગત નોંધાઈ ગઈ છે!")
