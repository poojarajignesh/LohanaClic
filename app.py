# સભ્ય રજીસ્ટ્રેશન ફોર્મ (Databank Form મુજબ)
st.subheader("📝 નવું સભ્ય રજીસ્ટ્રેશન ફોર્મ")

with st.form("registration_form", clear_on_submit=True):
    # પર્સનલ માહિતી
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("પૂરું નામ")
        father_name = st.text_input("પિતાનું નામ")
        dob = st.date_input("જન્મ તારીખ")
    with col2:
        blood_group = st.selectbox("બ્લડ ગ્રુપ", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
        city = st.text_input("ગામ / શહેર")
        mobile = st.text_input("મોબાઈલ નંબર")

    # વ્યવસાય માહિતી
    occupation = st.text_input("ધંધો / નોકરી / વ્યવસાયનું નામ")
    address = st.text_area("સરનામું")

    # સબમિટ બટન
    submit = st.form_submit_button("માહિતી સબમિટ કરો")

    if submit:
        # અહીં તમે શીટમાં ડેટા સેવ કરવાનું લોજિક મૂકી શકો છો
        st.success(f"આભાર {full_name}, તમારી વિગત નોંધાઈ ગઈ છે!")
