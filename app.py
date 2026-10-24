import streamlit as st
from pathlib import Path
from uuid import uuid4

st.set_page_config(
    page_title="UtilityCare",
    page_icon="⚡",
    layout="wide"
)

# ---------- DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #071522, #102d40, #071522);
    color: #f4f8fb;
}
[data-testid="stSidebar"] {
    background: #081b2a;
}
h1, h2, h3 { color: #f4f8fb; }
[data-testid="stMetric"] {
    background: #102b3c;
    border: 1px solid #285064;
    padding: 16px;
    border-radius: 14px;
}
[data-testid="stMetricValue"] { color: #42dfcc; }
.stButton button, .stFormSubmitButton button {
    background: #38d6c3;
    color: #071522;
    border-radius: 9px;
    font-weight: bold;
    border: none;
}
.uc-card {
    background: #10283a;
    border: 1px solid #285064;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 12px;
}
.uc-label {
    color: #42dfcc;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)

# ---------- PICTURES ----------
# Optional: create utilitycare_assets beside app.py and add these files.
# If a local picture is missing, the app tries an online picture instead.
ASSETS = Path(__file__).resolve().parent / "utilitycare_assets"

PICTURES = {
    "Home Dashboard": (
        "home_dashboard.png",
        "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
    "Smart Bill Explainer": (
        "smart_bill_explainer.png",
        "https://images.unsplash.com/photo-1554224155-6726b3ff858f"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
    "Bill Reading Verification": (
        "bill_reading_verification.png",
        "https://images.unsplash.com/photo-1621905251918-48416bd8575a"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
    "Safe Payment Tracker": (
        "safe_payment_tracker.png",
        "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
    "Outage Reporting": (
        "outage_reporting.png",
        "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
    "Tenant Support": (
        "tenant_support.png",
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
    "Priority Customer Support": (
        "priority_customer_support.png",
        "https://images.unsplash.com/photo-1521737711867-e3b97375f902"
        "?auto=format&fit=crop&w=1200&q=80"
    ),
}

def show_picture(feature, width=None):
    filename, url = PICTURES[feature]
    local_file = ASSETS / filename

    if local_file.is_file():
        st.image(str(local_file), use_container_width=True)
    else:
        try:
            st.image(url, use_container_width=True)
        except Exception:
            st.info("Picture unavailable. The feature still works.")

def hero(number, title, subtitle):
    st.markdown(
        f'<p class="uc-label">UTILITYCARE / {number:02d}</p>'
        f'<h1>{title}</h1><p>{subtitle}</p>',
        unsafe_allow_html=True
    )
    st.divider()

def money(value):
    return f"₹{value:,.2f}"

# ---------- NAVIGATION ----------
PAGES = [
    "Home Dashboard",
    "Smart Bill Explainer",
    "Bill Reading Verification",
    "Safe Payment Tracker",
    "Outage Reporting",
    "Tenant Support",
    "Priority Customer Support"
]

with st.sidebar:
    st.markdown("# ⚡ UtilityCare")
    st.caption("UTILITIES THAT EXPLAIN THEMSELVES")
    st.divider()
    page = st.radio("Choose a feature", PAGES)
    st.divider()
    st.success("DEMO MODE")
    st.caption("No live bank or utility provider is connected.")
    st.caption("IMPACTX 2026 · Round 2")

st.markdown("## ⚡ UtilityCare")
st.caption("Understand bills. Verify readings. Get clearer next steps.")

# ---------- 1. HOME DASHBOARD ----------
if page == "Home Dashboard":
    hero(1, "Utilities, made clearer.",
         "Understand the numbers, check the details, and know what to do next.")

    show_picture(page)

    a, b, c = st.columns(3)
    a.metric("Core features", "7")
    b.metric("Live integrations", "0")
    c.metric("Transparent scoring", "Rule-based")

    st.subheader("Explore your workspace")

    descriptions = [
        ("🧾", "Smart Bill Explainer",
         "Understand charges, taxes and your estimated bill."),
        ("🔎", "Bill Reading Verification",
         "Compare meter readings against billed usage."),
        ("💳", "Safe Payment Tracker",
         "Understand payment status differences."),
        ("⚡", "Outage Reporting",
         "Prepare a clear electricity outage report."),
        ("🏠", "Tenant Support",
         "Organize utility complaints and requests."),
        ("🚦", "Priority Customer Support",
         "See how a transparent priority score is calculated.")
    ]

    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(descriptions):
        with cols[i % 3]:
            st.markdown(
                f'<div class="uc-card"><h3>{icon} {title}</h3>'
                f'<p>{desc}</p></div>',
                unsafe_allow_html=True
            )

    st.info("Demo only: reports are not sent to providers or permanently stored.")

# ---------- 2. SMART BILL EXPLAINER ----------
elif page == "Smart Bill Explainer":
    hero(2, page, "Understand each part of your electricity bill.")
    show_picture(page)

    left, right = st.columns(2)
    with left:
        units = st.number_input("Units used (kWh)", min_value=0.0, value=200.0)
        rate = st.number_input("Sample rate per unit (₹)", min_value=0.0, value=6.0)
        fixed = st.number_input("Fixed charges (₹)", min_value=0.0, value=100.0)
    with right:
        tax_rate = st.number_input("Sample tax (%)", min_value=0.0, value=5.0)
        dues = st.number_input("Previous dues (₹)", min_value=0.0, value=0.0)
        adjustment = st.number_input("Adjustment (₹)", value=0.0)
        usual = st.number_input("Usual bill (₹)", min_value=1.0, value=1000.0)

    reading = st.selectbox("Reading type", ["Actual", "Estimated", "Unknown"])

    if st.button("Explain my bill", type="primary"):
        energy = units * rate
        tax = (energy + fixed) * tax_rate / 100
        total = energy + fixed + tax + dues + adjustment

        if total < 0:
            st.error("The total is negative. Please check the adjustment.")
        else:
            st.subheader("Your bill breakdown")
            a, b, c = st.columns(3)
            a.metric("Energy charge", money(energy))
            b.metric("Tax estimate", money(tax))
            c.metric("Estimated total", money(total))

            st.write("| Charge | Amount |")
            st.write("|---|---:|")
            for label, amount in [
                ("Energy", energy), ("Fixed charges", fixed),
                ("Tax", tax), ("Previous dues", dues),
                ("Adjustment", adjustment)
            ]:
                st.write(f"| {label} | {money(amount)} |")

            st.write(
                f"You entered {units:g} units at a sample rate of "
                f"{money(rate)} per unit."
            )
            if total >= 2 * usual:
                st.warning("This estimate is at least twice your usual bill. Review the entries.")
            if reading == "Estimated":
                st.info("Check the bill against an actual meter reading if possible.")
            elif reading == "Unknown":
                st.info("Check your bill to confirm whether the reading was estimated.")
            if dues > 0:
                st.info("Confirm previous dues against earlier bills.")

            st.caption("Illustrative calculation, not an official tariff.")

# ---------- 3. BILL READING VERIFICATION ----------
elif page == "Bill Reading Verification":
    hero(3, page, "Compare meter usage with the units shown on your bill.")
    show_picture(page)

    a, b = st.columns(2)
    with a:
        previous = st.number_input("Previous reading", min_value=0.0, value=1200.0)
        current = st.number_input("Current reading", min_value=0.0, value=1800.0)
    with b:
        billed = st.number_input("Billed units", min_value=0.0, value=650.0)
        tolerance = st.number_input("Allowed difference", min_value=0.0, value=1.0)

    if st.button("Verify reading", type="primary"):
        if current < previous:
            st.error("Current reading is lower than previous reading. Check the entries.")
        else:
            usage = current - previous
            difference = abs(usage - billed)
            a, b, c = st.columns(3)
            a.metric("Calculated usage", f"{usage:.2f}")
            b.metric("Billed units", f"{billed:.2f}")
            c.metric("Difference", f"{difference:.2f}")

            if difference <= tolerance:
                st.success("Readings match within the selected tolerance.")
            else:
                st.warning("A difference was detected. Check dates, readings and meter multiplier.")
            st.caption("A difference does not automatically prove a billing error.")

# ---------- 4. SAFE PAYMENT TRACKER ----------
elif page == "Safe Payment Tracker":
    hero(4, page, "Check sample payment statuses before taking your next step.")
    show_picture(page)

    reference = st.text_input("Transaction reference", "TXN10025")
    amount = st.number_input("Payment amount (₹)", min_value=1.0, value=1500.0)
    a, b = st.columns(2)
    with a:
        bank = st.selectbox("Bank / payment app status",
                            ["Successful", "Pending", "Failed"])
    with b:
        portal = st.selectbox("Utility portal status",
                              ["Paid", "Unpaid", "Update Pending"])

    if st.button("Check payment status", type="primary"):
        a, b, c = st.columns(3)
        a.metric("Amount", money(amount))
        b.metric("Bank status", bank)
        c.metric("Portal status", portal)
        st.write(f"Reference: `{reference or 'Not entered'}`")

        if bank == "Successful" and portal == "Paid":
            st.success("Both sample statuses show payment success. Keep your receipt.")
        elif bank == "Successful":
            st.warning(
                "Bank shows success, but the portal does not. Keep your receipt, "
                "check with official support, and avoid paying again immediately."
            )
        elif bank == "Pending":
            st.info("Check the final status with your bank or payment app before retrying.")
        else:
            st.warning("Confirm the final status with your bank before attempting another payment.")

        st.caption("Demo statuses only. No real transaction is checked.")

# ---------- 5. OUTAGE REPORTING ----------
elif page == "Outage Reporting":
    hero(5, page, "Prepare a clear report about an electricity interruption.")
    show_picture(page)

    with st.form("outage_form"):
        area = st.text_input("Area or locality")
        issue = st.selectbox("Issue type", [
            "Power cut", "Low voltage",
            "Frequent interruptions", "Other"
        ])
        households = st.number_input(
            "Households affected", min_value=1, value=25
        )
        details = st.text_area("Describe the problem")
        submit = st.form_submit_button("Create demo report")

    if submit:
        if not area.strip() or not details.strip():
            st.error("Please enter the area and problem details.")
        else:
            report_id = "OUTAGE-" + uuid4().hex[:8].upper()
            st.success("Demo report prepared.")
            st.subheader(f"Reference: {report_id}")
            st.write(f"**Area:** {area}")
            st.write(f"**Issue:** {issue}")
            st.write(f"**Households affected:** {households}")
            st.write(f"**Details:** {details}")
            st.info("This report has not been sent to an electricity provider.")

# ---------- 6. TENANT SUPPORT ----------
elif page == "Tenant Support":
    hero(6, page, "Organize utility-related tenant concerns.")
    show_picture(page)

    with st.form("tenant_form"):
        name = st.text_input("Tenant name")
        location = st.text_input("Building or area")
        category = st.selectbox("Complaint category", [
            "Electricity issue", "Water supply issue", "Billing dispute",
            "Maintenance request", "Payment issue", "Other"
        ])
        priority = st.select_slider(
            "Requested priority",
            options=["Low", "Medium", "High"],
            value="Medium"
        )
        details = st.text_area("Complaint details")
        submit = st.form_submit_button("Prepare demo complaint")

    if submit:
        if not name.strip() or not location.strip() or not details.strip():
            st.error("Complete the name, location and complaint details.")
        else:
            complaint_id = "TENANT-" + uuid4().hex[:8].upper()
            st.success("Demo complaint prepared.")
            st.metric("Request reference", complaint_id)
            st.write(f"**Tenant:** {name}")
            st.write(f"**Location:** {location}")
            st.write(f"**Category:** {category}")
            st.write(f"**Priority:** {priority}")
            st.write(details)
            st.info("This complaint is not permanently saved or sent to a support team.")

# ---------- 7. PRIORITY CUSTOMER SUPPORT ----------
elif page == "Priority Customer Support":
    hero(7, page, "See how a transparent rule-based priority score works.")
    show_picture(page)

    st.info(
        "Demo scoring uses severity, people affected and duration. "
        "It is not a trained AI model or official provider policy."
    )

    with st.form("priority_form"):
        complaint_type = st.selectbox("Complaint type", [
            "Electricity outage", "Water supply failure",
            "Billing problem", "Payment problem",
            "Routine maintenance", "Other"
        ])
        severity = st.selectbox("Impact level", [
            "Critical", "High", "Medium", "Low"
        ])
        people = st.number_input("People affected", min_value=1, value=1)
        duration = st.selectbox("How long has it continued?", [
            "Less than 1 hour", "1 to 6 hours",
            "6 to 24 hours", "More than 24 hours"
        ])
        details = st.text_area("Describe the issue")
        submit = st.form_submit_button("Evaluate priority")

    if submit:
        if not details.strip():
            st.error("Please describe the issue.")
        else:
            severity_points = {
                "Critical": 5, "High": 4, "Medium": 2, "Low": 1
            }[severity]
            people_points = (
                3 if people >= 50 else
                2 if people >= 10 else
                1 if people >= 2 else 0
            )
            duration_points = {
                "Less than 1 hour": 0,
                "1 to 6 hours": 1,
                "6 to 24 hours": 2,
                "More than 24 hours": 3
            }[duration]

            score = severity_points + people_points + duration_points
            result = "High" if score >= 8 else "Medium" if score >= 5 else "Low"

            a, b = st.columns(2)
            a.metric("Rule-based score", f"{score}/11")
            b.metric("Suggested review priority", result)
            st.write(f"**Complaint type:** {complaint_type}")
            st.write(f"**Details:** {details}")
            st.markdown("### Why this score?")
            st.write(f"- Severity: {severity_points} points")
            st.write(f"- People affected: {people_points} points")
            st.write(f"- Duration: {duration_points} points")

            if result == "High":
                st.error("Recommend urgent human review.")
            elif result == "Medium":
                st.warning("Recommend timely review.")
            else:
                st.success("Recommend normal review.")

            st.caption("A demo score does not guarantee response time or replace human review.")

# ---------- FOOTER ----------
st.divider()
st.caption(
    "⚡ UtilityCare | Utilities That Explain Themselves | "
    "IMPACTX 2026 Prototype"
)
st.caption(
    "Demo environment: no live utility, bank or support integrations. "
    "Reports are not sent or permanently stored."
)