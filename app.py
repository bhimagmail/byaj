import streamlit as st
from nepali_datetime import date as nepali_date

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Village Interest Calculator",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

:root {
    --radius: 18px;
}

.block-container {
    max-width: 760px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 2.4rem;
    font-weight: 800;
    margin-bottom: 0.2rem;
}

.sub-text {
    opacity: 0.75;
    margin-bottom: 2rem;
}

.card {
    padding: 22px;
    border-radius: var(--radius);
    border: 1px solid rgba(128,128,128,0.18);
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(10px);
    margin-bottom: 20px;
}

.metric-card {
    padding: 18px;
    border-radius: 16px;
    border: 1px solid rgba(128,128,128,0.15);
    margin-bottom: 14px;
    background: rgba(255,255,255,0.03);
}

.metric-label {
    font-size: 14px;
    opacity: 0.7;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    margin-top: 6px;
}

.stButton > button {
    width: 100%;
    height: 56px;
    border-radius: 16px;
    border: none;
    font-size: 18px;
    font-weight: 700;
    background: linear-gradient(90deg,#2563eb,#1d4ed8);
    color: white;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
}

.footer {
    text-align: center;
    margin-top: 40px;
    opacity: 0.75;
    font-size: 14px;
}

.social-links a {
    text-decoration: none;
    margin: 0 10px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    '<div class="main-title">💰 Village Interest Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-text">नेपालमा प्रचलित गाउँघरको वार्षिक compounding ब्याज प्रणाली</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------
# TODAY BS DATE
# ---------------------------------------------------
today_bs = nepali_date.today()

# ---------------------------------------------------
# INPUT CARD
# ---------------------------------------------------
# st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("Loan Details")

principal = st.number_input(
    "Principal Amount (मूल रकम)",
    min_value=0.0,
    value=80000.0,
    step=1000.0
)

rate = st.number_input(
    "Monthly Interest Rate (मासिक ब्याज दर %)",
    min_value=0.0,
    value=3.0,
    step=0.5
)

st.markdown("### 📅 Loan Date (BS)")

loan_col1, loan_col2, loan_col3 = st.columns(3)

with loan_col1:
    loan_year = st.number_input(
        "Loan Year (वर्ष)",
        min_value=2000,
        max_value=2090,
        value=today_bs.year - 1
    )

with loan_col2:
    loan_month = st.number_input(
        "Loan Month (महिना)",
        min_value=1,
        max_value=12,
        value=today_bs.month
    )

with loan_col3:
    loan_day = st.number_input(
        "Loan Day (दिन)",
        min_value=1,
        max_value=32,
        value=today_bs.day
    )

st.markdown("### 📍 Current Date (BS)")

current_col1, current_col2, current_col3 = st.columns(3)

with current_col1:
    current_year = st.number_input(
        "Current Year (वर्ष)",
        min_value=2000,
        max_value=2090,
        value=today_bs.year
    )

with current_col2:
    current_month = st.number_input(
        "Current Month (महिना)",
        min_value=1,
        max_value=12,
        value=today_bs.month
    )

with current_col3:
    current_day = st.number_input(
        "Current Day (दिन)",
        min_value=1,
        max_value=32,
        value=today_bs.day
    )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# DATE CALCULATION
# ---------------------------------------------------
try:

    loan_date_bs = nepali_date(
        int(loan_year),
        int(loan_month),
        int(loan_day)
    )

    current_date_bs = nepali_date(
        int(current_year),
        int(current_month),
        int(current_day)
    )

    loan_ad = loan_date_bs.to_datetime_date()

    current_ad = current_date_bs.to_datetime_date()

    total_days = (current_ad - loan_ad).days

    if total_days < 0:
        st.error("Current date must be after loan date.")
        st.stop()

    years = total_days // 365

    remaining_days = total_days % 365

    months = remaining_days // 30

    days = remaining_days % 30

    st.info(
        f"⏳ Duration: {years} years, "
        f"{months} months, "
        f"{days} days"
    )

except:
    st.error("Invalid date selected.")
    st.stop()

# ---------------------------------------------------
# INTEREST LOGIC
# ---------------------------------------------------
def calculate_interest(
    principal,
    rate,
    years,
    months,
    days
):

    original_principal = principal

    # YEARLY COMPOUNDING
    for _ in range(years):

        yearly_interest = (
            principal * 12 * rate
        ) / 100

        principal += yearly_interest

    # MONTHLY INTEREST
    monthly_interest = (
        principal * months * rate
    ) / 100

    # DAILY INTEREST
    daily_interest = (
        principal * days * rate
    ) / (30 * 100)

    final_amount = (
        principal
        + monthly_interest
        + daily_interest
    )

    total_interest = (
        final_amount
        - original_principal
    )

    return {
        "interest": total_interest,
        "total": final_amount
    }

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------
if st.button("🧮 Calculate Interest"):

    result = calculate_interest(
        principal,
        rate,
        years,
        months,
        days
    )

    # st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Result")

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Principal Amount (मूल रकम)</div>
        <div class="metric-value">रु. {principal:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Interest (ब्याज)</div>
        <div class="metric-value">रु. {result['interest']:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Amount (कुल रकम)</div>
        <div class="metric-value">रु. {result['total']:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("""
<div class="footer">

Made with ❤️ by <b>Er. Santosh Kapari</b>

<br><br>

<div class="social-links">
    <a href="https://facebook.com/" target="_blank">Facebook</a>
    •
    <a href="https://instagram.com/" target="_blank">Instagram</a>
    •
    <a href="https://github.com/" target="_blank">GitHub</a>
    •
    <a href="https://linkedin.com/" target="_blank">LinkedIn</a>
</div>

</div>
""", unsafe_allow_html=True)