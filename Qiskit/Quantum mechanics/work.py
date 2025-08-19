from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qcoin_0 = QuantumCircuit(1)
qcoin_0.h(0)
qcoin_0.h(0)
qcoin_0.measure_all()

qcoin_0.draw("mpl")

sim = AerSimulator()

compiled = transpile(qcoin_0,sim)
job = sim.run(compiled,shots=1000)
result = job.result()

print(result)
counts = result.get_counts()
plot_histogram(counts)
plt.show()