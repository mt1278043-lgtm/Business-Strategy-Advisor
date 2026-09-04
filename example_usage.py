#!/usr/bin/env python3
"""
Example usage of the Business Strategy Advisor Engine

This script demonstrates how to use the strategy_engine module
to generate business strategies programmatically.
"""

from strategy_engine import generate_strategy


def main():
    # Example 1: SaaS Expansion Strategy
    print("=" * 80)
    print("EXAMPLE 1: SaaS Product Expansion Strategy")
    print("=" * 80)

    goals = "Enter APAC market, reduce churn by 20%, improve NPS to 70"
    threats = "Declining retention, inflation in key markets, competitor product launches"
    trends = "Surge in AI adoption, growth of remote work, increasing focus on data privacy"

    print(f"\nGoals: {goals}")
    print(f"Threats: {threats}")
    print(f"Trends: {trends}\n")

    print("Generating strategy...")
    strategy = generate_strategy(goals, threats, trends)
    print(strategy)

    # Example 2: Cost Optimization Strategy
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Cost Optimization Strategy")
    print("=" * 80)

    goals = "Reduce operational expenses by 15%, maintain service quality, expand engineering team"
    threats = "Rising cloud costs, talent acquisition challenges, economic uncertainty"
    trends = "Auto-scaling technology maturity, open-source tool adoption, edge computing"

    print(f"\nGoals: {goals}")
    print(f"Threats: {threats}")
    print(f"Trends: {trends}\n")

    print("Generating strategy...")
    strategy = generate_strategy(goals, threats, trends)
    print(strategy)


if __name__ == "__main__":
    main()
