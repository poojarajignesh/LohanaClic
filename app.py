import streamlit as st
import pandas as pd

# 1. Page Setup
st.set_page_config(page_title="Lohana Clic", layout="wide")

# 2. Data Loading
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

# 3. Simple Location Dictionary (India na mukhya districts)
# Tame aa ma vadhare add kari shako
locations = {
    "Gujarat": {
        "Ahmedabad": ["Ahmedabad City", "Sanand", "Dholka"],
        "Rajkot": ["Rajkot City", "Gondal", "Jetpur"],
        "Surat": ["Surat City", "Olpad", "Bardoli"]
    },
    "Maharashtra": {
        "Mumbai": ["Mumbai City", "Mumbai Suburban"],
        "Pune": ["Pune City", "Haveli"]
    }
}

st.image("logo.png", width=200)
st.subheader("🔍 Vyavasay Shodho")

if df is not None:
    # Location Selection
    l1, l2, l3 = st.columns(3)
    state = l1.selectbox("State", ["Select"] + list(locations.keys()))
    
    dist_list = ["Select"]
    if state != "Select": dist_list = list(locations[state].keys())
    district = l2.selectbox("District", dist_list)
    
    tal_list = ["Select"]
    if district != "Select": tal_list = locations[state][district]
    taluka = l3.selectbox("Taluka", tal_list)
    
    # Category Selection
    c1, c2 = st.columns(2)
    main_cat = c1.selectbox("Category", ["Select"] + df['Main Category'].dropna().unique().tolist())
    sub_cat = c2.selectbox("Sub Category", ["Select"] + df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist() if main_cat != "Select" else [])

    if st.button("Search"):
        st.write("Results for: " + taluka)
        # Search logic...
else:
    st.error("Data file mali nathi!")
