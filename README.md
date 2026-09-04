# 🧠 Business Strategy Advisor Agent

A GPT-powered business strategy advisor that helps executives and product leaders analyze business data, interpret market trends, and generate strategic insights.

## Features

- 📊 **Strategic Analysis**: Analyze internal goals and external context
- 🎯 **OKR Generation**: Automatically generate Objectives and Key Results
- 📈 **SWOT Assessment**: Simulate comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis
- 💼 **Executive Summary**: Present results in a clear, executive-style format
- 📥 **Report Download**: Export strategy reports as text files

## Tech Stack

- **Python 3.8+**
- **Streamlit** - Web UI framework
- **LangChain** - LLM orchestration
- **OpenAI GPT-4** - Strategy generation engine
- **python-dotenv** - Environment variable management

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Business-Strategy-Advisor
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure OpenAI API Key

Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-api-key-here
```

## Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Usage

1. **Enter Company Goals**: Describe your strategic objectives
   - Example: "Expand into EMEA, reduce churn by 20%, improve NPS"

2. **Enter External Risks/Threats**: Identify potential challenges
   - Example: "Competitor X release, economic downturn, market saturation"

3. **Enter Market Trends**: Describe relevant market movements
   - Example: "Surge in AI adoption, remote work normalization"

4. **Generate Strategy**: Click "Generate Strategy" to get GPT-powered recommendations

5. **Review & Download**: Review the strategy report and download as needed

## Example Output

### Strategic Priorities
- Enter APAC market via low-cost SaaS tier
- Implement automation in support and finance
- Redesign retention funnel via personalization

### SWOT Summary
- **Strengths**: Scalable tech, agile team
- **Weaknesses**: High customer acquisition cost
- **Opportunities**: AI expansion, Asia-Pacific demand growth
- **Threats**: Retention risks, market saturation

### OKRs
- **Objective**: Expand APAC footprint
  - KR1: Localize platform in 3 languages
  - KR2: Acquire 5 regional partners
  
- **Objective**: Reduce operational expenses
  - KR1: Automate 3 back-office workflows
  - KR2: Reduce monthly SaaS cost by 10%

## Project Structure

```
Business-Strategy-Advisor/
├── app.py                 # Streamlit application
├── strategy_engine.py     # LangChain strategy generation logic
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Requirements

- Python 3.8 or higher
- OpenAI API key with GPT-4 access
- Internet connection for API calls

## Troubleshooting

### ImportError: No module named 'openai'
Make sure you've installed all requirements:
```bash
pip install -r requirements.txt
```

### OPENAI_API_KEY not found
Ensure your `.env` file exists and contains a valid API key:
```bash
echo "OPENAI_API_KEY=sk-your-key" > .env
```

### Streamlit not found
Install Streamlit:
```bash
pip install streamlit==1.28.1
```

## API Costs

This application uses OpenAI's GPT-4 API, which incurs costs per token. Monitor your API usage at https://platform.openai.com/account/usage/overview

## Future Enhancements

- Integration with financial APIs for market data
- Competitor analysis datasets
- Business Intelligence tool integration
- Advanced SWOT matrix visualization
- Custom strategy templates
- Multi-language support
- Export to PowerPoint/PDF

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License.

## Support

For issues or questions, please open an issue in the repository.
