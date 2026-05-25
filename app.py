import streamlit as st
import pandas as pd

# 1. Page Setup
st.set_page_config(page_title="Lohana Clic", layout="wide")

# 2. Data Loading
@st.cache_data
def load_data():
    try:
        # Tmari mukhya data file
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        df['Main Category'] = df['Main Category'].ffill()
        
        # Location file (j tame navi upload kari che)
        # Dhari lo ke file nu naam 'location_data.csv' che
        try:
            loc_df = pd.read_csv("location_data.csv")
            loc_df.columns = loc_df.columns.str.strip()
        except:
            loc_df = None
            
        return df, loc_df
    except:
        return None, None

df, loc_df = load_data()

# 3. UI
st.image("logo.png", width=200)
st.subheader("🔍 Vyavasay Shodho")

if df is not None:
    c1, c2, c3 = st.columns(3)
    
    # Main Category Filter
    main_cat = c1.selectbox("Main Category", ["Badha"] + df['Main Category'].dropna().unique().tolist())
    
    # Sub Category Filter
    sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist() if main_cat != "Badha" else df['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("Sub Category", ["Badha"] + sub_cats)
    
    # City Filter (Faltu values kadva mate .dropna())
    cities = df['City'].dropna().unique().tolist()
    city = c3.selectbox("City", ["Badha"] + [c for c in cities if pd.notna(c)])

    if st.button("Search Karo"):
        filtered_df = df.copy()
        if main_cat != "Badha": filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
        if sub_cat != "Badha": filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]
        if city != "Badha": filtered_df = filtered_df[filtered_df['City'] == city]
        
        st.dataframe(filtered_df, use_container_width=True)
else:
    st.error("Data file mali nathi!")
