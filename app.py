import streamlit as st

# પેજ લેઆઉટ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# કસ્ટમ CSS (રંગો માટે)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #002d72; /* બ્લુ રંગ */
        color: white;
        border-radius: 10px;
    }
    .orange-button>button {
        background-color: #ff8200; /* ઓરેન્જ રંગ */
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# હેડર
col1, col2 = st.columns([1, 10])
with col1:
    st.image("logo.png", width=80)
with col2:
    st.title("🚩 લોહાણા ક્લિક (Lohana Clic)")
    st.caption("તમારા સમાજની, તમારી આંગળીએ")

# સર્ચ બાર
st.text_input("🔍 પ્રોડક્ટ્સ અને સર્વિસ શોધો...", placeholder="દા.ત. રેસ્ટોરન્ટ, ડોક્ટર...")

# કેટેગરી ગ્રીડ
cols = st.columns(4)
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]

for i, cat in enumerate(categories):
    with cols[i % 4]:
        st.button(cat)

# નવું રજીસ્ટ્રેશન બટન
st.markdown('<div class="orange-button">', unsafe_allow_html=True)
st.button("+ નવું સભ્ય રજીસ્ટ્રેશન", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# સભ્ય ડિરેક્ટરી કાર્ડ્સ (એક ઉદાહરણ)
st.subheader("સભ્ય ડિરેક્ટરી")
card1, card2, card3 = st.columns(3)
with card1:
    st.markdown("""
    **માજન સમાસિત**
    - બ્લડ ગ્રુપ: B+
    - બિઝનેસ: Lohana Clic
    - ફેમિલી આઈડી: 0011023
    """)
    st.button("View Profile", key="btn1")
