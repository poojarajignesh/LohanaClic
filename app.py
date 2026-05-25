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
        
        loc_df = pd.read_csv("location_data.csv")
        loc_df.columns = loc_df.columns.str.strip()
        return df, loc_df
    except:
        return None, None

df, loc_df = load_data()

# ૩. UI
st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None and loc_df is not None:
    st.subheader("📍 લોકેશન પસંદ કરો")
    l1, l2, l3 = st.columns(3)
    
    # સ્ટેટ લિસ્ટ મેળવો
    states = loc_df['State'].unique().tolist()
    
    # ડિફોલ્ટ વેલ્યુ સેટ કરવાનું લોજિક (જો "Gujarat" ન મળે તો પહેલું નામ લેશે)
    default_state = "Gujarat"
    state_idx = states.index(default_state) if default_state in states else 0
    
    state = l1.selectbox("રાજ્ય", states, index=state_idx)
    
    # જિલ્લો
    districts = loc_df[loc_df['State'] == state]['District'].unique().tolist()
    default_dist = "Ahmedabad"
    dist_idx = districts.index(default_dist) if default_dist in districts else 0
    
    district = l2.selectbox("જિલ્લો", districts, index=dist_idx)
    
    # તાલુકો
    talukas = loc_df[(loc_df['State'] == state) & (loc_df['District'] == district)]['Taluka'].unique().tolist()
    taluka = l3.selectbox("તાલુકો", ["Select"] + talukas)

    # --- બાકીનું સર્ચ લોજિક... ---
else:
    st.error("ફાઈલો મળી નથી!")
