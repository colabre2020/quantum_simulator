# # Define quantum gates

import numpy as np

# Identity Gate
I = np.array([[1, 0],
              [0, 1]])

# Pauli-X Gate (NOT)
X = np.array([[0, 1],
              [1, 0]])

# Pauli-Y Gate
Y = np.array([[0, -1j],
              [1j, 0]])

# Pauli-Z Gate
Z = np.array([[1, 0],
              [0, -1]])

# Hadamard Gate
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])


# Phase Shift Gate (for any phase θ)
def phase(theta):
    return np.array([[1, 0],
                     [0, np.exp(1j * theta)]])

# Rotation-X
def rx(theta):
    return np.array([
        [np.cos(theta / 2), -1j * np.sin(theta / 2)],
        [-1j * np.sin(theta / 2), np.cos(theta / 2)]
    ])

# Rotation-Y
def ry(theta):
    return np.array([
        [np.cos(theta / 2), -np.sin(theta / 2)],
        [np.sin(theta / 2), np.cos(theta / 2)]
    ])

# Rotation-Z
def rz(theta):
    return np.array([
        [np.exp(-1j * theta / 2), 0],
        [0, np.exp(1j * theta / 2)]
    ])


# Controlled NOT (CNOT) Gate

def CNOT(state_vector, control_qubit, target_qubit, num_qubits):
    size = 2 ** num_qubits
    new_state = np.zeros_like(state_vector)
    for i in range(size):
        if (i >> (num_qubits - control_qubit - 1)) & 1:
            j = i ^ (1 << (num_qubits - target_qubit - 1))
            new_state[j] += state_vector[i]
        else:
            new_state[i] += state_vector[i]
    return new_state
