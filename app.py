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
    # --- લોકેશન ડાયરેક્ટ સિલેક્ટ કરવા માટેનું લોજિક ---
    st.subheader("📍 લોકેશન પસંદ કરો")
    l1, l2, l3 = st.columns(3)
    
    # ડિફોલ્ટ લોકેશન તરીકે અમદાવાદ સેટ કરો
    default_state = "Gujarat"
    default_dist = "Ahmedabad"
    
    # સ્ટેટ
    state = l1.selectbox("રાજ્ય", loc_df['State'].unique().tolist(), index=loc_df['State'].unique().tolist().index(default_state))
    
    # જિલ્લો
    districts = loc_df[loc_df['State'] == state]['District'].unique().tolist()
    district = l2.selectbox("જિલ્લો", districts, index=districts.index(default_dist))
    
    # તાલુકો
    talukas = loc_df[(loc_df['State'] == state) & (loc_df['District'] == district)]['Taluka'].unique().tolist()
    taluka = l3.selectbox("તાલુકો", ["Select"] + talukas)

    # --- કેટેગરી ---
    c1, c2 = st.columns(2)
    main_options = ["Select"] + df['Main Category'].dropna().unique().tolist()
    main_cat = c1.selectbox("Main Category", main_options)
    
    sub_cats = []
    if main_cat != "Select":
        sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("Sub Category", ["Select"] + sub_cats)

    if st.button("સર્ચ કરો"):
        # ફિલ્ટર લોજિક...
        st.success(f"તમે {taluka}, {district} માં સર્ચ કરી રહ્યા છો!")
else:
    st.error("ફાઈલો મળી નથી!")
