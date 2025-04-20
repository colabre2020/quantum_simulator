# Quantum Simulator

A simple quantum simulator built from scratch in Python. This project demonstrates foundational quantum computing concepts such as superdense coding and quantum teleportation, with support for basic gates, visualization, and state measurement.


## Features
- Simulate Bell states and entanglement.
- Implement Quantum Teleportation.
- Implement Superdense Coding.
- Visualize quantum states and Bloch spheres.
- Quantum Register abstraction
- Core quantum gates: Pauli, Hadamard, Rotation, CNOT
- Superdense Coding Protocol
- Quantum Teleportation Protocol
- State vector display & measurement sampling
- Bloch Sphere visualization
- State saving and plotting

## Project Structure

quantum_simulator/ ├── gates.py # Core quantum gates ├── register.py # Quantum register operations ├── teleportation.py # Quantum teleportation protocol ├── utils.py # Measurement, visualization, utilities └── superdense.py # Superdense coding protocol

## Installation
To install the package, clone the repository and install dependencies:

# bash''' Run the teleportation demo
python -m quantum_simulator.teleportation

# Run the superdense coding demo
python -m quantum_simulator.superdense

## Requirements
Python 3.7+
numpy
matplotlib

pip install numpy matplotlib


## Licenese

MIT --- see LICENSE


