import streamlit as st
import pandas as pd

# ૧. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df['Main Category'] = df['Main Category'].ffill()
    
    # લોકેશન ફાઈલ લોડ કરો
    loc_df = pd.read_csv("location_data.csv")
    loc_df.columns = loc_df.columns.str.strip()
    return df, loc_df

df, loc_df = load_data()

st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

# ૨. લોકેશન ડ્રોપડાઉન (ઓટોમેટિક લિસ્ટ)
st.subheader("📍 લોકેશન પસંદ કરો")
c1, c2, c3 = st.columns(3)

# સ્ટેટ -> ડિસ્ટ્રિક્ટ -> તાલુકા ઓટોમેટિક આવશે
state = c1.selectbox("રાજ્ય", ["Select"] + loc_df['State'].unique().tolist())
districts = ["Select"]
if state != "Select":
    districts += loc_df[loc_df['State'] == state]['District'].unique().tolist()
district = c2.selectbox("જિલ્લો", districts)

talukas = ["Select"]
if district != "Select":
    talukas += loc_df[(loc_df['District'] == district)]['Taluka'].unique().tolist()
taluka = c3.selectbox("તાલુકો (City)", talukas)

# ૩. કેટેગરી
main_cat = st.selectbox("મેઈન કેટેગરી", ["Select"] + df['Main Category'].unique().tolist())

# ૪. સર્ચ લોજિક
if st.button("સર્ચ કરો"):
    if taluka == "Select" or main_cat == "Select":
        st.warning("કૃપા કરીને લોકેશન અને કેટેગરી સિલેક્ટ કરો.")
    else:
        # લોકેશન અને કેટેગરી મુજબ ડેટા ફિલ્ટર
        filtered = df[(df['Main Category'] == main_cat)]
        
        st.write(f"### {taluka} માં રિઝલ્ટ:")
        if not filtered.empty:
            for index, row in filtered.iterrows():
                with st.container(border=True):
                    st.write(f"**{row['Sub Category']}**")
                    st.write(f"📍 સ્થળ: {taluka}")
        else:
            st.info("કોઈ ડેટા મળ્યો નથી.")
