import streamlit as st

# પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# કસ્ટમ CSS (બટન અને ડિઝાઇન માટે)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #002d72;
        color: white;
        border-radius: 10px;
        width: 100%;
        height: 50px;
    }
    .orange-button>button {
        background-color: #ff8200 !important;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# હેડર: મોટો લોગો
col1, col2 = st.columns([1, 10])
with col1:
    st.image("logo.png", width=200) # અહીં સાઈઝ મોટી કરી છે
with col2:
    st.title("🚩 લોહાણા ક્લિક")

# સર્ચ બાર
st.text_input("", placeholder="🔍 પ્રોડક્ટ્સ અને સર્વિસ શોધો...")

# કેટેગરી ગ્રીડ
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]
cols = st.columns(4)

for i, cat in enumerate(categories):
    with cols[i % 4]:
        st.button(cat)

# રજીસ્ટ્રેશન બટન
st.markdown('<div class="orange-button">', unsafe_allow_html=True)
st.button("+ નવું સભ્ય રજીસ્ટ્રેશન")
st.markdown('</div>', unsafe_allow_html=True)
