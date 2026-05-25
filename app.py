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
    # Pincode file load
    pin_df = pd.read_csv("pincode.csv")
    pin_df.columns = pin_df.columns.str.strip()
    return df, pin_df

df, pin_df = load_data()

# 4. UI
st.markdown("<h1 class='title'>Lohana Clic</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='search-section'>", unsafe_allow_html=True)
    search_input = st.text_input("📍 Enter Pincode or City Name")
    search_btn = st.button("Search Business")
    st.markdown("</div>", unsafe_allow_html=True)

# 5. Search Logic
if search_btn and search_input:
    location_filter = None
    
    # Check if input is Pincode (Digit)
    if search_input.isdigit():
        pincode_val = int(search_input)
        match = pin_df[pin_df['pincode'] == pincode_val]
        if not match.empty:
            location_filter = match.iloc[0]['district'].upper()
            st.success(f"Searching in: {location_filter} (from Pincode)")
        else:
            st.error("Invalid Pincode!")
    else:
        location_filter = search_input.upper()
    
    if location_filter:
        # Filter data.csv based on the city/district
        filtered = df[df['City'].str.upper().str.contains(location_filter, na=False)]
        
        if not filtered.empty:
            st.write(f"### {len(filtered)} results found for {location_filter}")
            for _, row in filtered.iterrows():
                with st.container(border=True):
                    st.write(f"### {row['Sub Category']}")
                    st.write(f"**City:** {row['City']}")
        else:
            st.info("No business found for this location.")
