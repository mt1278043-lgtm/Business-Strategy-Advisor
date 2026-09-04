from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage


def generate_strategy(goals, threats, market_trends):
    """Generate a business strategy using GPT-4."""
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.3,
        max_tokens=2000
    )

    prompt = f"""
    You are a Business Strategy Advisor AI.
    Based on the following input, provide a comprehensive strategy plan:

    Company Goals: {goals}
    External Threats: {threats}
    Market Trends: {market_trends}

    Output a strategy in 3 sections:
    1. Strategic Priorities
    2. SWOT Summary (bullets)
    3. Proposed OKRs (3 objectives with key results)

    Format each section clearly with headers and bullet points where appropriate.
    """

    message = HumanMessage(content=prompt)
    response = llm.invoke([message])
    return response.content
