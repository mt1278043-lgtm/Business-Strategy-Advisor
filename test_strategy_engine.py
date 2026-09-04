"""
Unit tests for the Business Strategy Advisor Engine
"""

import pytest
from strategy_engine import validate_input, generate_strategy
import config


class TestValidateInput:
    """Test input validation functions."""

    def test_valid_input(self):
        """Test that valid input passes validation."""
        goals = "Expand market presence and increase revenue"
        threats = "Economic downturn and competitive pressure"
        trends = "AI adoption and digital transformation"

        # Should not raise any exception
        validate_input(goals, threats, trends)

    def test_empty_input(self):
        """Test that empty input raises ValueError."""
        with pytest.raises(ValueError, match="All input fields are required"):
            validate_input("", "threats", "trends")

        with pytest.raises(ValueError, match="All input fields are required"):
            validate_input("goals", "", "trends")

        with pytest.raises(ValueError, match="All input fields are required"):
            validate_input("goals", "threats", "")

    def test_none_input(self):
        """Test that None input raises ValueError."""
        with pytest.raises(ValueError):
            validate_input(None, "threats", "trends")

    def test_input_too_short(self):
        """Test that input below minimum length raises ValueError."""
        short_input = "a" * (config.MIN_INPUT_LENGTH - 1)
        with pytest.raises(ValueError, match="at least"):
            validate_input(short_input, "valid threat description here", "trends here")

    def test_input_too_long(self):
        """Test that input above maximum length raises ValueError."""
        long_input = "a" * (config.MAX_INPUT_LENGTH + 1)
        with pytest.raises(ValueError, match="must not exceed"):
            validate_input(long_input, "valid input", "valid input")

    def test_whitespace_only_input(self):
        """Test that whitespace-only input raises ValueError."""
        with pytest.raises(ValueError, match="at least"):
            validate_input("   ", "valid input", "valid input")


class TestGenerateStrategy:
    """Test strategy generation (requires API key)."""

    @pytest.mark.skip(reason="Requires OpenAI API key and costs money")
    def test_generate_strategy_valid_input(self):
        """Test strategy generation with valid input."""
        goals = "Expand into new markets"
        threats = "Increased competition"
        trends = "Market growth in emerging economies"

        result = generate_strategy(goals, threats, trends)

        assert isinstance(result, str)
        assert len(result) > 0
        assert "Strategic Priorities" in result or "Objective" in result

    def test_generate_strategy_invalid_input(self):
        """Test that invalid input raises appropriate errors."""
        # Test with empty input
        with pytest.raises(ValueError):
            generate_strategy("", "", "")

        # Test with input that's too short
        short_input = "short"
        with pytest.raises(ValueError):
            generate_strategy(short_input, short_input, short_input)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
