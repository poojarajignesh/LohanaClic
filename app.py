import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ
@st.cache_data
def load_data():
    try:
        # મેઈન ડેટા
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        df['Main Category'] = df['Main Category'].ffill()
        
        # લોકેશન ડેટા (તમારી નવી ફાઈલ)
        loc_df = pd.read_csv("location_data.csv")
        loc_df.columns = loc_df.columns.str.strip()
        
        return df, loc_df
    except Exception as e:
        st.error(f"Error loading files: {e}")
        return None, None

df, loc_df = load_data()

# ૩. UI
st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None and loc_df is not None:
    # --- કેટેગરી ફિલ્ટર ---
    c1, c2 = st.columns(2)
    main_options = ["Select"] + df['Main Category'].dropna().unique().tolist()
    main_cat = c1.selectbox("Main Category", main_options)
    
    sub_cats = []
    if main_cat != "Select":
        sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
    sub_cat = c2.selectbox("Sub Category", ["Select"] + sub_cats)

    # --- લોકેશન ફિલ્ટર (State -> District -> Taluka) ---
    st.divider()
    st.subheader("📍 લોકેશન પસંદ કરો")
    l1, l2, l3 = st.columns(3)
    
    # State
    states = ["Select"] + loc_df['State'].dropna().unique().tolist()
    state = l1.selectbox("રાજ્ય", states)
    
    # District
    districts = ["Select"]
    if state != "Select":
        districts += loc_df[loc_df['State'] == state]['District'].dropna().unique().tolist()
    district = l2.selectbox("જિલ્લો", districts)
    
    # Taluka
    talukas = ["Select"]
    if district != "Select":
        talukas += loc_df[(loc_df['State'] == state) & (loc_df['District'] == district)]['Taluka'].dropna().unique().tolist()
    taluka = l3.selectbox("તાલુકો", talukas)

    # --- સર્ચ બટન ---
    if st.button("સર્ચ કરો"):
        if main_cat == "Select" or sub_cat == "Select":
            st.warning("કૃપા કરીને કેટેગરી સિલેક્ટ કરો.")
        else:
            filtered_df = df.copy()
            filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
            filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]
            
            # જો લોકેશન પસંદ કર્યું હોય તો તેને ફિલ્ટર કરો
            if taluka != "Select":
                filtered_df = filtered_df[filtered_df['City'] == taluka] # ધારી લો કે City column માં તાલુકાનું નામ છે
            
            if not filtered_df.empty:
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.info("આ લોકેશન પર કોઈ ડેટા મળ્યો નથી.")
else:
    st.error("ફાઈલો મળી નથી! કૃપા કરીને data.csv અને location_data.csv ફાઈલ ચેક કરો.")

# ૪. રજીસ્ટ્રેશન
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    name = col1.text_input("પૂરું નામ")
    mobile = col2.text_input("મોબાઈલ નંબર")
    if st.form_submit_button("સબમિટ"):
        st.success("આભાર!")
