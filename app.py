import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Lohana Clic", layout="wide")

# 2. Design (CSS - No text title, centered logo)
st.markdown("""
    <style>
    .business-card { padding: 20px; border-radius: 10px; border: 1px solid #ddd; background: white; margin-bottom: 10px; }
    .business-card h3 { color: #333; margin: 0; }
    /* Logo centering */
    .stImage { display: flex; justify-content: center; }
    </style>
""", unsafe_allow_html=True)

# 3. Data Loading
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df.fillna("N/A", inplace=True)
    return df

try:
    df = load_data()

    # 4. Centered Logo (Text removed)
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        st.image("logo.png", width=300)

    # 5. Search Interface
    c1, c2, c3 = st.columns(3)
    
    main_options = ["Select"] + sorted(df['Main Category'].unique().tolist())
    main_cat = c1.selectbox("Main Category", main_options)
    
    if main_cat != "Select":
        sub_options = sorted(df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist())
    else:
        sub_options = []
        
    sub_cat = c2.selectbox("Sub Category", ["Select"] + sub_options)
    city = c3.text_input("Enter City or Pincode")
    
    search_btn = st.button("🔍 Search Business")

    # 6. Results Logic
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
