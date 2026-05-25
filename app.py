import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ
@st.cache_data
def load_data():
    try:
        # તમારી ફાઈલનું નામ એક્ઝેટલી અહીં 'data.csv' છે
        df = pd.read_csv("data.csv")
        # બધી કોલમ્સના નામમાંથી આગળ-પાછળની સ્પેસ કાઢી નાખો
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        return None

df = load_data()

# ૩. હેડર
col1, col2 = st.columns([1, 10])
with col1: st.image("logo.png", width=200)

st.subheader("🔍 વ્યવસાય શોધો")

if df is not None:
    # ઉપલબ્ધ કોલમ્સ ચેક કરો
    cols_in_file = df.columns.tolist()
    
    # ખાતરી કરો કે જરૂરી કોલમ્સ અસ્તિત્વમાં છે
    if 'Main_Category' in cols_in_file and 'Sub_Category' in cols_in_file and 'City' in cols_in_file:
        c1, c2, c3 = st.columns(3)
        
        main_cat = c1.selectbox("મેઈન કેટેગરી", ["બધા"] + df['Main_Category'].dropna().unique().tolist())
        
        sub_options = ["બધા"]
        if main_cat != "બધા":
            sub_options += df[df['Main_Category'] == main_cat]['Sub_Category'].dropna().unique().tolist()
        else:
            sub_options += df['Sub_Category'].dropna().unique().tolist()
        
        sub_cat = c2.selectbox("સબ-કેટેગરી", sub_options)
        city = c3.selectbox("શહેર", ["બધા"] + df['City'].dropna().unique().tolist())

        if st.button("સર્ચ કરો"):
            filtered_df = df.copy()
            if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
            if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
            if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
            
            st.dataframe(filtered_df, use_container_width=True)
    else:
        st.error(f"એરર: તમારી CSV ફાઈલમાં આ કોલમ્સ નથી મળી. હાલમાં ફાઈલમાં આટલી કોલમ છે: {cols_in_file}")
else:
    st.error("ડેટા ફાઈલ 'data.csv' મળી નથી!")

# ૪. રજીસ્ટ્રેશન ફોર્મ
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form"):
    col1, col2 = st.columns(2)
    name = col1.text_input("પૂરું નામ")
    if st.form_submit_button("સબમિટ"):
        st.success("આભાર!")
