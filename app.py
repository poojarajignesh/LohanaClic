import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડિઝાઇન અને સ્ટાઈલિંગ
st.markdown("""
    <style>
    .big-title { text-align: center; font-size: 40px; color: #ff8200; font-weight: 800; margin-bottom: 30px; }
    .business-card { padding: 20px; border-radius: 10px; border: 1px solid #ddd; background: white; margin-bottom: 10px; }
    .business-card h3 { color: #333; margin: 0; }
    /* લોગો સેન્ટર કરવા માટે */
    [data-testid="stImage"] { display: flex; justify-content: center; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df.fillna("N/A", inplace=True)
    return df

try:
    df = load_data()

    # ૪. સેન્ટર્ડ લોગો
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", width=300)

    # ૫. સર્ચ ઈન્ટરફેસ
    c1, c2, c3 = st.columns(3)
    
    # Main Category Selection
    main_options = ["Select"] + sorted(df['Main Category'].unique().tolist())
    main_cat = c1.selectbox("Main Category", main_options)
    
    # Sub-Category Selection (Main Category પર આધારિત)
    if main_cat != "Select":
        sub_options = sorted(df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist())
    else:
        sub_options = []
        
    sub_cat = c2.selectbox("Sub Category", ["Select"] + sub_options)
    
    # Location Search
    city = c3.text_input("Enter City or Pincode")
    
    search_btn = st.button("🔍 Search Business")

    # ૬. રિઝલ્ટ લોજિક
    if search_btn:
        if main_cat == "Select" or sub_cat == "Select":
            st.error("Please select Category and Sub-category!")
        else:
            filtered = df[(df['Main Category'] == main_cat) & (df['Sub Category'] == sub_cat)]
            if city:
                if city.isdigit():
                    filtered = filtered[filtered['Pincode'].astype(str).str.contains(city, na=False)]
                else:
                    filtered = filtered[filtered['City'].str.contains(city, case=False, na=False)]
            
            if not filtered.empty:
                st.write(f"### Found {len(filtered)} results:")
                for _, row in filtered.iterrows():
                    st.markdown(f"""
                        <div class='business-card'>
                            <h3>{row['Sub Category']}</h3>
                            <p><b>📍 City:</b> {row['City']} | <b>Category:</b> {row['Main Category']}</p>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No results found.")

except Exception as e:
    st.error("Please ensure 'data.csv' and 'logo.png' are in your folder.")
