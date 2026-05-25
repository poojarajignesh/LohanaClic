import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        df['Main Category'] = df['Main Category'].ffill()
        # ખાલી સિટીને 'અન્ય' (Other) તરીકે બતાવીશું
        df['City'] = df['City'].fillna('Other')
        return df
    except:
        return None

df = load_data()

st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None:
    c1, c2, c3 = st.columns(3)
    
    main_options = ["Select"] + df['Main Category'].unique().tolist()
    main_cat = c1.selectbox("Main Category", main_options)
    
    sub_cats = []
    if main_cat != "Select":
        sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("Sub Category", ["Select"] + sub_cats)
    
    # સિટીમાં ડેટા છે કે નહીં તે અહીં ચેક થશે
    city_options = ["Select"] + df['City'].unique().tolist()
    city = c3.selectbox("City", city_options)

    if st.button("Search"):
        if main_cat == "Select" or sub_cat == "Select" or city == "Select":
            st.warning("કૃપા કરીને બધા ઓપ્શન સિલેક્ટ કરો.")
        else:
            filtered_df = df[(df['Main Category'] == main_cat) & 
                             (df['Sub Category'] == sub_cat) & 
                             (df['City'] == city)]
            
            if not filtered_df.empty:
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.info("આ કેટેગરીમાં કોઈ ડેટા મળ્યો નથી.")
else:
    st.error("ડેટા ફાઈલ મળી નથી!")
