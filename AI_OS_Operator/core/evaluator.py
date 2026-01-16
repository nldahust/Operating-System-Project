class Evaluator:
    def compute_reward(self, metrics, action):
        performance = 100 - metrics["cpu_load"]
        energy = metrics["power"]

        if action == "HIGH_PERFORMANCE":
            energy *= 1.3
        elif action == "LOW_POWER":
            energy *= 0.7

        return performance - 0.5 * energy
