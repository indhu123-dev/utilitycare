import streamlit as st
from uuid import uuid4

# ==========================================
# 1. PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="UtilityCare",
    page_icon="⚡",
    layout="wide"
)

# ==========================================
# 2. SIDEBAR NAVIGATION
# ==========================================

st.sidebar.title("⚡ UtilityCare")
st.sidebar.caption("Utilities That Explain Themselves")

pages = [
    "Home",
    "Smart Bill Explainer",
    "Bill Reading Verification",
    "Safe Payment Tracker",
    "Outage Reporting",
    "Tenant Support",
    "Priority Customer Support"
]

page = st.sidebar.radio("Choose a feature", pages)

st.title("⚡ UtilityCare")
st.subheader("Utilities That Explain Themselves")
st.caption("IMPACTX 2026 Hackathon | Problem 18")
st.divider()

# ==========================================
# 3. HOME
# ==========================================

if page == "Home":

    st.header("Welcome to UtilityCare")

    st.write(
        "UtilityCare helps people understand utility bills, "
        "verify meter readings, track payment problems, "
        "report outages, and manage complaints."
    )

    st.info(
        "Hackathon prototype: all calculations and reports use "
        "demo data. No real utility, bank, or support system is connected."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧾 Smart Bill Explainer")
        st.write("Understand bill amounts and possible reasons for increases.")

        st.markdown("### 🔍 Bill Reading Verification")
        st.write("Compare meter readings with billed units.")

        st.markdown("### 💳 Safe Payment Tracker")
        st.write("Understand payment status mismatches.")

    with col2:
        st.markdown("### ⚡ Outage Reporting")
        st.write("Create a sample electricity outage report.")

        st.markdown("### 🏠 Tenant Support")
        st.write("Create a utility-related tenant complaint.")

        st.markdown("### 🚨 Priority Customer Support")
        st.write("Identify complaints that may require urgent attention.")

# ==========================================
# 4. SMART BILL EXPLAINER
# ==========================================

elif page == "Smart Bill Explainer":

    st.header("🧾 Smart Bill Explainer")

    st.write("Enter sample bill details to calculate the estimated amount.")

    col1, col2 = st.columns(2)

    with col1:
        units = st.number_input(
            "Units consumed (kWh)", min_value=0.0,
            value=200.0, step=10.0
        )
        rate = st.number_input(
            "Sample rate per unit (₹)", min_value=0.0,
            value=6.0, step=0.5
        )
        fixed_charge = st.number_input(
            "Fixed charges (₹)", min_value=0.0,
            value=100.0, step=10.0
        )
        tax_percent = st.number_input(
            "Sample tax (%)", min_value=0.0,
            value=5.0, step=1.0
        )

    with col2:
        arrears = st.number_input(
            "Previous dues (₹)", min_value=0.0,
            value=0.0, step=50.0
        )
        adjustment = st.number_input(
            "Other adjustment (₹)", value=0.0, step=10.0
        )
        usual_bill = st.number_input(
            "Usual monthly bill (₹)", min_value=1.0,
            value=1000.0, step=100.0
        )
        reading_type = st.selectbox(
            "Meter reading type", ["Actual", "Estimated", "Unknown"]
        )
        estimated_months = st.number_input(
            "Consecutive estimated months",
            min_value=0, value=0, step=1
        )

    if st.button("Explain My Bill", type="primary"):

        energy_charge = units * rate
        subtotal = energy_charge + fixed_charge
        tax = subtotal * tax_percent / 100
        total = subtotal + tax + arrears + adjustment

        st.subheader("Bill Breakdown")

        c1, c2, c3 = st.columns(3)
        c1.metric("Energy Charge", f"₹{energy_charge:.2f}")
        c2.metric("Tax", f"₹{tax:.2f}")
        c3.metric("Estimated Total", f"₹{total:.2f}")

        st.write(f"Fixed charges: ₹{fixed_charge:.2f}")
        st.write(f"Previous dues: ₹{arrears:.2f}")
        st.write(f"Other adjustment: ₹{adjustment:.2f}")

        if total >= 2 * usual_bill:
            st.warning(
                "Your entered bill is at least twice your usual bill. "
                "Review the units, rates, dues, and adjustments."
            )
        else:
            st.success(
                "Your entered bill is less than twice your usual bill. "
                "Review the breakdown to understand the amount."
            )

        if reading_type == "Estimated":
            st.write(
                "• The bill uses an estimated reading. Compare it "
                "with an actual meter reading if available."
            )

        if reading_type == "Unknown":
            st.write("• Check whether the bill uses an actual or estimated reading.")

        if estimated_months >= 2:
            st.write(
                "• Several estimated bills in a row may need review."
            )

        if arrears > 0:
            st.write("• Previous dues contribute to the total.")

        if adjustment != 0:
            st.write("• An additional adjustment affects the total.")

        st.caption(
            "Sample calculation only. This does not prove that a bill is incorrect."
        )

# ==========================================
# 5. BILL READING VERIFICATION
# ==========================================

elif page == "Bill Reading Verification":

    st.header("🔍 Bill Reading Verification")

    st.write("Compare meter readings with the units printed on the bill.")

    previous_reading = st.number_input(
        "Previous meter reading", min_value=0.0,
        value=1200.0, step=10.0
    )

    current_reading = st.number_input(
        "Current meter reading", min_value=0.0,
        value=1800.0, step=10.0
    )

    billed_units = st.number_input(
        "Units shown on bill", min_value=0.0,
        value=650.0, step=10.0
    )

    tolerance = st.number_input(
        "Allowed difference (units)", min_value=0.0,
        value=1.0, step=1.0
    )

    if st.button("Verify Reading", type="primary"):

        if current_reading < previous_reading:
            st.error(
                "Current reading is lower than the previous reading. "
                "Check the entries or whether the meter was reset or replaced."
            )
        else:
            calculated_units = current_reading - previous_reading
            difference = abs(calculated_units - billed_units)

            c1, c2, c3 = st.columns(3)
            c1.metric("Calculated Usage", f"{calculated_units:.2f}")
            c2.metric("Billed Usage", f"{billed_units:.2f}")
            c3.metric("Difference", f"{difference:.2f}")

            if difference <= tolerance:
                st.success("The readings match within the selected tolerance.")
            else:
                st.warning(
                    "A difference was detected. Check the readings, "
                    "billing dates, and any meter multiplier."
                )

            st.caption(
                "A difference needs investigation; it does not automatically prove an error."
            )

# ==========================================
# 6. SAFE PAYMENT TRACKER
# ==========================================

elif page == "Safe Payment Tracker":

    st.header("💳 Safe Payment Tracker")

    st.write("Compare the entered bank status with the utility portal status.")

    reference = st.text_input(
        "Payment reference (demo)", placeholder="Example: PAY12345"
    )

    amount = st.number_input(
        "Payment amount (₹)", min_value=0.0,
        value=500.0, step=50.0
    )

    bank_status = st.selectbox(
        "Bank or payment app status",
        ["Successful", "Pending", "Failed"]
    )

    portal_status = st.selectbox(
        "Utility portal status",
        ["Paid", "Unpaid", "Update Pending"]
    )

    if st.button("Check Payment", type="primary"):

        st.subheader("Payment Status Guidance")

        if bank_status == "Successful" and portal_status == "Paid":
            st.success(
                "Both statuses show success. Keep your payment receipt."
            )

        elif bank_status == "Successful":
            st.warning(
                "The bank shows success, but the portal does not show Paid. "
                "Keep the receipt, check the reference, and contact official "
                "support if needed. Avoid paying again immediately."
            )

        elif bank_status == "Pending":
            st.info(
                "The payment is pending. Check with your bank or payment app "
                "before attempting another payment."
            )

        else:
            st.warning(
                "The payment is marked failed. Verify its final status with "
                "your bank before trying again."
            )

        st.write(f"Reference: {reference or 'Not entered'}")
        st.write(f"Entered amount: ₹{amount:.2f}")

        st.caption("Demo only. No real transaction is verified.")

# ==========================================
# 7. OUTAGE REPORTING
# ==========================================

elif page == "Outage Reporting":

    st.header("⚡ Outage Reporting")

    st.write("Create a demonstration report for an electricity problem.")

    with st.form("outage_form"):

        area = st.text_input("Area or locality")

        issue_type = st.selectbox(
            "Type of issue",
            [
                "Power cut",
                "Low voltage",
                "Frequent power interruptions",
                "Other"
            ]
        )

        households = st.number_input(
            "Estimated households affected",
            min_value=1, value=25, step=1
        )

        details = st.text_area("Describe the problem")

        submit_outage = st.form_submit_button("Create Demo Report")

    if submit_outage:

        if not area.strip() or not details.strip():
            st.error("Please enter the area and describe the problem.")
        else:
            report_id = "OUTAGE-" + uuid4().hex[:8].upper()

            st.success("Demo outage report created!")

            st.subheader("Report Summary")
            st.write(f"**Reference:** {report_id}")
            st.write(f"**Area:** {area}")
            st.write(f"**Issue:** {issue_type}")
            st.write(f"**Households affected:** {households}")
            st.write(f"**Details:** {details}")

            st.info(
                "Demo only: this report has not been sent to an electricity provider."
            )

# ==========================================
# 8. TENANT SUPPORT
# ==========================================

elif page == "Tenant Support":

    st.header("🏠 Tenant Support")

    st.write("Create a sample complaint about a utility or accommodation issue.")

    with st.form("tenant_form"):

        tenant_name = st.text_input("Tenant name (demo)")
        location = st.text_input("Building or area")

        category = st.selectbox(
            "Complaint category",
            [
                "Electricity issue",
                "Water supply issue",
                "Billing dispute",
                "Maintenance request",
                "Payment issue",
                "Other"
            ]
        )

        priority = st.selectbox("Complaint priority", ["Low", "Medium", "High"])

        description = st.text_area("Complaint details")

        submit_tenant = st.form_submit_button("Submit Demo Complaint")

    if submit_tenant:

        if not tenant_name.strip() or not location.strip() or not description.strip():
            st.error("Please complete the name, location, and complaint details.")
        else:
            complaint_id = "TENANT-" + uuid4().hex[:8].upper()

            st.success("Demo complaint created!")

            st.subheader("Complaint Summary")
            st.write(f"**Reference:** {complaint_id}")
            st.write(f"**Tenant:** {tenant_name}")
            st.write(f"**Location:** {location}")
            st.write(f"**Category:** {category}")
            st.write(f"**Priority:** {priority}")
            st.write(f"**Description:** {description}")
            st.write("**Status:** Submitted in demo")

            if priority == "High":
                st.warning(
                    "High priority selected. A real service would need an escalation process."
                )
            elif priority == "Medium":
                st.info("Medium priority selected. Timely review is recommended.")
            else:
                st.info("Low priority selected. Normal review is recommended.")

            st.caption(
                "Demo only: this complaint is not saved permanently or sent to a real team."
            )

# ==========================================
# 9. PRIORITY CUSTOMER SUPPORT
# ==========================================

elif page == "Priority Customer Support":

    st.header("🚨 Priority Customer Support")

    st.write(
        "Evaluate a sample utility complaint and recommend "
        "which cases may need attention first."
    )

    st.info(
        "This prototype uses transparent rules, not AI or a real customer database."
    )

    with st.form("priority_support_form"):

        complaint_type = st.selectbox(
            "Complaint type",
            [
                "Electricity outage",
                "Water supply failure",
                "Billing problem",
                "Payment problem",
                "Routine maintenance",
                "Other"
            ]
        )

        severity = st.selectbox(
            "Impact on the customer",
            [
                "Critical: essential service unavailable",
                "High: major disruption",
                "Medium: service partly affected",
                "Low: minor or routine issue"
            ]
        )

        affected_people = st.number_input(
            "Estimated people affected",
            min_value=1,
            value=1,
            step=1
        )

        duration = st.selectbox(
            "How long has the issue continued?",
            [
                "Less than 1 hour",
                "1 to 6 hours",
                "6 to 24 hours",
                "More than 24 hours"
            ]
        )

        description = st.text_area(
            "Additional details",
            placeholder="Describe the issue briefly."
        )

        evaluate = st.form_submit_button(
            "Evaluate Priority",
            type="primary"
        )

    if evaluate:

        if not description.strip():
            st.error("Please provide a short description of the complaint.")

        else:
            # Transparent demonstration scoring rules
            score = 0

            if severity == "Critical: essential service unavailable":
                score += 5
            elif severity == "High: major disruption":
                score += 4
            elif severity == "Medium: service partly affected":
                score += 2
            else:
                score += 1

            if affected_people >= 50:
                score += 3
            elif affected_people >= 10:
                score += 2
            elif affected_people >= 2:
                score += 1

            if duration == "More than 24 hours":
                score += 3
            elif duration == "6 to 24 hours":
                score += 2
            elif duration == "1 to 6 hours":
                score += 1

            if score >= 8:
                result = "High"
                recommendation = (
                    "Recommend urgent human review. Check the scale of impact "
                    "and follow the provider's escalation process."
                )
            elif score >= 5:
                result = "Medium"
                recommendation = (
                    "Recommend timely review. Confirm the impact and arrange "
                    "follow-up according to service procedures."
                )
            else:
                result = "Low"
                recommendation = (
                    "Recommend normal review. Provide the customer with "
                    "the appropriate next steps."
                )

            priority_id = "PRIORITY-" + uuid4().hex[:8].upper()

            st.subheader("Priority Assessment")

            c1, c2 = st.columns(2)
            c1.metric("Demo Priority Score", f"{score}/11")
            c2.metric("Recommended Priority", result)

            st.write(f"**Reference:** {priority_id}")
            st.write(f"**Complaint type:** {complaint_type}")
            st.write(f"**People affected:** {affected_people}")
            st.write(f"**Duration:** {duration}")
            st.write(f"**Details:** {description}")

            if result == "High":
                st.error(recommendation)
            elif result == "Medium":
                st.warning(recommendation)
            else:
                st.success(recommendation)

            st.caption(
                "This score is a hackathon demonstration, not an official "
                "service-level policy. It does not determine actual entitlement "
                "or replace human review."
            )

# ==========================================
# 10. FOOTER
# ==========================================

st.divider()

st.caption(
    "UtilityCare | IMPACTX 2026 | Prototype using demonstration data. "
    "No real utility, payment, or complaint system is connected."
)