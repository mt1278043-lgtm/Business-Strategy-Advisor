# Contributing to Business Strategy Advisor

Thank you for your interest in contributing to the Business Strategy Advisor Agent! This document provides guidelines and instructions for contributing.

## Getting Started

### 1. Fork and Clone the Repository
```bash
git clone https://github.com/your-username/Business-Strategy-Advisor.git
cd Business-Strategy-Advisor
```

### 2. Set Up Development Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and concise

### Commit Messages
- Write clear, descriptive commit messages
- Use present tense ("Add feature" not "Added feature")
- Reference issues when applicable: "Fix #123"

### Testing
- Test your changes locally before submitting
- Ensure the Streamlit app runs without errors
- Test with different input scenarios

## Submission Process

### Before Submitting

1. **Update Documentation**
   - Update README.md if adding new features
   - Add docstrings to new functions
   - Update CHANGELOG.md

2. **Test Your Changes**
   ```bash
   streamlit run app.py
   ```

3. **Check Code Quality**
   ```bash
   make lint
   make format
   ```

### Creating a Pull Request

1. Push your changes to your fork
2. Create a pull request to the main repository
3. Provide a clear description of:
   - What problem does it solve?
   - How does it work?
   - Any breaking changes?
   - Screenshots or examples (if applicable)

## Feature Ideas

We welcome contributions in these areas:

- **Enhanced Analysis**: Better SWOT analysis, industry-specific strategies
- **Data Integration**: Connect to financial APIs, market data providers
- **Visualization**: Charts, dashboards, visual reports
- **Export Options**: PDF, PowerPoint, Excel exports
- **Localization**: Multi-language support
- **Performance**: Caching, optimization improvements
- **Testing**: Unit tests, integration tests

## Reporting Bugs

Found a bug? Please create an issue with:

1. Clear description of the problem
2. Steps to reproduce
3. Expected vs actual behavior
4. Screenshots if applicable
5. Environment details (OS, Python version, etc.)

## Questions or Suggestions?

Feel free to open an issue to discuss ideas, ask questions, or suggest improvements.

## Code of Conduct

Please be respectful and constructive in all interactions. We're committed to providing a welcoming and inclusive environment for all contributors.

---

Thank you for contributing to make Business Strategy Advisor better! 🚀
