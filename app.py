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
        return df
    except:
        return None

df = load_data()

# ૩. UI
st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None:
    c1, c2, c3 = st.columns(3)
    
    # "બધા" કાઢી નાખ્યું છે
    main_options = df['Main Category'].dropna().unique().tolist()
    main_cat = c1.selectbox("Main Category", main_options)
    
    sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("Sub Category", sub_cats)
    
    cities = df['City'].dropna().unique().tolist()
    city = c3.selectbox("City", [c for c in cities if pd.notna(c)])

    if st.button("Search"):
        filtered_df = df.copy()
        filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
        filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]
        filtered_df = filtered_df[filtered_df['City'] == city]
        
        st.dataframe(filtered_df, use_container_width=True)
else:
    st.error("Data file mali nathi!")
