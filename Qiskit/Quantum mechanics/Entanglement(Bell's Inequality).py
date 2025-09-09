from qiskit import QuantumCircuit
import numpy as np
from qiskit.primitives import StatevectorSampler
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.primitives import BackendSamplerV2

qcs = [QuantumCircuit(2, 2), QuantumCircuit(2, 2), QuantumCircuit(2, 2)]
for i in range(0, len(qcs)):
    qcs[i].x([0, 1])
    qcs[i].h(0)
    qcs[i].cx(0, 1)

qcs[0].ry(-2 * np.pi / 3, 1)
qcs[1].ry(-4 * np.pi / 3, 1)
qcs[2].ry(-2 * np.pi / 3, 1)
qcs[2].ry(-4 * np.pi / 3, 1)
counts_list = [None] * len(qcs)

for i in range(0, len(qcs)):
    qcs[i].barrier()
    qcs[i].measure([0, 1], [0, 1])
    qcs[i].draw(output="mpl")

# 1. Running in a sampler

sampler = StatevectorSampler()

for i in range(0, len(qcs)):
    pub = qcs[i]
    job = sampler.run([pub], shots=10000)
    result = job.result()
    data_pub = result[0].data
    counts = data_pub.c.get_counts()
    counts_list[i] = counts
outcomes = ("00", "01", "10", "11")

#Here we convert "None"s into 0's so that we can sum.

for i in range(0, len(qcs)):
    for j in range(0, len(outcomes)):
        if counts_list[i].get(outcomes[j]) is None:
            counts_list[i].update({outcomes[j]: 0})

# Here we create a dictionary that holds all the outcomes and sums over their appearances in each of the circuits.

total_counts = {}
for i in range(0, len(outcomes)):
    total_counts[outcomes[i]] = sum(
        counts_list[j].get(outcomes[i]) for j in range(0, len(qcs))
    )

print(total_counts)
plot_histogram(total_counts)

plot_histogram(counts_list)
plt.show()

# 2. Running in Qiskit-Aer

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

for i in range(0, len(qcs)):
    pub = qcs[i]
    job = sam_sim.run([pub], shots=10000)
    result = job.result()
    data_pub = result[0].data
    counts = data_pub.c.get_counts()
    counts_list[i] = counts
outcomes = ("00", "01", "10", "11")

#Here we convert "None"s into 0's so that we can sum.

for i in range(0, len(qcs)):
    for j in range(0, len(outcomes)):
        if counts_list[i].get(outcomes[j]) is None:
            counts_list[i].update({outcomes[j]: 0})

# Here we create a dictionary that holds all the outcomes and sums over their appearances in each of the circuits.

total_counts = {}
for i in range(0, len(outcomes)):
    total_counts[outcomes[i]] = sum(
        counts_list[j].get(outcomes[i]) for j in range(0, len(qcs)))

print(total_counts)
plot_histogram(total_counts)
plot_histogram(counts_list)
plt.show()

