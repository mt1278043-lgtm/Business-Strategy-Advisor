import streamlit as st
from strategy_engine import generate_strategy

st.set_page_config(
    page_title="Business Strategy Advisor",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Business Strategy Advisor Agent")
st.caption("Input company goals and context. Get GPT-powered strategy suggestions.")

# Initialize session state for storing results
if "strategy_output" not in st.session_state:
    st.session_state.strategy_output = None

with st.form("strategy_form"):
    col1, col2 = st.columns(2)

    with col1:
        goals = st.text_area(
            "🎯 Company Goals",
            placeholder="e.g., Expand into EMEA, reduce churn by 20%, improve NPS",
            height=100
        )

    with col2:
        threats = st.text_area(
            "⚠️ External Risks / Threats",
            placeholder="e.g., Competitor X release, economic downturn",
            height=100
        )

    trends = st.text_area(
        "📈 Market Trends",
        placeholder="e.g., Surge in AI adoption, remote work trends, industry shifts",
        height=100
    )

    submitted = st.form_submit_button("🚀 Generate Strategy", use_container_width=True)

if submitted:
    if not goals or not threats or not trends:
        st.error("Please fill in all three fields to generate a strategy.")
    else:
        with st.spinner("🔄 Analyzing your business context..."):
            try:
                output = generate_strategy(goals, threats, trends)
                st.session_state.strategy_output = output
            except Exception as e:
                st.error(f"Error generating strategy: {str(e)}")

if st.session_state.strategy_output:
    st.subheader("📊 Strategy Report")
    st.markdown(st.session_state.strategy_output)

    # Download button for the strategy report
    col1, col2 = st.columns([3, 1])
    with col2:
        st.download_button(
            label="📥 Download Report",
            data=st.session_state.strategy_output,
            file_name="strategy_report.txt",
            mime="text/plain"
        )
