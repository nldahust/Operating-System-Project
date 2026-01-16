class StateProcessor:
    def process(self, metrics):
        workload_map = {
            "LOW": 0.0,
            "MEDIUM": 0.5,
            "HIGH": 1.0
        }

        return (
            metrics["cpu_load"] / 100.0,
            metrics["memory_usage"] / 100.0,
            metrics["io_activity"] / 100.0,
            metrics["power"] / 100.0,
            workload_map[metrics["workload_intensity"]]
        )
