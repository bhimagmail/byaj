import streamlit as st
from datetime import datetime
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
    "नेपालमा प्रचलित गाउँघरको वार्षिक compounding ब्याज प्रणाली अनुसार हिसाब"
)

# ---------------------------------------------------
# CURRENT NEPALI DATE
# ---------------------------------------------------
today_bs = nepali_date.today()

# ---------------------------------------------------
# USER INPUTS
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

st.subheader("📅 Loan Date (BS)")

col1, col2, col3 = st.columns(3)

with col1:
    loan_year = st.number_input(
        "Year",
        min_value=2000,
        max_value=2090,
        value=today_bs.year - 2
    )

with col2:
    loan_month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=today_bs.month
    )

with col3:
    loan_day = st.number_input(
        "Day",
        min_value=1,
        max_value=32,
        value=today_bs.day
    )

# ---------------------------------------------------
# CURRENT DATE DISPLAY
# ---------------------------------------------------
st.subheader("📍 Current Nepali Date")

st.info(
    f"{today_bs.year}-{today_bs.month:02d}-{today_bs.day:02d}"
)

# ---------------------------------------------------
# CALCULATE TIME DIFFERENCE
# ---------------------------------------------------
try:

    loan_date_bs = nepali_date(
        int(loan_year),
        int(loan_month),
        int(loan_day)
    )

    # Convert to AD for subtraction
    loan_ad = loan_date_bs.to_datetime_date()
    today_ad = today_bs.to_datetime_date()

    total_days = (today_ad - loan_ad).days

    years = total_days // 365
    remaining_days = total_days % 365

    months = remaining_days // 30
    days = remaining_days % 30

    st.success(
        f"⏳ Time Duration: {years} year(s), "
        f"{months} month(s), {days} day(s)"
    )

except Exception as e:
    st.error("Invalid Loan Date")
    st.stop()

# ---------------------------------------------------
# INTEREST LOGIC
# ---------------------------------------------------
def calculate_village_interest(principal, rate, years, months, days):

    yearly_details = []

    original_principal = principal

    # -------------------------
    # YEARLY COMPOUNDING
    # -------------------------
    for year in range(1, years + 1):

        yearly_interest = (
            principal * 12 * rate
        ) / 100

        principal += yearly_interest

        yearly_details.append({
            "year": year,
            "interest": yearly_interest,
            "principal": principal
        })

    # -------------------------
    # MONTH INTEREST
    # -------------------------
    monthly_interest = (
        principal * months * rate
    ) / 100

    # -------------------------
    # DAILY INTEREST
    # -------------------------
    daily_interest = (
        principal * days * rate
    ) / (30 * 100)

    # -------------------------
    # FINAL AMOUNT
    # -------------------------
    final_amount = (
        principal
        + monthly_interest
        + daily_interest
    )

    return {
        "yearly_details": yearly_details,
        "monthly_interest": monthly_interest,
        "daily_interest": daily_interest,
        "final_amount": final_amount,
        "principal_after_years": principal,
        "original_principal": original_principal
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

    # -------------------------
    # YEARLY BREAKDOWN
    # -------------------------
    for detail in result["yearly_details"]:

        st.write(
            f"Year {detail['year']} Interest: "
            f"रु. {detail['interest']:,.2f}"
        )

        st.write(
            f"New Principal: "
            f"रु. {detail['principal']:,.2f}"
        )

        st.markdown("---")

    # -------------------------
    # MONTH + DAY
    # -------------------------
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