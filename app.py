import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    
    # ખાલી જગ્યામાં 'Other' ભરી દો જેથી NaN ન આવે
    df['Main Category'] = df['Main Category'].fillna('Other')
    df['Sub Category'] = df['Sub Category'].fillna('Other')
    return df

df = load_data()

st.markdown("<h1 style='text-align: center; color: #ff8200;'>Lohana Clic</h1>", unsafe_allow_html=True)

# ૩. ફિક્સ Category ફિલ્ટર
st.subheader("📂 Filter by Category")
col1, col2 = st.columns(2)

# Main Category
main_options = ["All"] + sorted(df['Main Category'].unique().tolist())
main_cat = col1.selectbox("Main Category", main_options)

# Sub Category (Main Category મુજબ બદલાશે)
if main_cat == "All":
    sub_options = ["All"] + sorted(df['Sub Category'].unique().tolist())
else:
    # ફક્ત તે મેઈન કેટેગરીની અંદરની જ સબ-કેટેગરી બતાવશે
    sub_options = ["All"] + sorted(df[df['Main Category'] == main_cat]['Sub Category'].unique().tolist())

sub_cat = col2.selectbox("Sub Category", sub_options)

st.write("---")

# ૪. Location/Search વિભાગ
st.subheader("📍 Search by City or Pincode")
search_input = st.text_input("Type Pincode or City name...")

# ૫. ફિલ્ટર લોજિક (Category + Location)
filtered_df = df.copy()

if main_cat != "All":
    filtered_df = filtered_df[filtered_df['Main Category'] == main_cat]
if sub_cat != "All":
    filtered_df = filtered_df[filtered_df['Sub Category'] == sub_cat]

if search_input:
    if search_input.isdigit():
        filtered_df = filtered_df[filtered_df['Pincode'].astype(str).str.contains(search_input, na=False)]
    else:
        filtered_df = filtered_df[filtered_df['City'].str.contains(search_input, case=False, na=False)]

# રિઝલ્ટ
if not filtered_df.empty:
    st.write(f"### Found {len(filtered_df)} results:")
    for _, row in filtered_df.iterrows():
        with st.container(border=True):
            st.write(f"**Business:** {row['Sub Category']}")
            st.write(f"**City:** {row['City']} | **Main:** {row['Main Category']}")
else:
    st.info("No business found matching these criteria.")
