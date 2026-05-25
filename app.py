import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. કસ્ટમ CSS (ડિઝાઈન અને કલર માટે)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #002d72;
        color: white;
        border-radius: 10px;
        width: 100%;
        height: 50px;
        font-weight: bold;
    }
    .orange-button>button {
        background-color: #ff8200 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ (ફાઈલનું નામ data.csv રાખજો)
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip() # સ્પેસ કાઢવા માટે
        return df
    except:
        return None

df = load_data()

# ૪. હેડર: લોગો
col1, col2 = st.columns([1, 10])
with col1:
    try:
        st.image("logo.png", width=200)
    except:
        st.write("Logo Missing")

# ૫. સર્ચ સિસ્ટમ
st.subheader("🔍 વ્યવસાય શોધો")
if df is not None:
    c1, c2, c3 = st.columns(3)
    
    with c1:
        main_cat = st.selectbox("મેઈન કેટેગરી", ["બધા"] + df['Main_Category'].unique().tolist())
    with c2:
        if main_cat != "બધા":
            sub_options = ["બધા"] + df[df['Main_Category'] == main_cat]['Sub_Category'].unique().tolist()
        else:
            sub_options = ["બધા"] + df['Sub_Category'].unique().tolist()
        sub_cat = st.selectbox("સબ-કેટેગરી", sub_options)
    with c3:
        city = st.selectbox("શહેર", ["બધા"] + df['City'].unique().tolist())

    if st.button("સર્ચ કરો"):
        filtered_df = df.copy()
        if main_cat != "બધા": filtered_df = filtered_df[filtered_df['Main_Category'] == main_cat]
        if sub_cat != "બધા": filtered_df = filtered_df[filtered_df['Sub_Category'] == sub_cat]
        if city != "બધા": filtered_df = filtered_df[filtered_df['City'] == city]
        
        st.dataframe(filtered_df)
else:
    st.error("ડેટા ફાઈલ (data.csv) મળી નથી! GitHub માં ફાઈલનું નામ ચેક કરો.")

# ૬. કેટેગરી ગ્રીડ
st.divider()
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]
cols = st.columns(4)
for i, cat in enumerate(categories):
    with cols[i % 4]:
        st.button(cat)

# ૭. રજીસ્ટ્રેશન ફોર્મ
st.divider()
st.markdown('<div class="orange-button">', unsafe_allow_html=True)
st.button("+ નવું સભ્ય રજીસ્ટ્રેશન")
st.markdown('</div>', unsafe_allow_html=True)

with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("પૂરું નામ")
        father_name = st.text_input("પિતાનું નામ")
    with col2:
        blood_group = st.selectbox("બ્લડ ગ્રુપ", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        mobile = st.text_input("મોબાઈલ નંબર")
    
    if st.form_submit_button("માહિતી સબમિટ કરો"):
        st.success(f"આભાર {full_name}, તમારી વિગત નોંધાઈ ગઈ છે!")
