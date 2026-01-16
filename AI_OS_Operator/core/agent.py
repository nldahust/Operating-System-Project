import random
from collections import defaultdict

class RLAgent:
    def __init__(self, epsilon=0.2, alpha=0.1, gamma=0.9):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.actions = ["LOW_POWER", "BALANCED", "HIGH_PERFORMANCE"]
        self.q_table = defaultdict(float)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        return max(self.actions, key=lambda a: self.q_table[(state, a)])

    def update(self, state, action, reward):
        best_next = max(self.q_table[(state, a)] for a in self.actions)
        self.q_table[(state, action)] += self.alpha * (
            reward + self.gamma * best_next - self.q_table[(state, action)]
        )
