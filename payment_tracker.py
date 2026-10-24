import streamlit as st

st.set_page_config(
    page_title="UtilityCare Payment Tracker",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Safe Payment Tracker")
st.subheader("Check your electricity payment status")

st.info(
    "Demo application: All payment records are simulated. "
    "This application does not connect to real banks or electricity providers."
)

st.divider()

st.header("Enter Payment Details")

reference = st.text_input(
    "Transaction Reference",
    value="TXN10025"
)

amount = st.number_input(
    "Payment Amount (₹)",
    min_value=1.0,
    value=1500.0,
    step=100.0
)

bank_status = st.selectbox(
    "Bank Payment Status",
    ["Successful", "Pending", "Failed"]
)

portal_status = st.selectbox(
    "Electricity Portal Status",
    ["Paid", "Unpaid", "Update Pending"]
)

if st.button("Check Payment Status"):
    st.subheader("Payment Summary")

    st.write("Transaction Reference:", reference)
    st.write(f"Payment Amount: ₹{amount:.2f}")
    st.write("Bank Status:", bank_status)
    st.write("Portal Status:", portal_status)

    if bank_status == "Successful" and portal_status != "Paid":
        st.warning(
            "Your bank shows a successful payment, but the portal "
            "has not confirmed it. Do not pay again immediately. "
            "Keep your transaction reference and receipt, check "
            "the payment status with your provider, and contact "
            "support if the issue remains unresolved."
        )

    elif bank_status == "Successful" and portal_status == "Paid":
        st.success(
            "The sample record shows that payment was successful "
            "and the portal shows Paid."
        )

    elif bank_status == "Pending":
        st.warning(
            "Your payment is pending. Check the transaction status "
            "with your bank before attempting another payment."
        )

    else:
        st.error(
            "The sample bank status is Failed. Confirm the final "
            "transaction status with your bank before retrying."
        )

st.divider()

st.caption("UtilityCare | IMPACTX 2026 | Simulated Payment Tracker")