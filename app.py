import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. કસ્ટમ CSS
st.markdown("""
    <style>
    .stButton>button { background-color: #002d72; color: white; border-radius: 10px; width: 100%; height: 50px; font-weight: bold; }
    .orange-button>button { background-color: #ff8200 !important; color: white !important; font-weight: bold; }
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

# ૪. હેડર
col1, col2 = st.columns([1, 10])
with col1: st.image("logo.png", width=200)

# ૫. સર્ચ સિસ્ટમ (ફરીથી ગોઠવી છે)
st.subheader("🔍 વ્યવસાય શોધો")
if df is not None:
    c1, c2, c3 = st.columns(3)
    
    main_options = ["બધા"] + df['Main_Category'].unique().tolist()
    main_cat = c1.selectbox("મેઈન કેટેગરી", main_options)
    
    if main_cat != "બધા":
        sub_options = ["બધા"] + df[df['Main_Category'] == main_cat]['Sub_Category'].unique().tolist()
    else:
        sub_options = ["બધા"] + df['Sub_Category'].unique().tolist()
    sub_cat = c2.selectbox("સબ-કેટેગરી", sub_options)
    
    city_options = ["બધા"] + df['City'].unique().tolist()
    city = c3.selectbox("શહેર", city_options)

    if st.button("સર્ચ કરો"):
        filtered_df = df.copy()
        if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
        if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
        if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
        
        st.write(f"### {len(filtered_df)} પરિણામો મળ્યા:")
        st.dataframe(filtered_df, use_container_width=True)
else:
    st.error("ડેટા ફાઈલ (data.csv) મળી નથી!")

# ૬. કેટેગરી ગ્રીડ
st.divider()
cols = st.columns(4)
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]
for i, cat in enumerate(categories):
    with cols[i % 4]: st.button(cat)

# ૭. રજીસ્ટ્રેશન
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    name = col1.text_input("પૂરું નામ")
    mobile = col2.text_input("મોબાઈલ નંબર")
    if st.form_submit_button("માહિતી સબમિટ કરો"):
        st.success(f"આભાર {name}!")
