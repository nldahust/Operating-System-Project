from core.monitor import SystemMonitor
from core.state import StateProcessor
from core.agent import RLAgent
from core.config import ConfigManager
from core.evaluator import Evaluator
import time

monitor = SystemMonitor()
processor = StateProcessor()
agent = RLAgent()
config = ConfigManager()
evaluator = Evaluator()

print("AI-Based Self-Optimizing OS Simulator\n")

for step in range(60):
    metrics = monitor.observe()
    state = processor.process(metrics)
    action = agent.select_action(state)
    applied_config = config.apply(action)
    reward = evaluator.compute_reward(metrics, action)
    agent.update(state, action, reward)

    print(
        f"Step {step:02d} | "
        f"Action={action:<16} | "
        f"Reward={reward:7.2f} | "
        f"Config={applied_config}"
    )

    time.sleep(0.3)
