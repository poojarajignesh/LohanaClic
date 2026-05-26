import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Lohana Clic - Justdial Style", layout="wide")

# 2. Styling (Justdial Look)
st.markdown("""
    <style>
    .header { background-color: #ff8200; padding: 20px; color: white; text-align: center; border-radius: 10px; }
    .search-box { background: #fdfdfd; padding: 25px; border: 2px solid #ff8200; border-radius: 15px; margin: 20px 0; }
    .business-card { padding: 15px; border-bottom: 1px solid #eee; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 3. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# 4. Header & Logo
st.image("logo.png", width=150)
st.markdown("<h1 class='header'>Find Local Businesses</h1>", unsafe_allow_html=True)

# 5. Search Interface (The "Justdial" Box)
with st.container():
    st.markdown("<div class='search-box'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    # Selection
    main_cat = c1.selectbox("Main Category", ["Select"] + sorted(df['Main Category'].unique().tolist()))
    
    # Filtered Sub-Category
    sub_cats = sorted(df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist()) if main_cat != "Select" else []
    sub_cat = c2.selectbox("Sub Category", ["Select"] + sub_cats)
    
    city = c3.text_input("Enter City/Pincode")
    
    search_btn = st.button("Search Now")
    st.markdown("</div>", unsafe_allow_html=True)

# 6. Results Logic
if search_btn:
    if main_cat == "Select" or sub_cat == "Select":
        st.error("Please select Category and Sub-category!")
    else:
        filtered = df[(df['Main Category'] == main_cat) & (df['Sub Category'] == sub_cat)]
        if city:
            filtered = filtered[filtered['City'].str.contains(city, case=False, na=False)]
        
        if not filtered.empty:
            for _, row in filtered.iterrows():
                st.markdown(f"<div class='business-card'><h3>{row['Sub Category']}</h3><p>City: {row['City']}</p></div>", unsafe_allow_html=True)
        else:
            st.warning("No results found.")
