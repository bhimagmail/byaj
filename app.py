import streamlit as st
from nepali_datetime import date as nepali_date

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Village Interest Calculator",
    page_icon="💰",
    layout="centered"
)

# ---------------------------------------------------
# CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    padding-top: 20px;
}

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    background-color: #0f62fe;
    color: white;
}

.result-box {
    background-color: #f5f7fa;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    border: 1px solid #dfe3e8;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------
st.title("💰 Village Interest Calculator")

st.write(
    "नेपालमा प्रचलित गाउँघरको वार्षिक compounding ब्याज प्रणाली"
)

# ---------------------------------------------------
# CURRENT BS DATE
# ---------------------------------------------------
today_bs = nepali_date.today()

# ---------------------------------------------------
# INPUTS
# ---------------------------------------------------
principal = st.number_input(
    "मूल रकम (Principal Amount)",
    min_value=0.0,
    value=80000.0,
    step=1000.0
)

rate = st.number_input(
    "मासिक ब्याज दर (%)",
    min_value=0.0,
    value=3.0,
    step=0.5
)

# ---------------------------------------------------
# LOAN DATE
# ---------------------------------------------------
st.subheader("📅 Loan Date (BS)")

loan_col1, loan_col2, loan_col3 = st.columns(3)

with loan_col1:
    loan_year = st.number_input(
        "Loan Year",
        min_value=2000,
        max_value=2090,
        value=today_bs.year - 1
    )

with loan_col2:
    loan_month = st.number_input(
        "Loan Month",
        min_value=1,
        max_value=12,
        value=today_bs.month
    )

with loan_col3:
    loan_day = st.number_input(
        "Loan Day",
        min_value=1,
        max_value=32,
        value=today_bs.day
    )

# ---------------------------------------------------
# CURRENT DATE
# ---------------------------------------------------
st.subheader("📍 Current Date (BS)")

current_col1, current_col2, current_col3 = st.columns(3)

with current_col1:
    current_year = st.number_input(
        "Current Year",
        min_value=2000,
        max_value=2090,
        value=today_bs.year
    )

with current_col2:
    current_month = st.number_input(
        "Current Month",
        min_value=1,
        max_value=12,
        value=today_bs.month
    )

with current_col3:
    current_day = st.number_input(
        "Current Day",
        min_value=1,
        max_value=32,
        value=today_bs.day
    )

# ---------------------------------------------------
# CALCULATE DATE DIFFERENCE
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
        st.error("Current date must be after loan date")
        st.stop()

    years = total_days // 365

    remaining_days = total_days % 365

    months = remaining_days // 30

    days = remaining_days % 30

    # SHOW ONLY AFTER DATE SELECTION
    st.success(
        f"⏳ Time Duration: "
        f"{years} year(s), "
        f"{months} month(s), "
        f"{days} day(s)"
    )

except:
    st.error("Invalid Date")
    st.stop()

# ---------------------------------------------------
# INTEREST LOGIC
# ---------------------------------------------------
def calculate_village_interest(
    principal,
    rate,
    years,
    months,
    days
):

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

    # FINAL AMOUNT
    final_amount = (
        principal
        + monthly_interest
        + daily_interest
    )

    return {
        "principal_after_years": principal,
        "monthly_interest": monthly_interest,
        "daily_interest": daily_interest,
        "final_amount": final_amount
    }

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------
if st.button("🧮 ब्याज Calculate गर्नुहोस्"):

    result = calculate_village_interest(
        principal,
        rate,
        years,
        months,
        days
    )

    st.markdown(
        '<div class="result-box">',
        unsafe_allow_html=True
    )

    st.subheader("📊 Result")

    st.write(
        f"🏦 Principal After {years} Year(s): "
        f"रु. {result['principal_after_years']:,.2f}"
    )

    st.write(
        f"📅 Month Interest: "
        f"रु. {result['monthly_interest']:,.2f}"
    )

    st.write(
        f"🗓️ Day Interest: "
        f"रु. {result['daily_interest']:,.2f}"
    )

    st.write(
        f"💰 Final Amount: "
        f"रु. {result['final_amount']:,.2f}"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Built by Er. Santosh ❤️")