from qiskit import QuantumCircuit
from qiskit.circuit import Parameter , QuantumRegister , ClassicalRegister
import numpy as np
from qiskit.quantum_info import SparsePauliOp
from qiskit.result import marginal_counts
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.primitives import BackendEstimatorV2
from qiskit.primitives import BackendSamplerV2


### 1. MEASURING ALONG Z AND SWITCHING TO X

## Step 1: Map

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(2, "c")
qc = QuantumCircuit(qr, cr)

# Add a first measurement
qc.measure(0,0)
qc.barrier()

# Change basis so that measurements made on quantum computer which normally tell us about z, now tell us about x.
qc.h(0)

# Add a second measurement
qc.measure(0, 1)

qc.draw("mpl")

## Step 2: Optimise and Execute

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

job = sam_sim.run([qc])
counts=job.result()[0].data.c.get_counts()

# Step 3: Analyse

print(counts)
plot_histogram(counts)
plt.show()

#To see both measurements seperately

plot_histogram(
    marginal_counts(counts, indices=[0]), title="Counts after first measurement"
)
plot_histogram(
    marginal_counts(counts, indices=[1]), title="Counts after second measurement"
)

plt.show()

### 2. MEASURING ALONG X AND SWITCHING TO Z

## Step 1: Map

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(2, "c")
qc = QuantumCircuit(qr, cr)

# Add a first measurement

qc.h(qr)
qc.measure(qr , cr[0])
qc.barrier()

# Add a second measurement

qc.h(qr)
qc.measure(qr , cr[1])

## Step 2: Optimise and Execute

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

job = sam_sim.run([qc])
counts=job.result()[0].data.c.get_counts()

## Step 3: Analyse

print(counts)

plot_histogram(counts)

# To see both measurements seperately

plot_histogram(
    marginal_counts(counts, indices=[0]), title="Counts after first measurement"
)
plot_histogram(
    marginal_counts(counts, indices=[1]), title="Counts after second measurement"
)

plt.show()

### 3. GRAPHICALLY REPRESENTING UNCERTAINITY WITH X AND Z

# Step 1: Map the problem into a quantum circuit

# Specify observables
obs1 = SparsePauliOp("X")
obs2 = SparsePauliOp("Y")
obs3 = SparsePauliOp("Z")

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(1, "c")
qc = QuantumCircuit(qr, cr)

# Rotate away from |0>
theta = Parameter("θ")
qc.ry(theta, 0)

params = np.linspace(0, 2, num=21)

# Step 2: Transpile the circuit

obs1_isa = obs1.apply_layout(layout=qc.layout)
obs2_isa = obs2.apply_layout(layout=qc.layout)
obs3_isa = obs3.apply_layout(layout=qc.layout)

# Step 3: Run the circuit on a real quantum computer

sim = AerSimulator()
esm_sim = BackendEstimatorV2(backend=sim)

pubs = [(qc, [[obs1_isa], [obs2_isa], [obs3_isa]], [params])]
job = esm_sim.run(pubs)
res= job.result()


# Step 4: Post-processing and classical analysis.
xs = res[0].data.evs[0]
ys = abs(res[0].data.evs[1])
zs = res[0].data.evs[2]

# Calculate uncertainties

delx = []
delz = []
prodxz = []
for i in range(len(xs)):
    delx.append(abs((1 - xs[i] * xs[i])) ** 0.5)
    delz.append(abs((1 - zs[i] * zs[i])) ** 0.5)
    prodxz.append(delx[i] * delz[i])

# Here we can plot the results from this simulation.
import matplotlib.pyplot as plt

plt.plot(params, delx, label=r"$\Delta$ X")
plt.plot(params, ys, label=r"$\langle$ Y $\rangle$")
plt.plot(params, delz, label=r"$\Delta$ Z")
plt.plot(params, prodxz, label=r"$\Delta$X $\Delta$Z")
plt.xlabel(r"$\theta$")
plt.ylabel("Expectation/Uncertainty Values")
plt.legend()
plt.show()

### 4. MEASURING IN GRAPHS WITH HIGHER Y EXPECTATION VALUE

# Step 1: Map the problem to a quantum circuit

# Specify observables
obs1 = SparsePauliOp("X")
obs2 = SparsePauliOp("Y")
obs3 = SparsePauliOp("Z")

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(1, "c")
qc = QuantumCircuit(qr, cr)

# Rotate away from |0> along one plane, and then along a transverse direction.
theta = Parameter("θ")
qc.ry(theta, 0)
qc.rz(np.pi / 4, 0)

params = np.linspace(0, 2, num=21)

# Step 2: Transpile the circuit


obs1_isa = obs1.apply_layout(layout=qc.layout)
obs2_isa = obs2.apply_layout(layout=qc.layout)
obs3_isa = obs3.apply_layout(layout=qc.layout)

# Run the job on the Aer simulator with noise model from real backend

job = esm_sim.run([(qc, [[obs1_isa], [obs2_isa], [obs3_isa]], [params])], precision=0.01)
res=job.result()

# Step 4: Post-processing and classical analysis.
xs = res[0].data.evs[0]
ys = abs(res[0].data.evs[1])
zs = res[0].data.evs[2]

# Calculate uncertainties

delx = []
delz = []
prodxz = []
for i in range(len(xs)):
    delx.append(abs((1 - xs[i] * xs[i])) ** 0.5)
    delz.append(abs((1 - zs[i] * zs[i])) ** 0.5)
    prodxz.append(delx[i] * delz[i])

# Here we can plot the results from this simulation.

plt.plot(params, delx, label=r"$\Delta$ X")
plt.plot(params, ys, label=r"$\langle$ Y $\rangle$")
plt.plot(params, delz, label=r"$\Delta$ Z")
plt.plot(params, prodxz, label=r"$\Delta$X $\Delta$Z")
plt.xlabel(r"$\theta$")
plt.ylabel("Expectation/Uncertainty Values")
plt.legend()
plt.show()
