import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide", initial_sidebar_state="collapsed")

# ૨. સ્ટાઈલિંગ
st.markdown("""
    <style>
    .title { text-align: center; color: #ff8200; font-weight: bold; }
    .search-box { padding: 20px; border-radius: 10px; border: 1px solid #ccc; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    
    st.markdown("<h1 class='title'>Lohana Clic</h1>", unsafe_allow_html=True)

    # ૪. સર્ચ બાર
    search_query = st.text_input("🔍 Type a letter or city name to search:")

    # ૫. ડાયનેમિક ફિલ્ટરિંગ
    if search_query:
        # પિનકોડ હોય તો પિનકોડથી, નહીંતર સિટીના નામથી સર્ચ
        if search_query.isdigit():
            filtered_df = df[df['Pincode'].astype(str).str.contains(search_query, na=False)]
        else:
            filtered_df = df[df['City'].str.contains(search_query, case=False, na=False)]
        
        if not filtered_df.empty:
            st.write(f"### Results for '{search_query}':")
            # રિઝલ્ટ કાર્ડ્સ
            for _, row in filtered_df.iterrows():
                with st.container(border=True):
                    st.subheader(row['Sub Category'])
                    st.write(f"📍 City: {row['City']}")
        else:
            st.info("No results found. Try another spelling.")
    else:
        st.write("Start typing to explore business in your area...")

except FileNotFoundError:
    st.error("Error: 'data.csv' file not found. Please upload it.")
