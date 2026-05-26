import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. લોડિંગ ડેટા (પ્રોપર રીતે)
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df.fillna("N/A", inplace=True)
    return df

df = load_data()

# ૩. સ્ટેટ મેનેજમેન્ટ (જેથી રિઝલ્ટ ગાયબ ન થાય)
if 'search_clicked' not in st.session_state:
    st.session_state.search_clicked = False

# ૪. લોગો અને ટાઈટલ
st.image("logo.png", width=200) 
st.markdown("<h1 style='text-align: center; color: #ff8200;'>Lohana Clic</h1>", unsafe_allow_html=True)

# ૫. સર્ચ બોક્સ
with st.container():
    st.markdown("<div style='background:#f9f9f9; padding:20px; border-radius:15px;'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    # Main Category
    main_options = ["All"] + sorted(df['Main Category'].unique().tolist())
    main_cat = c1.selectbox("Main Category", main_options, key="main_cat")
    
    # સુધારેલું Logic: Main Category મુજબ બધા જ Sub-options લાવશે
    if main_cat != "All":
        sub_options = ["All"] + sorted(df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist())
    else:
        sub_options = ["All"] + sorted(df['Sub Category'].unique().tolist())
        
    sub_cat = c2.selectbox("Sub Category", sub_options, key="sub_cat")
    search_input = c3.text_input("Enter City or Pincode")
    
    if st.button("🔍 Search Business"):
        st.session_state.search_clicked = True
    st.markdown("</div>", unsafe_allow_html=True)

# ૬. રિઝલ્ટ કાર્ડ્સ (જે ક્યારેય ગાયબ નહીં થાય)
if st.session_state.search_clicked:
    filtered_df = df.copy()
    if main_cat != "All": filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
    if sub_cat != "All": filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]
    
    if search_input:
        if search_input.isdigit():
            filtered_df = filtered_df[filtered_df['Pincode'].astype(str).str.contains(search_input, na=False)]
        else:
            filtered_df = filtered_df[filtered_df['City'].str.contains(search_input, case=False, na=False)]

    if not filtered_df.empty:
        st.write(f"### Found {len(filtered_df)} results:")
        for _, row in filtered_df.iterrows():
            with st.container(border=True):
                st.write(f"### {row['Sub Category']}")
                st.write(f"📍 City: {row['City']} | Category: {row['Main Category']}")
    else:
        st.info("No results found.")
