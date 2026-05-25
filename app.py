import streamlit as st
import pandas as pd

# ૧. પેજ સેટઅપ
st.set_page_config(page_title="Lohana Clic", layout="wide")

# ૨. કસ્ટમ CSS (કાર્ડ્સને સુંદર બનાવવા માટે)
st.markdown("""
    <style>
    .business-card { padding: 15px; border-radius: 10px; border: 1px solid #ddd; margin-bottom: 10px; background-color: #f9f9f9; }
    </style>
""", unsafe_allow_html=True)

# ૩. ડેટા લોડિંગ
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df.columns = df.columns.str.strip()
    df['Main Category'] = df['Main Category'].ffill()
    df['City'] = df['City'].fillna('Ahmedabad') # ડિફોલ્ટ શહેર
    return df

df = load_data()

st.image("logo.png", width=200)
st.subheader("🔍 વ્યવસાય શોધો")

# ૪. સર્ચ ડ્રોપડાઉન
c1, c2, c3 = st.columns(3)

# શહેર ડ્રોપડાઉન
city = c3.selectbox("શહેર", ["Select"] + sorted(df['City'].unique().tolist()))

# મેઈન કેટેગરી
main_options = ["Select"] + df['Main Category'].unique().tolist()
main_cat = c1.selectbox("મેઈન કેટેગરી", main_options)

# સબ-કેટેગરી
sub_cats = []
if main_cat != "Select":
    sub_cats = df[df['Main Category'] == main_cat]['Sub Category'].dropna().unique().tolist()
sub_cat = c2.selectbox("સબ-કેટેગરી", ["Select"] + sub_cats)

# ૫. સર્ચ રિઝલ્ટ (Justdial સ્ટાઈલ કાર્ડ્સ)
if st.button("સર્ચ કરો"):
    if main_cat == "Select" or sub_cat == "Select":
        st.warning("કૃપા કરીને કેટેગરી સિલેક્ટ કરો.")
    else:
        filtered = df[(df['Main Category'] == main_cat) & (df['Sub Category'] == sub_cat)]
        if city != "Select":
            filtered = filtered[filtered['City'] == city]

        if not filtered.empty:
            st.write(f"### {len(filtered)} પરિણામો મળ્યા:")
            for index, row in filtered.iterrows():
                # સુંદર કાર્ડ બનાવવા માટે
                st.markdown(f"""
                <div class="business-card">
                    <h4>{row['Sub Category']}</h4>
                    <p>📍 શહેર: {row['City']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button("સંપર્ક કરો", key=f"btn_{index}"):
                    st.toast("સંપર્ક વિગત: 98XXXXXX00") # અહીં તમે નંબર ઉમેરી શકો
        else:
            st.info("ક્ષમા કરશો, કોઈ ડેટા મળ્યો નથી.")
