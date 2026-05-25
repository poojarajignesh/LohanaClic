import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip() # વધારાની સ્પેસ કાઢવા માટે
        return df
    except:
        return None

df = load_data()

# ૩. હેડર
if "logo.png" in locals() or True: # લોગો લોડિંગ
    try:
        st.image("logo.png", width=200)
    except:
        st.write("")

# ૪. મુખ્ય સર્ચ વિભાગ
st.subheader("🔍 વ્યવસાય શોધો")

if df is not None:
    # કોલમ્સ ચેક કરવી
    required_cols = ['Main_Category', 'Sub_Category', 'City']
    if all(col in df.columns for col in required_cols):
        c1, c2, c3 = st.columns(3)
        
        main_cat = c1.selectbox("મેઈન કેટેગરી", ["બધા"] + df['Main_Category'].dropna().unique().tolist())
        
        if main_cat != "બધા":
            sub_options = ["બધા"] + df[df['Main_Category'] == main_cat]['Sub_Category'].dropna().unique().tolist()
        else:
            sub_options = ["બધા"] + df['Sub_Category'].dropna().unique().tolist()
        
        sub_cat = c2.selectbox("સબ-કેટેગરી", sub_options)
        city = c3.selectbox("શહેર", ["બધા"] + df['City'].dropna().unique().tolist())

        if st.button("સર્ચ કરો"):
            filtered_df = df.copy()
            if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
            if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
            if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
            
            st.dataframe(filtered_df, use_container_width=True)
    else:
        st.error(f"તમારી CSV ફાઈલમાં આ કોલમ હોવી જરૂરી છે: {required_cols}")
else:
    st.error("ડેટા ફાઈલ (data.csv) મળી નથી! ફાઈલના નામ અને અપલોડ ચેક કરો.")

# ૫. રજીસ્ટ્રેશન
st.divider()
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન")
with st.form("reg_form", clear_on_submit=True):
    name = st.text_input("પૂરું નામ")
    if st.form_submit_button("સબમિટ"):
        st.success("આભાર!")
