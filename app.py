import streamlit as st
import pandas as pd

# પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# કસ્ટમ CSS
st.markdown("""
    <style>
    .stButton>button { background-color: #002d72; color: white; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; }
    .orange-button>button { background-color: #ff8200 !important; color: white !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ડેટા લોડિંગ (ફાઈલના નામમાં સ્પેલિંગ ચેક કરી લેજો)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Business Categories.xlsx - Sheet1.csv")
        # કોલમ્સના નામમાં જો કોઈ વધારાની સ્પેસ હોય તો તે કાઢવા માટે
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"ડેટા લોડ કરવામાં ભૂલ: {e}")
        return None

df = load_data()

# હેડર
col1, col2 = st.columns([1, 10])
with col1:
    st.image("logo.png", width=200)

if df is not None:
    # સર્ચ સિસ્ટમ
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
        
        st.dataframe(filtered_df)
else:
    st.warning("કૃપા કરીને CSV ફાઈલ તપાસો.")

# કેટેગરી ગ્રીડ અને રજીસ્ટ્રેશન ફોર્મ બાકીનો ભાગ...
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("પૂરું નામ")
    with col2:
        mobile = st.text_input("મોબાઈલ")
    if st.form_submit_button("સબમિટ"):
        st.success("નોંધાઈ ગયું!")
