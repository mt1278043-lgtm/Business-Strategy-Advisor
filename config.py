"""
Configuration settings for the Business Strategy Advisor Agent
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.3"))
OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "2000"))

# Application Configuration
APP_TITLE = "🧠 Business Strategy Advisor Agent"
APP_DESCRIPTION = "Input company goals and context. Get GPT-powered strategy suggestions."
APP_ICON = "🧠"

# Strategy Generation Prompts
STRATEGY_PROMPT_TEMPLATE = """
You are a Business Strategy Advisor AI with expertise in:
- Strategic planning and execution
- Market analysis and competitive positioning
- Organizational development and OKR frameworks
- Risk assessment and mitigation strategies

Based on the following input, provide a comprehensive strategy plan:

Company Goals: {goals}
External Threats: {threats}
Market Trends: {market_trends}

Provide your analysis in the following structure:

## 1. Strategic Priorities
List 3-5 key strategic priorities with brief descriptions.

## 2. SWOT Summary
- **Strengths**: List 3-4 internal strengths
- **Weaknesses**: List 3-4 internal weaknesses
- **Opportunities**: List 3-4 external opportunities
- **Threats**: List 3-4 external threats

## 3. Proposed OKRs
For each of 3 objectives:
- **Objective**: [Clear strategic objective]
  - **Key Result 1**: [Measurable outcome]
  - **Key Result 2**: [Measurable outcome]
  - **Key Result 3**: [Measurable outcome]

## 4. Implementation Roadmap
Provide a high-level timeline for implementation of key initiatives.

## 5. Success Metrics
Define 3-4 key metrics to track strategy execution.
"""

# UI Configuration
FORM_HEIGHT_GOALS = 100
FORM_HEIGHT_THREATS = 100
FORM_HEIGHT_TRENDS = 100

# File Configuration
DOWNLOAD_FILENAME = "strategy_report.txt"
DOWNLOAD_MIME_TYPE = "text/plain"

# Validation
MIN_INPUT_LENGTH = 10
MAX_INPUT_LENGTH = 5000

# Messages
ERROR_EMPTY_FIELDS = "Please fill in all three fields to generate a strategy."
ERROR_SHORT_INPUT = f"Please provide more detailed input (minimum {MIN_INPUT_LENGTH} characters)."
ERROR_GENERATION = "Error generating strategy: {error}"
MESSAGE_ANALYZING = "🔄 Analyzing your business context..."
MESSAGE_SUCCESS = "✅ Strategy generated successfully!"

# Feature Flags
ENABLE_DOWNLOAD = True
ENABLE_MARKDOWN = True
SHOW_ADVANCED_OPTIONS = os.getenv("SHOW_ADVANCED_OPTIONS", "false").lower() == "true"
