import streamlit as st
import pandas as pd

# 1. Page Setup
st.set_page_config(page_title="Lohana Clic", layout="wide", initial_sidebar_state="collapsed")

# 2. Modern Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    .title { text-align: center; font-size: 3rem; font-weight: 700; color: #1a1a1a; margin-top: -50px; }
    .search-section { background: #f8f9fa; padding: 40px; border-radius: 20px; border: 1px solid #e9ecef; }
    .stButton>button { width: 100%; background-color: #ff5722; color: white; font-weight: 600; border-radius: 8px; }
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

# 4. Main UI
st.markdown("<h1 class='title'>Lohana Clic</h1>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='search-section'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    # Location (City) selection
    city = c1.selectbox("📍 Select Location", ["Select"] + sorted(df['City'].unique().tolist()))
    
    # Category selection
    main_cat = c2.selectbox("📂 Select Category", ["Select"] + df['Main Category'].unique().tolist())
    
    # Sub-Category selection
    sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist() if main_cat != "Select" else []
    sub_cat = c3.selectbox("🔍 Select Sub-Category", ["Select"] + sub_cats)
    
    search_btn = st.button("Search Business")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Results Section
if search_btn:
    if main_cat == "Select" or sub_cat == "Select":
        st.warning("Please select both Category and Sub-Category to search.")
    else:
        filtered = df[(df['Main Category'] == main_cat) & (df['Sub Category'] == sub_cat)]
        if city != "Select":
            filtered = filtered[filtered['City'] == city]
        
        if not filtered.empty:
            st.write(f"### {len(filtered)} results found")
            for _, row in filtered.iterrows():
                with st.container(border=True):
                    st.write(f"### {row['Sub Category']}")
                    st.write(f"**City:** {row['City']}")
        else:
            st.info("No business found. Please try different filters.")
