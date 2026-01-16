from core.state import StateProcessor

def test_state_normalization():
    processor = StateProcessor()
    metrics = {
        "cpu_load": 50,
        "memory_usage": 50,
        "io_activity": 50,
        "power": 50,
        "workload_intensity": "MEDIUM"
    }

    state = processor.process(metrics)

    for value in state:
        assert 0.0 <= value <= 1.0
