from IPython.display import display
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt

def dj_query(num_qubits):

    # Creates the Oracle which either gives a Constant function or Balanced function

    qc = QuantumCircuit(num_qubits + 1)

    if np.random.randint(0, 2):

        # Flip output qubit with 50% chance , Just for randomness
        qc.x(num_qubits)

    if np.random.randint(0, 2):
        # return constant circuit with 50% chance
        return qc

    # Choose half the possible input strings to create a balanced function , Outputs the numbers selected

    on_states = np.random.choice(range(2 ** num_qubits),2 ** num_qubits // 2,  replace=False)

#   Changes binary to qubit
    def add_cx(qc, bit_string):
        for qubit, bit in enumerate(reversed(bit_string)):
            if bit == "1":
                qc.x(qubit)
        return qc

    for state in on_states:
        qc.barrier()  # Barriers are added to help visualize how the functions are created.
        qc = add_cx(qc, f"{state:0b}") # Adds x gates to selected qubit
        qc.mcx(list(range(num_qubits)), num_qubits)
        qc = add_cx(qc, f"{state:0b}") # resets to original

    qc.barrier()

    return qc

display(dj_query(4).draw(output="mpl"))


def compile_circuit(function: QuantumCircuit):
    # Compiles a circuit for use in the Deutsch-Jozsa algorithm.

    n = function.num_qubits - 1
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)
    qc.h(range(n + 1))
    qc.compose(function, inplace=True)
    qc.h(range(n))
    qc.measure(range(n), range(n))
    return qc


def dj_algorithm(function: QuantumCircuit):
    # Determine if a function is constant or balanced.

    qc = compile_circuit(function)
    qc.draw(output="mpl")
    result = AerSimulator().run(qc, shots=1, memory=True).result()
    measurements = result.get_memory()
    if "1" in measurements[0]:
        return "balanced"
    return "constant"

f = dj_query(4)
display(f.draw("mpl"))
display(dj_algorithm(f))
plt.show()