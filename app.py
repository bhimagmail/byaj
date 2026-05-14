import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="साधारण ब्याज Calculator",
    page_icon="💰",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
.main {
    padding-top: 20px;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: bold;
    background-color: #1f77b4;
    color: white;
}

.result-box {
    background-color: #f1f5f9;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("💰 साधारण ब्याज Calculator")
st.write("Principal, Rate र Time अनुसार साधारण ब्याज हिसाब गर्नुहोस्।")

# Function
def calculate_simple_interest(principal, rate, years, months, days):

    total_time = years + (months / 12) + (days / 365)

    simple_interest = (principal * rate * total_time) / 100

    total_amount = principal + simple_interest

    return simple_interest, total_amount, total_time


# Inputs
st.subheader("📌 विवरण")

principal = st.number_input(
    "मूल रकम (Principal)",
    min_value=0.0,
    value=100000.0,
    step=1000.0
)

rate = st.number_input(
    "ब्याज दर (%)",
    min_value=0.0,
    value=12.0,
    step=0.5
)

col1, col2, col3 = st.columns(3)

with col1:
    years = st.number_input("वर्ष", min_value=0, value=1)

with col2:
    months = st.number_input("महिना", min_value=0, max_value=11, value=0)

with col3:
    days = st.number_input("दिन", min_value=0, max_value=31, value=0)


# Button
if st.button("🧮 Calculate ब्याज"):

    interest, total_amount, total_time = calculate_simple_interest(
        principal,
        rate,
        years,
        months,
        days
    )

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.subheader("📊 परिणाम")

    st.write(f"⏳ कुल समय: {total_time:.2f} वर्ष")
    st.write(f"💵 साधारण ब्याज: रु. {interest:,.2f}")
    st.write(f"💰 कुल रकम: रु. {total_amount:,.2f}")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Made with Streamlit ❤️")
