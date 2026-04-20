# LLM-like Inventory Decision Agent (Research Prototype)

## Overview

This project simulates an intelligent inventory management system using an LLM-inspired decision-making agent.

The agent operates in a simplified supply chain environment, where it observes system state, performs structured reasoning, and makes autonomous decisions about inventory replenishment.

---

## Key Idea

The system follows an **agentic workflow**:

1. Observation (inventory, demand)
2. Reasoning (structured decision logic inspired by LLM thinking)
3. Decision (order / hold)
4. Execution (inventory update)

---

## Features

- Stochastic demand simulation
- Autonomous decision-making agent
- LLM-like reasoning process (Chain-of-Thought style structure)
- Risk scoring mechanism
- Visualization of system behavior over time

---

## Scientific Motivation

The project is inspired by research in:

- Large Language Model agents (LLMs)
- Agent-Based Modeling (ABM)
- Intelligent decision systems in supply chains
- Digital twin simulation environments

It serves as a simplified prototype of how LLM-based agents can be integrated into operational decision-making systems.

---

## Output

The simulation provides:

- Inventory level over time
- Demand fluctuations
- Order actions
- Risk evaluation of decisions

---

## Technologies

- Python
- matplotlib
- random

---

## Future Improvements

- Integration with real LLM API (GPT-based reasoning)
- Multi-agent system (supplier + warehouse + customer)
- Reinforcement learning for optimal policy learning
- Integration with full supply chain digital twin
