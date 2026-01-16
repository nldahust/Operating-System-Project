from core.agent import RLAgent

def test_agent_action():
    agent = RLAgent(epsilon=0.0)  # disable randomness
    state = (0.5, 0.5, 0.5, 0.5, 0.5)

    action = agent.select_action(state)

    assert action in ["LOW_POWER", "BALANCED", "HIGH_PERFORMANCE"]
