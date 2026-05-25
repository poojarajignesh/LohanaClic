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
        # સ્પેસ સાફ કરવા માટે
        df.columns = df.columns.str.strip()
        # Main Category માં જે ખાલી જગ્યાઓ છે તે ભરવા માટે (Forward fill)
        df['Main Category'] = df['Main Category'].ffill()
        return df
    except Exception as e:
        st.error(f"Error: {e}")
        return None

df = load_data()

# ૪. હેડર
st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None:
    c1, c2, c3 = st.columns(3)
    
    # મેઈન કેટેગરી ડ્રોપડાઉન
    main_options = ["બધા"] + df['Main Category'].dropna().unique().tolist()
    main_cat = c1.selectbox("મેઈન કેટેગરી", main_options)
    
    # સબ-કેટેગરી ડ્રોપડાઉન
    if main_cat != "બધા":
        sub_options = ["બધા"] + df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
    else:
        sub_options = ["બધા"] + df['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("સબ-કેટેગરી", sub_options)
    
    # શહેર ડ્રોપડાઉન
    city_options = ["બધા"] + df['City'].dropna().unique().tolist()
    city = c3.selectbox("શહેર", city_options)

    if st.button("સર્ચ કરો"):
        filtered_df = df.copy()
        if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
        if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]
        if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
        
        st.dataframe(filtered_df, use_container_width=True)
else:
    st.error("ડેટા ફાઈલ (data.csv) મળી નથી!")

# ૫. રજીસ્ટ્રેશન ફોર્મ
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    name = col1.text_input("પૂરું નામ")
    mobile = col2.text_input("મોબાઈલ નંબર")
    if st.form_submit_button("માહિતી સબમિટ કરો"):
        st.success(f"આભાર {name}!")
