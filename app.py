import streamlit as st
import logging
from strategy_engine import generate_strategy
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout="wide"
)

st.title(config.APP_TITLE + " Agent")
st.caption(config.APP_DESCRIPTION)

# Initialize session state for storing results
if "strategy_output" not in st.session_state:
    st.session_state.strategy_output = None

with st.form("strategy_form"):
    col1, col2 = st.columns(2)

    with col1:
        goals = st.text_area(
            "🎯 Company Goals",
            placeholder="e.g., Expand into EMEA, reduce churn by 20%, improve NPS",
            height=config.FORM_HEIGHT_GOALS
        )

    with col2:
        threats = st.text_area(
            "⚠️ External Risks / Threats",
            placeholder="e.g., Competitor X release, economic downturn",
            height=config.FORM_HEIGHT_THREATS
        )

    trends = st.text_area(
        "📈 Market Trends",
        placeholder="e.g., Surge in AI adoption, remote work trends, industry shifts",
        height=config.FORM_HEIGHT_TRENDS
    )

    submitted = st.form_submit_button("🚀 Generate Strategy", use_container_width=True)

if submitted:
    if not all([goals.strip(), threats.strip(), trends.strip()]):
        st.error(config.ERROR_EMPTY_FIELDS)
    else:
        with st.spinner(config.MESSAGE_ANALYZING):
            try:
                output = generate_strategy(goals, threats, trends)
                st.session_state.strategy_output = output
                st.success(config.MESSAGE_SUCCESS)
                logger.info("Strategy generated and displayed to user.")
            except ValueError as e:
                st.error(str(e))
                logger.error(f"Validation error: {str(e)}")
            except Exception as e:
                error_msg = config.ERROR_GENERATION.format(error=str(e))
                st.error(error_msg)
                logger.error(f"Strategy generation error: {str(e)}")

if st.session_state.strategy_output:
    st.subheader("📊 Strategy Report")

    if config.ENABLE_MARKDOWN:
        st.markdown(st.session_state.strategy_output)
    else:
        st.text(st.session_state.strategy_output)

    # Download button for the strategy report
    if config.ENABLE_DOWNLOAD:
        col1, col2 = st.columns([3, 1])
        with col2:
            st.download_button(
                label="📥 Download Report",
                data=st.session_state.strategy_output,
                file_name=config.DOWNLOAD_FILENAME,
                mime=config.DOWNLOAD_MIME_TYPE
            )
