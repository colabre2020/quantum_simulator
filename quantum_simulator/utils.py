#  # Measurement & utility functions

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter

def get_probabilities(state_vector):
    """
    Calculate the probability of each basis state.
    """
    return np.abs(state_vector) ** 2

def measure_state(state_vector):
    """
    Simulate a quantum measurement on the state vector.
    Returns:
        - measurement result (0 or 1)
        - updated (collapsed) state vector
    """
    probabilities = get_probabilities(state_vector)
    result = np.random.choice([0, 1], p=probabilities)

    # Collapse the state
    collapsed_state = np.zeros_like(state_vector)
    collapsed_state[result] = 1.0
    return result, collapsed_state

def print_state(state_vector):
    """
    Print the quantum state in a readable format.
    """
    for i, amplitude in enumerate(state_vector):
        print(f"|{i}>: {amplitude:.4f} (prob: {abs(amplitude)**2:.2f})")

#  Visualize State Vector
def pretty_print_statevector(state_vector):
    n = int(np.log2(len(state_vector)))
    for i, amp in enumerate(state_vector):
        if np.abs(amp) > 1e-4:
            print(f"|{i:0{n}b}>: {amp:.4f} (|amp|^2 = {np.abs(amp)**2:.3f})")



def plot_state_vector(state_vector):
    n = int(np.log2(len(state_vector)))
    labels = [f"|{i:0{n}b}⟩" for i in range(len(state_vector))]
    probabilities = np.abs(state_vector) ** 2

    fig, ax = plt.subplots()
    bars = ax.bar(labels, probabilities, color='skyblue')
    ax.set_ylabel("Probability")
    ax.set_title("Quantum State Probabilities")
    ax.set_ylim(0, 1)

    for bar, prob in zip(bars, probabilities):
        height = bar.get_height()
        if prob > 0.01:
            ax.text(bar.get_x() + bar.get_width()/2.0, height,
                    f'{prob:.2f}', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    plt.show()


#  Bloch Sphere Visualization

def bloch_coordinates(state):
    alpha = state[0]
    beta = state[1]

    x = 2 * (alpha.conjugate() * beta).real
    y = 2 * (alpha.conjugate() * beta).imag
    z = abs(alpha)**2 - abs(beta)**2

    return x, y, z

def plot_bloch_sphere(state):
    x, y, z = bloch_coordinates(state)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Draw the sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.1)

    # Axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)

    # Bloch vector
    ax.quiver(0, 0, 0, x, y, z, color='black', linewidth=2)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_title("Bloch Sphere")
    plt.tight_layout()
    plt.show()


## Logging

def save_probabilities_to_file(state_vector, filename="probabilities.txt"):
    n = int(np.log2(len(state_vector)))
    with open(filename, "w") as f:
        for i, amp in enumerate(state_vector):
            prob = np.abs(amp) ** 2
            if prob > 1e-6:
                f.write(f"|{i:0{n}b}>: {prob:.6f}\n")



def sample_measurements(state_vector, num_samples=1000):
    probs = np.abs(state_vector) ** 2
    outcomes = np.random.choice(len(state_vector), size=num_samples, p=probs)
    counts = Counter(outcomes)
    total = sum(counts.values())
    
    result = {}
    n = int(np.log2(len(state_vector)))
    for outcome, count in sorted(counts.items()):
        result[f"|{outcome:0{n}b}>"] = count / total
    return result

def extract_single_qubit_state(full_state, target_qubit, num_qubits):
    """
    Approximate single-qubit state by marginalizing over other qubits.
    WARNING: This is a simplification — only valid if the qubit is not entangled.
    """
    size = 2 ** num_qubits
    amplitudes = [0j, 0j]  # For |0> and |1>

    for i in range(size):
        bit = (i >> (num_qubits - target_qubit - 1)) & 1
        amplitudes[bit] += full_state[i]

    norm = np.linalg.norm(amplitudes)
    return np.array(amplitudes) / norm if norm > 0 else np.array(amplitudes)
