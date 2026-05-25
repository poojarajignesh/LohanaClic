import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    return df

df = load_data()

st.markdown("<h1 style='text-align: center; color: #ff8200;'>Lohana Clic</h1>", unsafe_allow_html=True)

# ૩. Category વિભાગ (હંમેશા ફિક્સ રહેશે)
st.subheader("📂 Select Business Category")
col1, col2 = st.columns(2)
main_cat = col1.selectbox("Main Category", ["All"] + df['Main Category'].unique().tolist())
sub_cat_list = df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist() if main_cat != "All" else df['Sub Category'].unique().tolist()
sub_cat = col2.selectbox("Sub Category", ["All"] + sorted(sub_cat_list))

st.write("---")

# ૪. Location/Search વિભાગ (અહીં તમે સર્ચ કરશો)
st.subheader("📍 Search by City or Pincode")
search_input = st.text_input("Type Pincode or City name...")

# ૫. ફિલ્ટર લોજિક
filtered_df = df.copy()

# Category ફિલ્ટર
if main_cat != "All":
    filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
if sub_cat != "All":
    filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]

# Location ફિલ્ટર
if search_input:
    if search_input.isdigit():
        filtered_df = filtered_df[filtered_df['Pincode'].astype(str).str.contains(search_input, na=False)]
    else:
        filtered_df = filtered_df[filtered_df['City'].str.contains(search_input, case=False, na=False)]

# રિઝલ્ટ બતાવવાનું લોજિક
if not filtered_df.empty:
    st.write(f"### Found {len(filtered_df)} results:")
    for _, row in filtered_df.iterrows():
        with st.container(border=True):
            st.write(f"**Business:** {row['Sub Category']}")
            st.write(f"**City:** {row['City']} | **Category:** {row['Main Category']}")
else:
    st.info("Please select category or enter location to see results.")
