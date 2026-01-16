import random
from kernel.kernel_interface import get_cpu_load

class SystemMonitor:
    def observe(self):
        cpu_load = get_cpu_load()

        return {
            "cpu_load": min(cpu_load * 30, 100),  # scale to %
            "memory_usage": random.uniform(30, 85),
            "io_activity": random.uniform(10, 80),
            "power": random.uniform(30, 100),
            "workload_intensity": (
                "HIGH" if cpu_load > 2.5 else
                "MEDIUM" if cpu_load > 1.2 else
                "LOW"
            )
        }
