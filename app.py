import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide", initial_sidebar_state="collapsed")

# ૨. મોડર્ન સ્ટાઈલિંગ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }
    .title { text-align: center; font-size: 3rem; font-weight: 700; color: #ff8200; margin-bottom: 20px; }
    .search-section { background: #ffffff; padding: 30px; border-radius: 15px; border: 1px solid #ddd; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stButton>button { width: 100%; background-color: #ff8200; color: white; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    pin_df = pd.read_csv("pincode.csv")
    pin_df.columns = pin_df.columns.str.strip()
    return df, pin_df

df, pin_df = load_data()

# ૪. યુઝર ઈન્ટરફેસ
st.markdown("<h1 class='title'>Lohana Clic</h1>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='search-section'>", unsafe_allow_html=True)
    
    # સિટીનું લિસ્ટ જે યુઝર ટાઈપ કરી શકે
    city_list = sorted(df['City'].dropna().unique().tolist())
    
    # પિનકોડ અને સિટી સર્ચ બાર
    search_input = st.text_input("📍 Enter Pincode or start typing City Name")
    
    # ઓટોમેટિક સર્ચ માટે ડ્રોપડાઉન (જે સ્પેલિંગ મિસ્ટેક અટકાવશે)
    selected_city = st.selectbox("OR Select City from list:", ["Select"] + city_list)
    
    search_btn = st.button("Search Business")
    st.markdown("</div>", unsafe_allow_html=True)

# ૫. સર્ચ લોજિક
if search_btn:
    results = pd.DataFrame()
    
    # જો પિનકોડ નાખ્યો હોય
    if search_input.isdigit():
        match = pin_df[pin_df['pincode'] == int(search_input)]
        if not match.empty:
            city_found = match.iloc[0]['district'].upper()
            results = df[df['City'].str.upper().str.contains(city_found, na=False)]
            st.success(f"Showing results for Pincode area: {city_found}")
    
    # જો સિટીનું નામ નાખ્યું હોય અથવા ડ્રોપડાઉનમાંથી સિલેક્ટ કર્યું હોય
    elif selected_city != "Select":
        results = df[df['City'] == selected_city]
    elif search_input:
        results = df[df['City'].str.contains(search_input, case=False, na=False)]

    # રિઝલ્ટ બતાવવાનું લોજિક
    if not results.empty:
        st.write(f"### {len(results)} Business found:")
        for _, row in results.iterrows():
            with st.container(border=True):
                st.subheader(row['Sub Category'])
                st.write(f"**City:** {row['City']}")
    else:
        st.info("No business found. Please check spelling or try another location.")
