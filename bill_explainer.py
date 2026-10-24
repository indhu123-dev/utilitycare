import streamlit as st

st.title("🧾 Smart Bill Explainer")
st.write("Enter sample bill details to understand your electricity bill.")

st.info("Demo only: These are sample calculations, not official electricity tariffs.")

st.subheader("Enter Bill Details")

units = st.number_input(
    "Electricity used (units)",
    min_value=0,
    value=200,
    step=10
)

rate = st.number_input(
    "Charge per unit (₹)",
    min_value=0.0,
    value=5.0,
    step=0.5
)

fixed_charge = st.number_input(
    "Fixed charge (₹)",
    min_value=0.0,
    value=100.0,
    step=10.0
)

tax_percent = st.number_input(
    "Tax (%)",
    min_value=0.0,
    value=5.0,
    step=1.0
)

arrears = st.number_input(
    "Previous unpaid amount (₹)",
    min_value=0.0,
    value=0.0,
    step=50.0
)

adjustment = st.number_input(
    "Adjustment (₹; negative reduces the bill)",
    value=0.0,
    step=10.0
)

if st.button("Explain My Bill"):
    usage_charge = units * rate
    tax = (usage_charge + fixed_charge) * tax_percent / 100
    total = usage_charge + fixed_charge + tax + arrears + adjustment

    st.subheader("Bill Breakdown")

    st.write(f"Usage charge: ₹{usage_charge:.2f}")
    st.write(f"Fixed charge: ₹{fixed_charge:.2f}")
    st.write(f"Tax: ₹{tax:.2f}")
    st.write(f"Previous unpaid amount: ₹{arrears:.2f}")
    st.write(f"Adjustment: ₹{adjustment:.2f}")

    st.success(f"Estimated bill total: ₹{total:.2f}")

    st.subheader("What does this mean?")

    st.write(
        f"You used {units} units. The usage charge is "
        f"₹{usage_charge:.2f}, based on the sample rate "
        f"of ₹{rate:.2f} per unit."
    )

    if arrears > 0:
        st.warning(
            "Your bill includes a previous unpaid amount. "
            "Check the earlier bill to confirm it."
        )

    if adjustment != 0:
        st.write(
            "An adjustment has changed the bill total. "
            "Check the bill statement for its reason."
        )

    st.caption(
        "This prototype uses a simplified calculation. "
        "Actual bills may include slabs, other fees, and different tax rules."
    )