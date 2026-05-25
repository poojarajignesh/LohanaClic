import streamlit as st

# પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# કસ્ટમ CSS (ડિઝાઈન માટે)
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

# હેડર: લોગો (મોટો સાઈઝમાં)
col1, col2 = st.columns([1, 10])
with col1:
    st.image("logo.png", width=200)
with col2:
    st.empty() # નામ કાઢી નાખ્યું છે

# સર્ચ બાર
st.text_input("", placeholder="🔍 પ્રોડક્ટ્સ અને સર્વિસ શોધો...")

# કેટેગરી ગ્રીડ
st.subheader("કેટેગરી")
categories = ["🍽️ રેસ્ટોરન્ટ", "🏨 હોટેલ્સ", "🎓 એજ્યુકેશન", "💄 બ્યુટી સ્પા", "💼 વ્યવસાય", "⚖️ વકીલ", "🏥 ડોક્ટર્સ", "❤️ બ્લડ"]
cols = st.columns(4)

for i, cat in enumerate(categories):
    with cols[i % 4]:
        st.button(cat)

# રજીસ્ટ્રેશન બટન
st.markdown('<div class="orange-button">', unsafe_allow_html=True)
st.button("+ નવું સભ્ય રજીસ્ટ્રેશન")
st.markdown('</div>', unsafe_allow_html=True)

# રજીસ્ટ્રેશન ફોર્મ (પોઈન્ટ 4 મુજબ)
st.subheader("📝 સભ્ય રજીસ્ટ્રેશન વિગત")
with st.form("reg_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("પૂરું નામ")
        father_name = st.text_input("પિતાનું નામ")
        dob = st.date_input("જન્મ તારીખ")
    with col2:
        blood_group = st.selectbox("બ્લડ ગ્રુપ", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        city = st.text_input("ગામ / શહેર")
        mobile = st.text_input("મોબાઈલ નંબર")

    occupation = st.text_input("ધંધો / નોકરી / વ્યવસાયનું નામ")
    address = st.text_area("સરનામું")

    submit = st.form_submit_button("માહિતી સબમિટ કરો")

    if submit:
        st.success(f"આભાર {full_name}, તમારી વિગત નોંધાઈ ગઈ છે!")
