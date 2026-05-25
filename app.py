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
        # ખાલી રો (rows) કાઢી નાખો
        df = df.dropna(how='all')
        return df
    except:
        return None

df = load_data()

# ૩. હેડર
st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None and not df.empty:
    # જરૂરી કોલમ્સ ચેક કરવી
    if 'Main_Category' in df.columns and 'Sub_Category' in df.columns:
        c1, c2, c3 = st.columns(3)
        
        main_options = ["બધા"] + df['Main_Category'].dropna().unique().tolist()
        main_cat = c1.selectbox("મેઈન કેટેગરી", main_options)
        
        # સબ-કેટેગરી લોજિક
        if main_cat != "બધા":
            sub_options = ["બધા"] + df[df['Main_Category'] == main_cat]['Sub_Category'].dropna().unique().tolist()
        else:
            sub_options = ["બધા"] + df['Sub_Category'].dropna().unique().tolist()
        
        sub_cat = c2.selectbox("સબ-કેટેગરી", sub_options)
        
        city_options = ["બધા"] + df['City'].dropna().unique().tolist() if 'City' in df.columns else ["બધા"]
        city = c3.selectbox("શહેર", city_options)

        if st.button("સર્ચ કરો"):
            filtered_df = df.copy()
            if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
            if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
            if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
            
            if not filtered_df.empty:
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.warning("કોઈ રિઝલ્ટ મળ્યું નથી.")
    else:
        st.error("CSV ફાઈલમાં હેડર્સ (Main_Category, Sub_Category, City) નથી.")
else:
    st.error("ડેટા ફાઈલ ખાલી છે અથવા મળી નથી. કૃપા કરીને data.csv માં ડેટા ઉમેરો.")

# ૪. રજીસ્ટ્રેશન
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form", clear_on_submit=True):
    name = st.text_input("પૂરું નામ")
    if st.form_submit_button("સબમિટ"):
        st.success("આભાર!")
