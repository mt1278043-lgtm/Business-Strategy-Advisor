# Quick Start Guide

Get the Business Strategy Advisor Agent running in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/account/api-keys)
- Internet connection

## Installation (Choose One Method)

### Method 1: Using Setup Script (Recommended)

**On Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```bash
setup.bat
```

### Method 2: Manual Installation

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

### Method 3: Using Makefile

```bash
make setup
```

## Configuration

1. **Get an OpenAI API Key**
   - Visit https://platform.openai.com/account/api-keys
   - Create a new API key
   - Copy your key

2. **Add API Key to .env**
   ```bash
   # Edit .env file
   OPENAI_API_KEY=sk-your-api-key-here
   ```

## Running the App

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run Streamlit app
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Using the Application

### Step 1: Enter Company Goals
```
Example: "Expand into EMEA, reduce churn by 20%, improve NPS to 70"
```

### Step 2: Enter External Threats
```
Example: "Declining retention, inflation, competitor launches"
```

### Step 3: Enter Market Trends
```
Example: "AI adoption surge, remote work growth, data privacy focus"
```

### Step 4: Generate Strategy
Click "🚀 Generate Strategy" and wait for GPT-4 to analyze your business.

### Step 5: Review & Download
- Review the generated strategy report
- Download as a text file for sharing with your team

## Example Output

The system generates a comprehensive strategy including:

✅ **Strategic Priorities** - Key focus areas
✅ **SWOT Analysis** - Strengths, Weaknesses, Opportunities, Threats
✅ **OKRs** - Objectives and Key Results
✅ **Implementation Roadmap** - Timeline for execution
✅ **Success Metrics** - KPIs to track progress

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install -r requirements.txt
```

### "OPENAI_API_KEY not found"
Make sure `.env` file exists and contains your API key:
```bash
echo "OPENAI_API_KEY=sk-your-key" > .env
```

### "Connection error" or "API error"
1. Check your internet connection
2. Verify your API key is valid
3. Check OpenAI's status page: https://status.openai.com

### App won't start
```bash
# Reinstall Streamlit
pip install --upgrade streamlit

# Run with debug info
streamlit run app.py --logger.level=debug
```

## Advanced Configuration

Edit `config.py` to customize:

- `OPENAI_MODEL`: Change to "gpt-3.5-turbo" for cost savings
- `OPENAI_TEMPERATURE`: Adjust creativity (0.0-1.0)
- `OPENAI_MAX_TOKENS`: Limit response length
- `MIN_INPUT_LENGTH`: Minimum characters per field
- Feature flags and UI settings

Example:
```python
# Use GPT-3.5 instead of GPT-4 for faster/cheaper processing
OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_TEMPERATURE = 0.5  # More balanced responses
```

## Common Use Cases

### Market Entry Strategy
```
Goals: "Enter Japan market with local partnerships"
Threats: "Language barriers, regulatory requirements"
Trends: "Growing Asia-Pacific AI adoption"
```

### Cost Optimization
```
Goals: "Reduce cloud costs by 20%, maintain service level"
Threats: "Rising infrastructure costs, talent shortage"
Trends: "Cost optimization tool maturity, open-source growth"
```

### Product Pivot
```
Goals: "Shift to AI-first product, expand to enterprises"
Threats: "Market saturation, regulatory uncertainty"
Trends: "Enterprise AI adoption, regulatory momentum"
```

## Getting Help

- 📖 See [README.md](README.md) for full documentation
- 🤝 See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- 🐛 Open an issue on GitHub for bugs
- 💬 Check examples in [example_usage.py](example_usage.py)

## Next Steps

1. ✅ Run your first strategy analysis
2. 📥 Download and share the report with your team
3. 🔄 Iterate on different scenarios
4. 📊 Compare multiple strategies
5. 🚀 Execute your strategic plan

---

Happy strategizing! 🎯
