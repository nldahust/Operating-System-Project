from core.evaluator import Evaluator

def test_reward_values():
    evaluator = Evaluator()
    metrics = {
        "cpu_load": 30,
        "power": 50
    }

    r_low = evaluator.compute_reward(metrics, "LOW_POWER")
    r_high = evaluator.compute_reward(metrics, "HIGH_PERFORMANCE")

    assert r_low > r_high
