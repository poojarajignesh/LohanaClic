import streamlit as st

st.header("📋 Lohana Samaj Databank Registration")

with st.form("main_form"):
    # Personal Info
    st.subheader("Personal Information")
    name = st.text_input("Puru Naam")
    dob = st.date_input("Janm Tarikh")
    education = st.text_input("Shikshan (Education)")
    
    # Contact
    st.subheader("Contact Details")
    mobile = st.text_input("Mobile Number")
    whatsapp = st.text_input("WhatsApp Number")
    address = st.text_area("Address")
    
    # Professional
    st.subheader("Business / Service Details")
    occupation = st.text_input("Vyavsay / Job Profile")
    business_name = st.text_input("Business Name")
    
    # Matrimony/Blood Group
    col1, col2 = st.columns(2)
    with col1:
        blood_group = st.selectbox("Blood Group", ["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])
    with col2:
        marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
    
    submit = st.form_submit_button("Submit Data")

    if submit:
        # Aahi tame Google Sheet ma data mokalvano code muki shaksho
        st.success("Tari vigat sachalai gai che!")
