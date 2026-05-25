import streamlit as st
import pandas as pd
# Aa library install karvi padshe: pip install india-location
from india_location import get_states, get_districts, get_talukas 

st.set_page_config(page_title="Lohana Clic", layout="wide")

st.image("logo.png", width=200)
st.subheader("🔍 Vyavasay Shodho")

# Automatic States
state = st.selectbox("Select State", get_states())

# Automatic Districts based on State
district = st.selectbox("Select District", get_districts(state))

# Automatic Talukas based on District
taluka = st.selectbox("Select Taluka", get_talukas(district))

# Baaki nu search logic...
if st.button("Search"):
    st.write("Searching in: " + taluka)
