# ⚙️  Quantum Circuits

Quantum circuits represent **unitary operations** acting on **quantum states**.

A single-qubit transformation is

$$
|\psi' \rangle = U |\psi\rangle, \quad \text{where } U^\dagger U = I
$$

For multiple qubits, operations are built using **tensor products** and **controlled gates**.

---

## 🧩  One-Qubit Operations

Each gate is a **2×2 unitary matrix** acting on a single qubit.

**Common examples:**

$$
X =
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix},
\quad
Y =
\begin{bmatrix}
0 & -i \\
i & 0
\end{bmatrix},
\quad
Z =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

---

## 🔗  Two-Qubit Operations

Two-qubit operations act on **4-dimensional Hilbert spaces**.

### Controlled-NOT (CNOT)

$$
\text{CNOT} =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0
\end{bmatrix}
$$

This flips the **target qubit** when the **control** is 1.

| Input | Output |
|:------|:-------|
| `|00⟩` | `|00⟩` |
| `|01⟩` | `|01⟩` |
| `|10⟩` | `|11⟩` |
| `|11⟩` | `|10⟩` |

---

##   Circuit Composition

If two gates \( U_1 \) and \( U_2 \) act sequentially:

$$
|\psi' \rangle = U_2 U_1 |\psi\rangle
$$

Matrix multiplication order follows **right-to-left** execution.

Parallel operations use tensor products:

$$
U_{\text{total}} = U_1 \otimes U_2
$$

---

# 🔺  Inner Products and Projections

## 📐  Inner Product Definition

For two qubit states:

$$
\langle \phi | \psi \rangle = \alpha_0^* \beta_0 + \alpha_1^* \beta_1
$$

If both are normalized:

$$
|\langle \phi | \psi \rangle|^2 \le 1
$$

Equality occurs only if \( |\phi\rangle = e^{i\theta}|\psi\rangle \).

---

## 🧮  Orthogonality and Measurement

Two states are **orthogonal** if their inner product is zero:

$$
\langle \phi | \psi \rangle = 0
$$

**Examples:**

$$
\langle 0 | 1 \rangle = 0, \quad \langle + | - \rangle = 0
$$

When measured in an orthogonal basis, the probability of confusing them is **zero**.

---

## 🎯  Projection Operators

Projection onto a state \( |\phi\rangle \):

$$
P_\phi = |\phi\rangle \langle \phi |
$$

Applied to any state:

$$
P_\phi |\psi\rangle = |\phi\rangle \langle \phi | \psi \rangle
$$

**Example:**

$$
P_{|0\rangle} =
\begin{bmatrix}
1 & 0 \\
0 & 0
\end{bmatrix},
\quad
P_{|1\rangle} =
\begin{bmatrix}
0 & 0 \\
0 & 1
\end{bmatrix}
$$

Measurement probabilities:

$$
P(0) = \langle \psi | P_{|0\rangle} | \psi \rangle
$$

---

# 🚫  Limitations of Quantum Information

## 🌀  Global Phase Irrelevance

Multiplying a state by a **global phase** does not change physical predictions:

$$
|\psi\rangle \sim e^{i\theta}|\psi\rangle
$$

**Example:**

$$
|0\rangle \text{ and } e^{i\pi}|0\rangle = -|0\rangle
$$

represent **the same physical state**.

---

## ❌  No-Cloning Theorem

There is **no unitary operator** \( U \) that can clone an arbitrary unknown quantum state:

$$
U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle
$$

**Proof Sketch:**

For any two distinct states \( |\psi_1\rangle, |\psi_2\rangle \):

$$
\langle \psi_1 | \psi_2 \rangle = \langle \psi_1 | \psi_2 \rangle^2
$$

This equality is only possible if  
\( \langle \psi_1 | \psi_2 \rangle = 0 \) or \( 1 \).  

Hence cloning cannot preserve inner products, violating unitarity.

---

## 🧩  Non-Orthogonal States Cannot Be Perfectly Distinguished

Quantum states that are **not orthogonal** cannot be perfectly identified by any measurement.

**Example:**

$$
|0\rangle, \quad |+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
$$

They have inner product:

$$
\langle 0 | + \rangle = \frac{1}{\sqrt{2}}
$$

Any measurement on them has inherent uncertainty —  
the foundation of **quantum cryptography**.

---

# 🧭 Summary

| Concept | Mathematical Condition | Physical Meaning |
|:---------|:-----------------------|:-----------------|
| **Unitary gate** | \(U^\dagger U = I\) | Reversible evolution |
| **Orthogonal states** | \(\langle \phi | \psi \rangle = 0\) | Perfectly distinguishable |
| **Projection** | \(P_\phi = |\phi\rangle\langle\phi|\) | Measurement operator |
| **Global phase** | \(e^{i\theta}\) factor | Physically irrelevant |
| **No-cloning** | Nonlinear transformation impossible | Protects quantum information |
| **Non-orthogonality** | \(0 < |\langle \phi | \psi \rangle| < 1\) | Measurement uncertainty |

---

📘 *These principles constrain what can be done with quantum information, forming the foundation of quantum communication, algorithms, and cryptography.*
