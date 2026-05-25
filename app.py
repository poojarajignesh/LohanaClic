import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ (અહીં સુધારો કર્યો છે)
st.set_page_config(page_title="Lohana Clic", layout="wide", initial_sidebar_state="collapsed")

# ૨. કસ્ટમ CSS
st.markdown("""
    <style>
    .main-title { text-align: center; font-size: 40px; color: #ff8200; font-weight: bold; margin-bottom: 30px; }
    .search-box { background-color: #f0f2f6; padding: 25px; border-radius: 15px; }
    .stButton>button { width: 100%; height: 45px; background-color: #ff8200; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        df['Main Category'] = df['Main Category'].ffill()
        df['City'] = df['City'].fillna('Ahmedabad')
        return df
    except:
        return None

df = load_data()

# ૪. હોમ પેજ લેઆઉટ
st.markdown("<div class='main-title'>Lohana Clic</div>", unsafe_allow_html=True)

if df is not None:
    with st.container():
        st.markdown("<div class='search-box'>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        
        # ડ્રોપડાઉન
        city = c1.selectbox("📍 શહેર", ["Select"] + sorted(df['City'].unique().tolist()))
        main_cat = c2.selectbox("📂 કેટેગરી", ["Select"] + df['Main Category'].unique().tolist())
        
        sub_cats = []
        if main_cat != "Select":
            sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
        sub_cat = c3.selectbox("🔍 સબ-કેટેગરી", ["Select"] + sub_cats)
        
        search_btn = st.button("🔍 સર્ચ કરો")
        st.markdown("</div>", unsafe_allow_html=True)

    # ૫. સર્ચ રિઝલ્ટ
    if search_btn:
        if main_cat == "Select" or sub_cat == "Select":
            st.warning("⚠️ કૃપા કરીને કેટેગરી અને સબ-કેટેગરી પસંદ કરો.")
        else:
            filtered = df[(df['Main Category'] == main_cat) & (df['Sub Category'] == sub_cat)]
            if city != "Select":
                filtered = filtered[filtered['City'] == city]
            
            if not filtered.empty:
                st.write(f"### 📍 {len(filtered)} પરિણામો મળ્યા:")
                for index, row in filtered.iterrows():
                    with st.container(border=True):
                        st.subheader(row['Sub Category'])
                        st.write(f"**શહેર:** {row['City']}")
            else:
                st.info("સૂચના: આ ફિલ્ટર માટે કોઈ બિઝનેસ મળ્યો નથી.")
else:
    st.error("ડેટા ફાઈલ મળી નથી. 'data.csv' ચેક કરો.")
