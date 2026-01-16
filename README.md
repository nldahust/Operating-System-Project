# 🤖 AI-Based Self-Optimizing Operating System Simulator

A **Python-based operating system simulator** that applies **Reinforcement Learning (RL)** to autonomously optimize system configurations for **performance** and **energy efficiency**.

This project demonstrates how AI techniques can be integrated into operating system design using a **safe, user-space approach**, without modifying the kernel.

---

## 🚀 Features

- Reinforcement Learning (Q-learning) decision engine  
- Closed-loop self-optimizing control architecture  
- Modular OS-inspired design  
- Kernel-aware monitoring on macOS (via `sysctl`)  
- Energy vs performance trade-off optimization  
- Unit tests for core system modules  

---

## 🧠 How It Works

The system follows an autonomic control loop:

```
Monitor → State → Decide → Apply → Evaluate → Learn
```

At each step, the RL agent selects one of three operating system modes:

- **LOW_POWER** – prioritize energy efficiency  
- **BALANCED** – default trade-off  
- **HIGH_PERFORMANCE** – prioritize performance  

The agent improves its decisions over time using reward feedback.

---

## 🗂 Project Structure

```
ai_os_simulator/
│
├── core/
│   ├── monitor.py        # System monitoring
│   ├── state.py          # State processing
│   ├── agent.py          # RL agent (Q-learning)
│   ├── evaluator.py      # Reward function
│   └── config.py         # OS configuration logic
│
├── kernel/
│   └── macos_interface.py  # Kernel-aware metrics (macOS)
│
├── tests/                # Unit tests
├── main.py               # Main control loop
└── README.md
```

---

## 🖥 Kernel Interaction

- **macOS**: Reads real CPU load using `sysctl`
- **Linux (conceptual)**: Designed to work with `/proc` and `/sys`
- Configuration actions are **simulated** for safety

> No kernel modification is required.

---

## ▶️ Running the Simulator

Run the simulator from the project root:

```bash
python3 main.py
```

Example output:

```
Step 02 | Action=LOW_POWER | Reward=21.20 | Config={'cpu_freq': 'LOW', 'scheduler': 'POWER_SAVE', 'power_mode': 'SLEEP'}
```

---

## 🧪 Run Tests

Install `pytest` (only once):

```bash
pip install pytest
```

Run all unit tests:

```bash
python3 -m pytest tests/
```

---

## ⚠️ Limitations

- Simulation only (not a real OS kernel)
- Kernel configuration is restricted on macOS
- Lightweight RL model for educational purposes
- No real-time guarantees

---

---

