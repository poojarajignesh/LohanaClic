import streamlit as st
import pandas as pd
from streamlit_geolocation import streamlit_geolocation

# 1. Page Setup
st.set_page_config(page_title="Lohana Clic", layout="wide", initial_sidebar_state="collapsed")

# 2. Styling (Latest Professional Fonts)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    .main-title { text-align: center; font-size: 45px; color: #1a1a1a; font-weight: 700; margin-bottom: 20px; }
    .search-box { background: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #ff5722; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. Data Loading
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df['Main Category'] = df['Main Category'].ffill()
    df['City'] = df['City'].fillna('Ahmedabad')
    return df

df = load_data()

# 4. Auto-detect Location
st.markdown("<div class='main-title'>Lohana Clic</div>", unsafe_allow_html=True)

# Location Detection Trigger
location = streamlit_geolocation()
current_city = "Ahmedabad" # Default
if location['latitude']:
    # Amne location male etle logic mukvu (Currently using placeholder)
    current_city = "Ahmedabad" 

# 5. Search Bar
with st.container():
    st.markdown("<div class='search-box'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    city = c1.selectbox("📍 Location", ["Select"] + sorted(df['City'].unique().tolist()), index=0)
    main_cat = c2.selectbox("📂 Category", ["Select"] + df['Main Category'].unique().tolist())
    
    sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist() if main_cat != "Select" else []
    sub_cat = c3.selectbox("🔍 Sub-Category", ["Select"] + sub_cats)
    
    search_btn = st.button("🔍 Search")
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Results
if search_btn:
    if main_cat == "Select" or sub_cat == "Select":
        st.warning("Please select Category and Sub-Category.")
    else:
        filtered = df[(df['Main Category'] == main_cat) & (df['Sub Category'] == sub_cat)]
        if city != "Select":
            filtered = filtered[filtered['City'] == city]
        
        if not filtered.empty:
            st.write(f"### {len(filtered)} results found:")
            for _, row in filtered.iterrows():
                with st.container(border=True):
                    st.subheader(row['Sub Category'])
                    st.write(f"**City:** {row['City']}")
        else:
            st.info("No business found for this filter.")
