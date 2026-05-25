import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ (સૌથી મહત્વનું સ્ટેપ)
@st.cache_data
def load_data():
    try:
        # તમારી ફાઈલનું નામ એક્ઝેટ અહીં લખ્યું છે
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        # અહીં એરર દેખાશે જેથી તમને ખબર પડે કે શું પ્રોબ્લેમ છે
        return None

df = load_data()

# ૪. હેડર અને લોગો
col1, col2 = st.columns([1, 10])
with col1:
    try:
        st.image("logo.png", width=200)
    except:
        st.write("Logo Missing")

# ૫. મુખ્ય લોજિક (જો ડેટા મળે તો જ આગળ વધો)
if df is not None:
    st.subheader("🔍 વ્યવસાય શોધો")
    
    # કોલમ બનાવતી વખતે સાવધાની
    c1, c2, c3 = st.columns(3)
    
    # ડ્રોપડાઉન બનાવવા માટે યુનિક લિસ્ટ (કોલમનું નામ સાચું છે તેની ખાતરી કરો)
    if 'Main_Category' in df.columns:
        main_options = ["બધા"] + df['Main_Category'].dropna().unique().tolist()
        main_cat = c1.selectbox("મેઈન કેટેગરી", main_options)
        
        # સબ-કેટેગરી ફિલ્ટર
        if main_cat != "બધા":
            sub_options = ["બધા"] + df[df['Main_Category'] == main_cat]['Sub_Category'].dropna().unique().tolist()
        else:
            sub_options = ["બધા"] + df['Sub_Category'].dropna().unique().tolist()
        sub_cat = c2.selectbox("સબ-કેટેગરી", sub_options)
        
        # શહેર ફિલ્ટર
        city_options = ["બધા"] + df['City'].dropna().unique().tolist()
        city = c3.selectbox("શહેર", city_options)

        if st.button("સર્ચ કરો"):
            filtered_df = df.copy()
            if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
            if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
            if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
            
            st.dataframe(filtered_df)
    else:
        st.error("તમારી CSV ફાઈલમાં 'Main_Category' કોલમ નથી! કૃપા કરીને ફાઈલ ચેક કરો.")
else:
    st.error("ડેટા ફાઈલ (data.csv) મળી નથી. કૃપા કરીને GitHub રિપોઝિટરીમાં ફાઈલ અપલોડ થયેલી છે કે નહીં તે તપાસો.")
