from qiskit import QuantumCircuit
from qiskit.circuit import Parameter , QuantumRegister , ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from qiskit.primitives import BackendSamplerV2
import numpy as np
import random

### 1 .ONE ARBITRARY STATE MULTIPLE MEASUREMENT

# Creating a Arbitrary Spin state.
a = random.random()
b = random.random()
norm = np.sqrt(a * np.conjugate(a) + b * np.conjugate(b))
a = a / norm
b = b / norm

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

#Setting up Circuit
qc = QuantumCircuit(1,1)
qc.initialize([a,b])
qc.measure(0,0)
qc.draw("mpl")

#Running

result = sam_sim.run([qc],shots=10).result()

counts = result[0].data.c.get_counts()
print(counts)
plot_histogram(counts)
plt.show()

### 2. CREATING RANDOM SPIN

theta = Parameter("θ")
phi = Parameter("$\phi$")

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(1, "c")
qc = QuantumCircuit(qr, cr)

# Add rotation gates for rotating the state of qubit 0 to random orientations
qc.rx(theta, 0)
qc.rz(phi, 0)
qc.measure(0, 0)

qc.draw("mpl")

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

# A list to store the accumulated probabilities of the two possible measurement outcomes.
probslist = {"0": 0.0, "1": 0.0}

# Choose how many "particles"/measurements
measurements = 3
num_shots = 1

for i in range(measurements):
    # Assign a random orientation for each measurement
    phi = random.random() * 2 * np.pi
    theta = random.random() * 2 * np.pi

    angles = [phi, theta]
    circuit = qc.assign_parameters(angles)
    #Run the circuit
    job = sam_sim.run([circuit],shots = num_shots).result()

    # Update the list of probabilities
    zeroterm = job[0].data.c.get_counts().get("0") or 0
    oneterm = job[0].data.c.get_counts().get("1") or 0
    probslist.update({"0": probslist.get("0") + zeroterm})
    probslist.update({"1": probslist.get("1") + oneterm})

probslist.update({"0": probslist.get("0") / measurements})
probslist.update({"1": probslist.get("1") / measurements})

print(probslist)
plot_histogram(probslist)
plt.show()

### 3.REPEATED MEASUREMENTS

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(2, "c")
qc = QuantumCircuit(qr, cr)

# Initialize the qubit to be a mixture of 0 and 1 states.
qc.h(0)

# Add a first measurement
qc.measure(0, 0)
qc.barrier()

# Add a second measurement
qc.measure(0, 1)
qc.draw("mpl")

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

#Running

result = sam_sim.run([qc],shots=1000).result()
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()

### 4. MEASURING DIFFERENT OBSERVABLES

## 4.1 Measuring Along X for |0>

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(1, "c")
qc = QuantumCircuit(qr, cr)

# Add a hadamard gate to rotate into the x-basis
qc.h(0)
qc.measure(0, 0)

qc.draw("mpl")

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

#Running

result = sam_sim.run([qc],shots=1000).result()
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()

## 4.2 Measuring Along X for |1>

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(1, "c")
qc = QuantumCircuit(qr, cr)

# Add a Not gate and hadamard gate to rotate into the x-basis for |1>
qc.x(0)
qc.h(0)
qc.measure(0, 0)

qc.draw("mpl")

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

#Running

result = sam_sim.run([qc],shots=1000).result()
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()

## 4.3 Checking if measured qubit stays the same value

# Define registers
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(2, "c")
qc = QuantumCircuit(qr, cr)

# Rotate into x-basis using a Hadamard gate, then make two measurements in succession
qc.h(0)
qc.measure(0, 0)
qc.barrier()
qc.measure(0, 1)

#Setting up Simulator

sim = AerSimulator()
sam_sim = BackendSamplerV2(backend=sim)

#Running

result = sam_sim.run([qc],shots=1000).result()
counts = result[0].data.c.get_counts()
print(counts)

plot_histogram(counts)
plt.show()
