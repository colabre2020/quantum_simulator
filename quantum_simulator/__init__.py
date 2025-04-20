# __init__.py to initialize your package
from .gates import *
from .register import QuantumRegister
from .utils import *
from .teleportation import teleport
from .superdense import run_superdense
__all__ = [
    "QuantumRegister",
    "teleport",
    "run_superdense",
    "H",
    "X",
    "Z",
    "CNOT",
    "pretty_print_statevector",
    "sample_measurements"
]
__version__ = "0.1.0"
__author__ = "Satya Panda"
__email__ = "spanda202020@gmail.com"
__description__ = "A simple quantum simulator for educational purposes."
__license__ = "MIT"