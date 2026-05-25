import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df['Main Category'] = df['Main Category'].ffill()
    
    loc_df = pd.read_csv("location_data.csv")
    loc_df.columns = loc_df.columns.str.strip()
    return df, loc_df

df, loc_df = load_data()

st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

# લોકેશન ફિલ્ટર
c1, c2, c3 = st.columns(3)

# 1. State
states = ["Select"] + loc_df['State'].dropna().unique().tolist()
state = c1.selectbox("રાજ્ય", states)

# 2. District
districts = ["Select"]
if state != "Select":
    districts += loc_df[loc_df['State'] == state]['District'].dropna().unique().tolist()
district = c2.selectbox("જિલ્લો", districts)

# 3. Taluka
talukas = ["Select"]
if district != "Select":
    talukas += loc_df[(loc_df['State'] == state) & (loc_df['District'] == district)]['Taluka'].dropna().unique().tolist()
taluka = c3.selectbox("તાલુકો", talukas)

# સર્ચ બટન
if st.button("સર્ચ કરો"):
    if taluka != "Select":
        # અહીં તમારો મેઈન ડેટા ફિલ્ટર થશે
        st.write(f"તમે {taluka} પસંદ કર્યું છે.")
        # તમે અહીં data.csv માંથી ડેટા ફિલ્ટર કરી શકો છો
    else:
        st.warning("કૃપા કરીને તાલુકો પસંદ કરો.")
