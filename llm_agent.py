import random
import matplotlib.pyplot as plt


class InventoryEnvironment:
    """
    Simulates a simple inventory system with stochastic demand.
    """

    def __init__(self, initial_inventory=100):
        self.inventory = initial_inventory
        self.history_inventory = []
        self.history_demand = []
        self.history_orders = []

    def generate_demand(self):
        # stochastic demand
        return random.randint(10, 30)

    def apply_demand(self, demand):
        self.inventory -= demand
        if self.inventory < 0:
            self.inventory = 0


class LLMLikeAgent:
    """
    Simulated LLM-based decision agent using structured reasoning.
    """

    def __init__(self):
        self.safety_threshold = 50
        self.order_amount = 100

    def act(self, inventory, demand):
        reasoning = []

        reasoning.append(f"Observed inventory: {inventory}")
        reasoning.append(f"Observed demand: {demand}")

        risk_level = 0.0

        if inventory < self.safety_threshold:
            reasoning.append("Inventory below safety threshold.")
            reasoning.append("High risk of stockout detected.")
            risk_level = 0.9
            decision = "ORDER"
        else:
            reasoning.append("Inventory level is stable.")
            reasoning.append("No immediate risk.")
            risk_level = 0.2
            decision = "HOLD"

        return decision, reasoning, risk_level


def run_simulation(days=20):
    env = InventoryEnvironment()
    agent = LLMLikeAgent()

    print("\n=== LLM-like Inventory Agent Simulation ===\n")

    for day in range(days):
        demand = env.generate_demand()
        env.apply_demand(demand)

        decision, reasoning, risk = agent.act(env.inventory, demand)

        if decision == "ORDER":
            env.inventory += agent.order_amount
            order = agent.order_amount
        else:
            order = 0

        env.history_inventory.append(env.inventory)
        env.history_demand.append(demand)
        env.history_orders.append(order)

        print(f"\nDAY {day+1}")
        print(f"Demand: {demand}")
        print(f"Inventory: {env.inventory}")
        print(f"Decision: {decision}")
        print(f"Risk score: {risk}")

        print("--- Reasoning ---")
        for r in reasoning:
            print(r)

    visualize(env)


def visualize(env):
    plt.figure(figsize=(10, 5))

    plt.plot(env.history_inventory, label="Inventory")
    plt.plot(env.history_demand, label="Demand")
    plt.plot(env.history_orders, label="Orders")

    plt.title("Inventory Simulation Results")
    plt.xlabel("Time (days)")
    plt.ylabel("Units")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    run_simulation(20)