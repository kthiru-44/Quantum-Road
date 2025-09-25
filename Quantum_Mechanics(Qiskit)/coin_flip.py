from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.primitives import BackendSamplerV2
from qiskit.primitives import BackendEstimatorV2
from qiskit.quantum_info import Pauli

sim = AerSimulator()

sampler_sim = BackendSamplerV2(backend = sim)

estimator_sim = BackendEstimatorV2(backend = sim)

##Single  coin Flip
# qcoin_0 = QuantumCircuit(1)
# qcoin_0.h(0)
# qcoin_0.measure_all()
#
# qcoin_0.draw("mpl")
#
# job = sampler_sim.run([qcoin_0])
# counts=job.result()[0].data.meas.get_counts()
#
# plot_histogram(counts)
# plt.show()

##Double coin Flip
# qcoin_0 = QuantumCircuit(1)
# qcoin_0.h(0)
# qcoin_0.h(0)
# qcoin_0.measure_all()
#
# qcoin_0.draw("mpl")
#
# job = sampler_sim.run([qcoin_0])
# counts=job.result()[0].data.meas.get_counts()
#
# plot_histogram(counts)
# plt.show()

# # Measuring on all coordinates
# qcoin_sx = QuantumCircuit(1)
# qcoin_sx.sx(0)
# qcoin_sx.draw("mpl")
#
# obs1 = Pauli("X")
# obs2 = Pauli("Y")
# obs3 = Pauli("Z")
#
# pubs = [(qcoin_sx, [obs1, obs2, obs3])]
# job = estimator_sim.run(pubs)
# res = job.result()
# counts = res[0].data.evs
# print("Expectation values ⟨X⟩, ⟨Y⟩, ⟨Z⟩:")
# print(counts)
# plt.show()
