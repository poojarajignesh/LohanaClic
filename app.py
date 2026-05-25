import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lohana Clic", layout="wide")

@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        df['Main Category'] = df['Main Category'].ffill()
        loc_df = pd.read_csv("location_data.csv")
        loc_df.columns = loc_df.columns.str.strip()
        return df, loc_df
    except:
        return None, None

df, loc_df = load_data()

st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None and loc_df is not None:
    # ૧. લોકેશન સેક્શન
    st.subheader("📍 લોકેશન પસંદ કરો")
    l1, l2, l3 = st.columns(3)
    
    state = l1.selectbox("રાજ્ય", loc_df['State'].unique().tolist())
    districts = loc_df[loc_df['State'] == state]['District'].unique().tolist()
    district = l2.selectbox("જિલ્લો", districts)
    talukas = loc_df[(loc_df['State'] == state) & (loc_df['District'] == district)]['Taluka'].unique().tolist()
    taluka = l3.selectbox("તાલુકો", talukas)
    
    # ૨. કેટેગરી સેક્શન
    c1, c2 = st.columns(2)
    main_options = df['Main Category'].unique().tolist()
    main_cat = c1.selectbox("Main Category", main_options)
    
    sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("Sub Category", sub_cats)
    
    # ૩. સર્ચ બટન
    if st.button("સર્ચ કરો"):
        filtered_df = df[
            (df['Main Category'] == main_cat) & 
            (df['Sub Category'] == sub_cat)
        ]
        
        if not filtered_df.empty:
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.warning("આ ફિલ્ટર માટે કોઈ ડેટા નથી.")
else:
    st.error("ફાઈલ મળી નથી!")
