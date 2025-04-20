from .gates import H, CNOT
from .register import QuantumRegister
from .utils import pretty_print_statevector, plot_state_vector, save_probabilities_to_file, sample_measurements, plot_bloch_sphere, extract_single_qubit_state

# Create a 2-qubit register
qr = QuantumRegister(2)

print("🌀 Initial State:")
pretty_print_statevector(qr.get_state())

# Apply Hadamard to qubit 0
qr.apply_single_qubit_gate(H, 0)

# Apply CNOT with qubit 0 as control and qubit 1 as target
qr.state = CNOT(qr.get_state(), control_qubit=0, target_qubit=1, num_qubits=qr.num_qubits)

print("\n⚛️ After CNOT (Bell state):")
pretty_print_statevector(qr.get_state())

# Visualize state vector
plot_state_vector(qr.get_state())

# Save probabilities to file
save_probabilities_to_file(qr.get_state(), filename="bell_probabilities.txt")

# Sampling measurements
samples = sample_measurements(qr.get_state(), num_samples=1000)
print("\n📊 Sampled Measurement Distribution (1000 shots):")
for state, prob in samples.items():
    print(f"{state}: {prob:.3f}")

# Plot Bloch spheres (for each qubit)
for i in range(qr.num_qubits):
    print(f"\n🧭 Bloch Sphere for Qubit {i}:")
    approx_single_qubit = extract_single_qubit_state(qr.get_state(), i, qr.num_qubits)
    plot_bloch_sphere(approx_single_qubit)

# Measure final state
result, probs = qr.measure()
print(f"\n🎯 Measurement Result: |{result:02b}>")

# Final collapsed state
print("\n📉 Collapsed State:")
pretty_print_statevector(qr.get_state())
