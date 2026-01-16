from core.monitor import SystemMonitor

def test_monitor_output():
    monitor = SystemMonitor()
    metrics = monitor.observe()

    assert 0 <= metrics["cpu_load"] <= 100
    assert 0 <= metrics["memory_usage"] <= 100
    assert metrics["workload_intensity"] in ["LOW", "MEDIUM", "HIGH"]
