import numpy as np
from .utils import get_probabilities

class QuantumRegister:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1.0  # |00...0⟩

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state

    def apply_single_qubit_gate(self, gate, target):
        I = np.eye(2)
        gate_full = 1
        for i in range(self.num_qubits):
            gate_full = np.kron(gate_full, gate if i == target else I)
        self.state = gate_full @ self.state

    def apply_two_qubit_gate(self, gate_func, control, target):
        new_state = gate_func(self.state, control, target, self.num_qubits)
        self.set_state(new_state)

    def measure_qubit(self, qubit_index):
        n = self.num_qubits
        probs = np.abs(self.state)**2
        outcome_probs = [0.0, 0.0]
        for i in range(2**n):
            bit = (i >> (n - qubit_index - 1)) & 1
            outcome_probs[bit] += probs[i]
        result = np.random.choice([0, 1], p=outcome_probs)
        for i in range(2**n):
            bit = (i >> (n - qubit_index - 1)) & 1
            if bit != result:
                self.state[i] = 0
        self.state = self.state / np.linalg.norm(self.state)
        return result, self.state

    def measure(self):
        probabilities = get_probabilities(self.state)
        result = np.random.choice(len(self.state), p=probabilities)
        collapsed = np.zeros_like(self.state)
        collapsed[result] = 1.0
        self.state = collapsed
        return result, probabilities
