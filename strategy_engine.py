import logging
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def validate_input(goals, threats, market_trends):
    """Validate input parameters."""
    if not all([goals, threats, market_trends]):
        raise ValueError("All input fields are required.")

    if any(len(field.strip()) < config.MIN_INPUT_LENGTH for field in [goals, threats, market_trends]):
        raise ValueError(f"Each field must be at least {config.MIN_INPUT_LENGTH} characters long.")

    if any(len(field) > config.MAX_INPUT_LENGTH for field in [goals, threats, market_trends]):
        raise ValueError(f"Each field must not exceed {config.MAX_INPUT_LENGTH} characters.")


def generate_strategy(goals, threats, market_trends):
    """Generate a business strategy using GPT-4.

    Args:
        goals: Company strategic goals
        threats: External threats and risks
        market_trends: Market trends and opportunities

    Returns:
        str: Generated strategy report

    Raises:
        ValueError: If input validation fails
        Exception: If API call fails
    """
    try:
        validate_input(goals, threats, market_trends)
        logger.info("Input validation passed.")

        llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model=config.OPENAI_MODEL,
            temperature=config.OPENAI_TEMPERATURE,
            max_tokens=config.OPENAI_MAX_TOKENS
        )

        prompt = config.STRATEGY_PROMPT_TEMPLATE.format(
            goals=goals,
            threats=threats,
            market_trends=market_trends
        )

        logger.info("Sending request to OpenAI API...")
        message = HumanMessage(content=prompt)
        response = llm.invoke([message])
        logger.info("Strategy generated successfully.")
        return response.content

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Error generating strategy: {str(e)}")
        raise
