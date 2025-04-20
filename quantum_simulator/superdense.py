from .register import QuantumRegister
from .gates import X, Z, H, CNOT
from .utils import pretty_print_statevector, sample_measurements

def superdense_encode(qr, bits):
    if bits == "00":
        pass
    elif bits == "01":
        qr.apply_single_qubit_gate(X, 0)
    elif bits == "10":
        qr.apply_single_qubit_gate(Z, 0)
    elif bits == "11":
        qr.apply_single_qubit_gate(X, 0)
        qr.apply_single_qubit_gate(Z, 0)

def superdense_decode(qr):
    qr.apply_two_qubit_gate(CNOT, control=0, target=1)
    qr.apply_single_qubit_gate(H, 0)

def run_superdense(bits="10"):
    print("🧠 Superdense Coding Protocol")
    print(f"💾 Message to send: {bits}")

    qr = QuantumRegister(2)
    qr.apply_single_qubit_gate(H, 0)
    qr.apply_two_qubit_gate(CNOT, control=0, target=1)

    print("\n🔗 Bell State:")
    pretty_print_statevector(qr.get_state())

    superdense_encode(qr, bits)

    print("\n📤 After Alice's Encoding:")
    pretty_print_statevector(qr.get_state())

    superdense_decode(qr)

    print("\n📥 After Bob's Decoding:")
    pretty_print_statevector(qr.get_state())

    result, _ = qr.measure()
    print(f"\n🎯 Measured Bits: |{result:02b}> (Received '{result:02b}')")

    print("\n📊 Sampled Measurements (1000 shots):")
    samples = sample_measurements(qr.get_state(), 1000)
    for state, prob in samples.items():
        print(f"{state}: {prob:.3f}")

if __name__ == "__main__":
    run_superdense("11")
