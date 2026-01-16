class ConfigManager:
    def apply(self, action):
        if action == "LOW_POWER":
            return {
                "cpu_freq": "LOW",
                "scheduler": "POWER_SAVE",
                "power_mode": "SLEEP"
            }

        if action == "BALANCED":
            return {
                "cpu_freq": "MEDIUM",
                "scheduler": "DEFAULT",
                "power_mode": "NORMAL"
            }

        if action == "HIGH_PERFORMANCE":
            return {
                "cpu_freq": "HIGH",
                "scheduler": "PERFORMANCE",
                "power_mode": "TURBO"
            }
