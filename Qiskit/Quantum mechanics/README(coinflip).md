# 🪙 Quantum Coin Flip Experiments (Qiskit + AerSimulator)

This repository contains small quantum computing experiments in **Qiskit** to simulate coin flips using single-qubit circuits.  
The experiments use the **AerSimulator** backend and Qiskit’s new primitives (`BackendSamplerV2` and `BackendEstimatorV2`) to estimate outcomes and expectation values.

---

## 📌 Setup

Make sure you have Qiskit installed with Aer support:

📂 Experiments Included
1. Single Quantum Coin Flip

Creates a 1-qubit circuit.

Applies a Hadamard gate to put the qubit into equal superposition.

Measures the state, producing outcomes 0 or 1 with equal probability.

qcoin_0 = QuantumCircuit(1)
qcoin_0.h(0)
qcoin_0.measure_all()


🔍 Output: A histogram showing ~50% chance for 0 and 1.

2. Double Quantum Coin Flip

Applies two Hadamard gates in sequence.

Since two Hadamards cancel out, the state returns to |0⟩.

qcoin_0 = QuantumCircuit(1)
qcoin_0.h(0)
qcoin_0.h(0)
qcoin_0.measure_all()


🔍 Output: Histogram shows 100% probability for 0.

3. Measuring in Different Bases (X, Y, Z)

Uses the SX gate (√X) on a qubit.

Then measures expectation values ⟨X⟩, ⟨Y⟩, ⟨Z⟩ using BackendEstimatorV2 and the Pauli operators.

qcoin_sx = QuantumCircuit(1)
qcoin_sx.sx(0)

obs1 = Pauli("X")
obs2 = Pauli("Y")
obs3 = Pauli("Z")

pubs = [(qcoin_sx, [obs1, obs2, obs3])]
job = estimator_sim.run(pubs)
res = job.result()
print(res[0].data.evs)


🔍 Output: Expectation values representing the Bloch vector of the state.

📊 Results

Histograms show probability distributions of measurement outcomes.

Expectation values (.data.evs) reveal geometric representation on the Bloch sphere.
