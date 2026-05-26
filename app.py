import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ફોટા જેવી ડિઝાઇન (CSS)
st.markdown("""
    <style>
    .big-title { text-align: center; font-size: 50px; color: #ff8200; font-weight: 800; margin-bottom: 20px; }
    .search-box { background: #ffffff; padding: 30px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #ddd; }
    .business-card { padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; background: white; margin-bottom: 15px; transition: 0.3s; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df.fillna("N/A", inplace=True)
    return df

df = load_data()

# ૪. લોગો અને ટાઈટલ
# તમારી પાસે logo.png હોવી જોઈએ
st.image("logo.png", width=200) 
st.markdown("<h1 class='big-title'>Lohana Clic</h1>", unsafe_allow_html=True)

# ૫. વચ્ચેનું સર્ચ બોક્સ
with st.container():
    st.markdown("<div class='search-box'>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    # Main Category Selection
    main_options = ["All"] + sorted(df['Main Category'].unique().tolist())
    main_cat = c1.selectbox("Main Category", main_options)
    
    # સુધારેલું Logic: Main Category મુજબ Sub Category ફિલ્ટર થશે
    if main_cat != "All":
        sub_options = sorted(df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist())
    else:
        sub_options = sorted(df['Sub Category'].unique().tolist())
        
    sub_cat = c2.selectbox("Sub Category", ["All"] + sub_options)
    
    search_input = c3.text_input("Enter City or Pincode")
    
    search_btn = st.button("🔍 Search Business")
    st.markdown("</div>", unsafe_allow_html=True)

# ૬. રિઝલ્ટ કાર્ડ્સ
if search_btn:
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
            st.markdown(f"""
                <div class='business-card'>
                    <h3>{row['Sub Category']}</h3>
                    <p><b>📍 City:</b> {row['City']} | <b>Category:</b> {row['Main Category']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No results found.")
