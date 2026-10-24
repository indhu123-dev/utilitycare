import streamlit as st
from pathlib import Path
from uuid import uuid4
from datetime import datetime

st.set_page_config(
    page_title="UtilityCare | Smart Utility Companion",
    page_icon="⚡",
    layout="wide"
)

# ==================== PROFESSIONAL DESIGN ====================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: radial-gradient(circle at 85% 0%, #123a49 0, transparent 30%),
                linear-gradient(135deg, #06111d, #0b2333, #071522);
    color: #F4FAFF;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background: #071522;
    border-right: 1px solid #28768A;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

h1, h2, h3, h4 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

p, li, label {
    color: #EAF4FA;
    line-height: 1.6;
}

[data-testid="stCaptionContainer"] {
    color: #C4D9E5;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #123247, #0b2231);
    border: 1px solid #285064;
    padding: 16px;
    border-radius: 15px;
}

[data-testid="stMetricValue"] {
    color: #45E0CC !important;
    font-weight: 800;
}

[data-testid="stMetricLabel"] {
    color: #FFFFFF !important;
}

.stButton button,
.stFormSubmitButton button,
.stDownloadButton button {
    background: linear-gradient(90deg, #40E0C8, #8AF2DF);
    color: #06202B !important;
    border: 0;
    border-radius: 10px;
    font-weight: 800;
    min-height: 2.6rem;
}

.stButton button:hover,
.stFormSubmitButton button:hover,
.stDownloadButton button:hover {
    border: 1px solid #FFFFFF;
    filter: brightness(1.05);
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    color: #FFFFFF !important;
    background: #102C3D !important;
    border: 1px solid #477487 !important;
}

[data-baseweb="select"] > div {
    color: #FFFFFF !important;
    background: #102C3D !important;
}

[data-testid="stAlert"] {
    border-radius: 12px;
}

.uc-hero {
    background: linear-gradient(120deg, #12384B, #0A1E2D);
    border: 1px solid #33778A;
    border-radius: 22px;
    padding: 26px 28px;
    margin: 8px 0 22px;
}

.uc-hero h1 {
    color: #FFFFFF !important;
    font-size: clamp(2rem, 4vw, 3.1rem);
    margin: .2rem 0 .5rem;
}

.uc-hero p {
    color: #E4F1F7;
    margin: 0;
}

.uc-eyebrow {
    color: #56F0DE;
    font-size: .76rem;
    font-weight: 900;
    letter-spacing: .12em;
    text-transform: uppercase;
}

.uc-card {
    background: linear-gradient(145deg, #102C3D, #0B2030);
    border: 1px solid #326579;
    padding: 18px;
    border-radius: 16px;
    min-height: 145px;
    margin-bottom: 12px;
}

.uc-card h3 {
    font-size: 1.02rem;
    margin: .35rem 0 .55rem;
}

.uc-card p {
    color: #E2EFF7;
    font-size: .9rem;
}

.uc-pill {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 99px;
    background: #103C43;
    border: 1px solid #2C8B83;
    color: #8AFFF0;
    font-size: .75rem;
    font-weight: 900;
}

.uc-step {
    border-left: 3px solid #40E0C8;
    padding: 6px 0 6px 13px;
    margin: 9px 0;
}

@media (max-width: 768px) {
    .uc-hero {
        padding: 20px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==================== APP CONFIGURATION ====================

ASSETS = Path(__file__).resolve().parent / "utilitycare_assets"

PAGES = [
    "Home Dashboard",
    "Smart Bill Explainer",
    "Bill Reading Verification",
    "Safe Payment Tracker",
    "Outage Reporting",
    "Tenant Support",
    "Priority Customer Support"
]

INFO = {
    "Home Dashboard": (
        "🏠", "Utilities, made clearer.",
        "Understand bills, verify readings, and prepare support requests."
    ),
    "Smart Bill Explainer": (
        "🧾", "Your bill, explained.",
        "Break down sample charges into plain language."
    ),
    "Bill Reading Verification": (
        "🔎", "Check the numbers.",
        "Compare meter usage with the units shown on your bill."
    ),
    "Safe Payment Tracker": (
        "💳", "Know what your status means.",
        "Compare manually entered sample payment statuses."
    ),
    "Outage Reporting": (
        "⚡", "Prepare an outage report.",
        "Create a structured report you can download."
    ),
    "Tenant Support": (
        "🏠", "A clearer tenant support request.",
        "Prepare a utility-related complaint summary."
    ),
    "Priority Customer Support": (
        "🚦", "Make priority explainable.",
        "Inspect a transparent rule-based priority score."
    )
}

PICS = {
    "Home Dashboard": (
        "home_dashboard.png",
        "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=1400&q=80"
    ),
    "Smart Bill Explainer": (
        "smart_bill_explainer.png",
        "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=1200&q=80"
    ),
    "Bill Reading Verification": (
        "bill_reading_verification.png",
        "https://images.unsplash.com/photo-1621905251918-48416bd8575a?auto=format&fit=crop&w=1200&q=80"
    ),
    "Safe Payment Tracker": (
        "safe_payment_tracker.png",
        "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1200&q=80"
    ),
    "Outage Reporting": (
        "outage_reporting.png",
        "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=1200&q=80"
    ),
    "Tenant Support": (
        "tenant_support.png",
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80"
    ),
    "Priority Customer Support": (
        "priority_customer_support.png",
        "https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=1200&q=80"
    )
}

if "demo_reports" not in st.session_state:
    st.session_state.demo_reports = []


# ==================== HELPER FUNCTIONS ====================

def money(amount):
    return f"₹{amount:,.2f}"


def hero(number, title, subtitle):
    st.markdown(
        f"""
        <div class="uc-hero">
            <div class="uc-eyebrow">
                UTILITYCARE / {number:02d} · DEMO WORKSPACE
            </div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def picture(page):
    filename, url = PICS[page]
    local_file = ASSETS / filename
    source = str(local_file) if local_file.is_file() else url

    try:
        st.image(source, use_container_width=True)
    except Exception:
        st.info("Image preview unavailable; this feature is still usable.")


def card(icon, title, description):
    st.markdown(
        f"""
        <div class="uc-card">
            <div style="font-size:1.5rem">{icon}</div>
            <div class="uc-eyebrow">AVAILABLE</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def add_report(report_type, report_id):
    st.session_state.demo_reports.insert(
        0,
        {
            "type": report_type,
            "id": report_id,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    )


# ==================== SIDEBAR ====================

with st.sidebar:
    st.markdown("# ⚡ UtilityCare")
    st.caption("UTILITIES THAT EXPLAIN THEMSELVES")

    st.markdown(
        '<span class="uc-pill">IMPACTX 2026 · ROUND 2</span>',
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "YOUR WORKSPACE",
        PAGES,
        format_func=lambda p: f"{INFO[p][0]}  {p}"
    )

    st.divider()
    st.success("Demo mode active")
    st.caption("No live bank, utility, or support integration.")

    with st.expander(
        f"Session demo log ({len(st.session_state.demo_reports)})"
    ):
        for report in st.session_state.demo_reports[:5]:
            st.write(f"{report['type']} · {report['id']}")
            st.caption(report["created"])

        if st.session_state.demo_reports:
            if st.button("Clear session log"):
                st.session_state.demo_reports = []
                st.rerun()


# ==================== PAGE HEADER ====================

st.markdown("### ⚡ UtilityCare")
st.caption("Understand bills. Verify readings. Get clearer next steps.")


# ==================== 1. HOME DASHBOARD ====================

if page == "Home Dashboard":

    hero(1, *INFO[page][1:])

    left, right = st.columns([1.4, 1], gap="large")

    with left:
        picture(page)

    with right:
        st.markdown("#### Your utility toolkit")

        st.markdown("""
        <div class="uc-step">
            <b>01 · Understand</b><br>
            See how an estimated bill is calculated.
        </div>
        <div class="uc-step">
            <b>02 · Verify</b><br>
            Compare meter readings and billed units.
        </div>
        <div class="uc-step">
            <b>03 · Take action</b><br>
            Prepare structured demo support reports.
        </div>
        """, unsafe_allow_html=True)

    a, b, c, d = st.columns(4)
    a.metric("Core tools", "7", "Included")
    b.metric("Live integrations", "0", "Prototype mode")
    c.metric("Scoring logic", "Explainable", "Rule-based")
    d.metric(
        "Session reports",
        len(st.session_state.demo_reports),
        "Current session"
    )

    st.markdown("#### Explore your workspace")

    features = [
        ("🧾", "Smart Bill Explainer",
         "Understand energy, fixed charges, tax, and dues."),
        ("🔎", "Bill Reading Verification",
         "Compare readings and billed units."),
        ("💳", "Safe Payment Tracker",
         "Review sample bank and portal statuses."),
        ("⚡", "Outage Reporting",
         "Prepare an outage report."),
        ("🏠", "Tenant Support",
         "Prepare a utility-related tenant request."),
        ("🚦", "Priority Customer Support",
         "Understand the factors behind a priority score.")
    ]

    columns = st.columns(3)

    for index, feature in enumerate(features):
        with columns[index % 3]:
            card(*feature)

    st.info(
        "Demo reports are not sent to providers. "
        "They remain in this active session."
    )


# ==================== 2. SMART BILL EXPLAINER ====================

elif page == "Smart Bill Explainer":

    hero(2, *INFO[page][1:])
    picture(page)

    with st.container(border=True):
        left, right = st.columns(2)

        with left:
            units = st.number_input(
                "Units used (kWh)",
                min_value=0.0,
                value=200.0,
                step=10.0
            )

            rate = st.number_input(
                "Sample rate per unit (₹)",
                min_value=0.0,
                value=6.0,
                step=0.5
            )

            fixed = st.number_input(
                "Fixed charges (₹)",
                min_value=0.0,
                value=100.0,
                step=10.0
            )

        with right:
            tax_rate = st.number_input(
                "Sample tax (%)",
                min_value=0.0,
                value=5.0,
                step=0.5
            )

            dues = st.number_input(
                "Previous dues (₹)",
                min_value=0.0,
                value=0.0,
                step=50.0
            )

            adjustment = st.number_input(
                "Adjustment (₹)",
                value=0.0,
                step=10.0
            )

        usual = st.number_input(
            "Usual bill amount (₹)",
            min_value=1.0,
            value=1000.0,
            step=100.0
        )

        reading = st.selectbox(
            "Meter reading type",
            ["Actual", "Estimated", "Unknown"]
        )

        calculate = st.button(
            "Explain my bill",
            type="primary",
            use_container_width=True
        )

    if calculate:
        energy = units * rate
        tax = (energy + fixed) * tax_rate / 100
        total = energy + fixed + tax + dues + adjustment

        if total < 0:
            st.error(
                "Estimated total is negative. Review the adjustment."
            )
        else:
            st.markdown("#### Your estimated breakdown")

            a, b, c = st.columns(3)
            a.metric("Energy charge", money(energy))
            b.metric("Estimated tax", money(tax))
            c.metric("Estimated total", money(total))

            st.bar_chart(
                {
                    "Amount (₹)": [
                        energy,
                        fixed,
                        tax,
                        dues,
                        adjustment
                    ]
                },
                horizontal=True
            )

            rows = [
                {"Charge": name, "Amount": money(value)}
                for name, value in [
                    ("Energy", energy),
                    ("Fixed charges", fixed),
                    ("Tax estimate", tax),
                    ("Previous dues", dues),
                    ("Adjustment", adjustment)
                ]
            ]

            st.dataframe(
                rows,
                hide_index=True,
                use_container_width=True
            )

            st.write(
                f"You entered **{units:g} kWh** at a sample rate of "
                f"**{money(rate)} per unit**."
            )

            if total >= 2 * usual:
                st.warning(
                    "This estimate is at least twice your usual bill. "
                    "Recheck units, rate, dues, and adjustments."
                )
            elif total > 1.25 * usual:
                st.info(
                    "This estimate is over 25% above your usual bill. "
                    "Compare it with your actual bill."
                )
            else:
                st.success(
                    "The estimate is within 25% of your usual bill amount."
                )

            if reading == "Estimated":
                st.info(
                    "Compare an estimated reading with your meter "
                    "and your provider's explanation if possible."
                )
            elif reading == "Unknown":
                st.info(
                    "Check whether your bill uses an actual or estimated reading."
                )

            if dues > 0:
                st.info(
                    "Previous dues are included. Compare them with earlier bills."
                )

            st.caption(
                "Illustrative calculation only; actual rates and fees "
                "depend on your provider."
            )


# ==================== 3. BILL READING VERIFICATION ====================

elif page == "Bill Reading Verification":

    hero(3, *INFO[page][1:])
    picture(page)

    left, right = st.columns(2)

    with left:
        previous = st.number_input(
            "Previous reading",
            min_value=0.0,
            value=1200.0
        )

        current = st.number_input(
            "Current reading",
            min_value=0.0,
            value=1800.0
        )

    with right:
        billed = st.number_input(
            "Billed units",
            min_value=0.0,
            value=650.0
        )

        tolerance = st.number_input(
            "Allowed difference",
            min_value=0.0,
            value=1.0
        )

    if st.button(
        "Verify readings",
        type="primary",
        use_container_width=True
    ):
        if current < previous:
            st.error(
                "Current reading is lower than previous. "
                "Check dates and values."
            )
        else:
            usage = current - previous
            difference = abs(usage - billed)

            a, b, c = st.columns(3)
            a.metric("Calculated usage", f"{usage:.2f}")
            b.metric("Billed units", f"{billed:.2f}")
            c.metric("Difference", f"{difference:.2f}")

            st.bar_chart(
                {"Units": [usage, billed]},
                horizontal=True
            )

            if difference <= tolerance:
                st.success("Readings match within tolerance.")
            else:
                st.warning(
                    "Difference detected. Check reading dates, "
                    "meter multiplier, and estimated readings."
                )

            st.caption(
                "A mismatch is a prompt to investigate, "
                "not proof of a billing error."
            )


# END OF SECTION 1
# ==================== 4. SAFE PAYMENT TRACKER ====================

elif page == "Safe Payment Tracker":

    hero(4, *INFO[page][1:])
    picture(page)

    reference = st.text_input(
        "Transaction reference (sample)",
        "TXN10025"
    )

    amount = st.number_input(
        "Payment amount (₹)",
        min_value=0.0,
        value=1500.0
    )

    left, right = st.columns(2)

    with left:
        bank = st.selectbox(
            "Bank / payment app status",
            ["Successful", "Pending", "Failed"]
        )

    with right:
        portal = st.selectbox(
            "Utility portal status",
            ["Paid", "Unpaid", "Update Pending"]
        )

    if st.button(
        "Review payment status",
        type="primary",
        use_container_width=True
    ):
        a, b, c = st.columns(3)

        a.metric("Amount", money(amount))
        b.metric("Bank status", bank)
        c.metric("Portal status", portal)

        st.write(
            f"**Sample reference:** "
            f"`{reference.strip() or 'Not entered'}`"
        )

        if bank == "Successful" and portal == "Paid":
            st.success(
                "The entered statuses agree. Keep your receipt and "
                "verify the transaction through your official provider portal."
            )

        elif bank == "Successful":
            st.warning(
                "The bank status says successful, but the portal does not "
                "show paid. Check the official portal or contact your provider "
                "before attempting another payment."
            )

        elif bank == "Pending":
            st.info(
                "The transaction is marked pending. Check with your bank "
                "or payment app before retrying."
            )

        else:
            st.warning(
                "The bank status is marked failed. Confirm the final status "
                "with your bank or payment app before making another payment."
            )

        st.caption(
            "This is a manual demo review; no transaction is verified live."
        )

    if st.button("Save demo payment review"):
        report_id = f"PAY-{uuid4().hex[:8].upper()}"
        add_report("Payment review", report_id)
        st.success(f"Saved to session log: {report_id}")


# ==================== 5. OUTAGE REPORTING ====================

elif page == "Outage Reporting":

    hero(5, *INFO[page][1:])
    picture(page)

    st.markdown("#### Create an outage report")

    st.caption(
        "Prepare a report to download or submit through your provider's "
        "official support channel."
    )

    with st.form("outage_form"):

        col1, col2 = st.columns(2)

        with col1:
            outage_type = st.selectbox(
                "Utility affected",
                ["Electricity", "Water", "Gas", "Internet", "Other"]
            )

            outage_area = st.text_input(
                "Area / locality",
                placeholder="Enter your locality"
            )

            outage_since = st.text_input(
                "When did the outage start?",
                placeholder="e.g. Today around 6:30 PM"
            )

        with col2:
            outage_status = st.selectbox(
                "Current situation",
                [
                    "Completely unavailable",
                    "Intermittent service",
                    "Low supply / voltage",
                    "Unknown"
                ]
            )

            affected = st.selectbox(
                "People affected",
                [
                    "Only my property",
                    "Several properties",
                    "Entire area",
                    "Unknown"
                ]
            )

            urgency = st.selectbox(
                "Impact level",
                ["Routine", "High impact", "Urgent safety concern"]
            )

        outage_details = st.text_area(
            "Describe the issue",
            placeholder=(
                "Explain what happened and any relevant observations."
            )
        )

        outage_submit = st.form_submit_button(
            "Prepare outage report",
            type="primary",
            use_container_width=True
        )

    if outage_submit:

        report_id = f"OUT-{uuid4().hex[:8].upper()}"

        report_text = f"""UTILITYCARE — OUTAGE REPORT
Report ID: {report_id}
Prepared: {datetime.now().strftime("%Y-%m-%d %H:%M")}
Utility affected: {outage_type}
Area: {outage_area.strip() or "Not provided"}
Outage began: {outage_since.strip() or "Not provided"}
Current situation: {outage_status}
People affected: {affected}
Impact level: {urgency}

Issue description:
{outage_details.strip() or "No additional details provided."}

This report was prepared in UtilityCare demo mode.
It has NOT been sent to a utility provider.
"""

        st.success(f"Report prepared: {report_id}")

        st.text_area(
            "Review your report",
            value=report_text,
            height=300,
            key="outage_preview"
        )

        st.download_button(
            "Download outage report",
            data=report_text,
            file_name=f"{report_id}.txt",
            mime="text/plain",
            use_container_width=True
        )

        add_report("Outage report", report_id)

        if urgency == "Urgent safety concern":
            st.warning(
                "If there is immediate danger, stay away from hazardous "
                "equipment and contact the appropriate emergency service "
                "or utility emergency helpline."
            )

    else:
        st.info(
            "Your report is prepared in demo mode. "
            "It is not automatically sent to the provider."
        )


# ==================== 6. TENANT SUPPORT ====================

elif page == "Tenant Support":

    hero(6, *INFO[page][1:])
    picture(page)

    st.markdown("#### Prepare a utility-related tenant request")

    st.caption(
        "Create a clear summary to discuss with your landlord, "
        "property manager, or utility provider."
    )

    with st.form("tenant_form"):

        tenant_issue = st.selectbox(
            "Issue category",
            [
                "Unexpected utility charge",
                "Shared bill disagreement",
                "Meter access or reading",
                "Service interruption",
                "Account transfer",
                "Deposit or refund question",
                "Other"
            ]
        )

        property_type = st.selectbox(
            "Property type",
            [
                "Apartment",
                "Independent house",
                "Shared accommodation",
                "Other"
            ]
        )

        tenant_role = st.selectbox(
            "Your role",
            [
                "Tenant",
                "Property owner",
                "Housemate",
                "Authorized representative"
            ]
        )

        tenant_reference = st.text_input(
            "Bill or account reference (optional)",
            placeholder="Do not enter passwords or bank details"
        )

        tenant_summary = st.text_area(
            "Explain the issue",
            placeholder=(
                "Include relevant dates, bill amounts, readings, "
                "and steps already taken."
            )
        )

        desired_resolution = st.text_area(
            "What outcome are you requesting?",
            placeholder=(
                "e.g. An itemized bill explanation or meter recheck."
            )
        )

        tenant_submit = st.form_submit_button(
            "Prepare tenant request",
            type="primary",
            use_container_width=True
        )

    if tenant_submit:

        if not tenant_summary.strip():
            st.error(
                "Please describe the issue before preparing the request."
            )

        else:
            report_id = f"TEN-{uuid4().hex[:8].upper()}"

            tenant_report = f"""UTILITYCARE — TENANT SUPPORT REQUEST
Reference: {report_id}
Prepared: {datetime.now().strftime("%Y-%m-%d %H:%M")}
Issue category: {tenant_issue}
Property type: {property_type}
Role: {tenant_role}
Bill/account reference: {tenant_reference.strip() or "Not provided"}

Issue summary:
{tenant_summary.strip()}

Requested resolution:
{desired_resolution.strip() or "Please review and advise on next steps."}

This is a draft prepared in UtilityCare demo mode.
It has NOT been sent to a landlord, provider, or support team.
"""

            st.success(f"Tenant request prepared: {report_id}")

            st.text_area(
                "Review your request",
                value=tenant_report,
                height=300,
                key="tenant_preview"
            )

            st.download_button(
                "Download tenant request",
                data=tenant_report,
                file_name=f"{report_id}.txt",
                mime="text/plain",
                use_container_width=True
            )

            add_report("Tenant request", report_id)

            st.info(
                "Keep relevant bills, meter readings, and written "
                "communications as supporting records."
            )


# ==================== 7. PRIORITY CUSTOMER SUPPORT ====================

elif page == "Priority Customer Support":

    hero(7, *INFO[page][1:])
    picture(page)

    st.markdown("#### Transparent priority assessment")

    st.write(
        "This demonstration uses a visible, rule-based score to show how "
        "reported impact can influence a suggested support priority. "
        "It is not an official utility-provider decision."
    )

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:
            issue_severity = st.selectbox(
                "Issue severity",
                ["Low", "Moderate", "High", "Critical"]
            )

            people_affected = st.selectbox(
                "People affected",
                [
                    "One person",
                    "One household",
                    "Several households",
                    "Large area"
                ]
            )

        with col2:
            duration = st.selectbox(
                "Issue duration",
                [
                    "Under 1 hour",
                    "1–6 hours",
                    "6–24 hours",
                    "Over 24 hours"
                ]
            )

            vulnerable = st.selectbox(
                "Additional support consideration",
                [
                    "None reported",
                    "Person requiring essential powered equipment",
                    "Person with mobility or access needs",
                    "Other urgent support need"
                ]
            )

    if st.button(
        "Calculate demo priority",
        type="primary",
        use_container_width=True
    ):

        severity_points = {
            "Low": 5,
            "Moderate": 15,
            "High": 25,
            "Critical": 35
        }

        people_points = {
            "One person": 5,
            "One household": 10,
            "Several households": 20,
            "Large area": 30
        }

        duration_points = {
            "Under 1 hour": 0,
            "1–6 hours": 5,
            "6–24 hours": 10,
            "Over 24 hours": 15
        }

        support_points = {
            "None reported": 0,
            "Person requiring essential powered equipment": 20,
            "Person with mobility or access needs": 15,
            "Other urgent support need": 15
        }

        severity_score = severity_points[issue_severity]
        people_score = people_points[people_affected]
        duration_score = duration_points[duration]
        support_score = support_points[vulnerable]

        total_score = min(
            100,
            severity_score
            + people_score
            + duration_score
            + support_score
        )

        if (
            issue_severity == "Critical"
            or vulnerable != "None reported"
        ):
            priority = "Priority review recommended"

        elif total_score >= 60:
            priority = "High suggested priority"

        elif total_score >= 35:
            priority = "Moderate suggested priority"

        else:
            priority = "Routine suggested priority"

        a, b = st.columns(2)

        a.metric("Demo priority score", f"{total_score}/100")
        b.metric("Suggested category", priority)

        st.progress(total_score / 100)

        st.markdown("#### Score breakdown")

        breakdown = [
            {
                "Factor": "Issue severity",
                "Points": severity_score
            },
            {
                "Factor": "People affected",
                "Points": people_score
            },
            {
                "Factor": "Issue duration",
                "Points": duration_score
            },
            {
                "Factor": "Additional support consideration",
                "Points": support_score
            }
        ]

        st.dataframe(
            breakdown,
            hide_index=True,
            use_container_width=True
        )

        st.info(
            "This score is illustrative, not medically validated and not "
            "an official service-level agreement. A real service should use "
            "provider-approved policies and human review."
        )

        report_id = f"PRI-{uuid4().hex[:8].upper()}"

        priority_report = f"""UTILITYCARE — PRIORITY ASSESSMENT (DEMO)
Reference: {report_id}
Prepared: {datetime.now().strftime("%Y-%m-%d %H:%M")}
Severity: {issue_severity}
People affected: {people_affected}
Duration: {duration}
Additional support consideration: {vulnerable}
Demo score: {total_score}/100
Suggested category: {priority}

This score is illustrative and is not an official provider decision.
"""

        st.download_button(
            "Download priority assessment",
            data=priority_report,
            file_name=f"{report_id}.txt",
            mime="text/plain",
            use_container_width=True
        )

        if st.button("Save priority assessment to session log"):
            add_report("Priority assessment", report_id)
            st.success(f"Assessment saved: {report_id}")


# ==================== FOOTER ====================

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:12px 0 24px;">
        <div style="color:#56F0DE; font-weight:900; letter-spacing:.08em;">
            ⚡ UTILITYCARE
        </div>
        <div style="color:#D0E2EC; margin-top:6px;">
            Utilities That Explain Themselves
        </div>
        <div style="color:#A9C4D3; font-size:.8rem; margin-top:8px;">
            IMPACTX 2026 · Round 2 Prototype · Demo mode
        </div>
    </div>
    """,
    unsafe_allow_html=True
)