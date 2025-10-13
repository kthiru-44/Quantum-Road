#  From Classical to Quantum Information

## 1️⃣ Comparison of Information Types

**Classical bit** → one of `{0,1}`  
**Probabilistic bit** → real probability vector (e.g. (p, 1–p))  
**Quantum bit (qubit)** → complex vector (α₀, α₁)

| Type | Representation | Normalization | Operations |
|------|----------------|----------------|-------------|
| Classical | 0 or 1 | — | Logic gates |
| Probabilistic | (p, 1–p) | p₀ + p₁ = 1 | Stochastic matrices |
| Quantum | (α₀, α₁) ∈ ℂ² | \|α₀\|² + \|α₁\|² = 1 | **Unitary** matrices |

Quantum = probabilistic + **complex amplitudes** + **interference**.

---

## ⚛️ 2️⃣ Quantum State Vectors

A **quantum state** (ket) is a **unit vector** in a complex vector space:

$$
|\psi\rangle =
\begin{bmatrix}
\alpha_0 \\
\alpha_1
\end{bmatrix},
\quad
|\alpha_0|^2 + |\alpha_1|^2 = 1
$$

### Examples

$$
|0\rangle =
\begin{bmatrix}
1 \\
0
\end{bmatrix},
\quad
|1\rangle =
\begin{bmatrix}
0 \\
1
\end{bmatrix}
$$

$$
|+\rangle =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
1
\end{bmatrix},
\quad
|-\rangle =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 \\
-1
\end{bmatrix}
$$

A general qubit:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle,
\quad
|\alpha|^2 + |\beta|^2 = 1
$$

---

## 📏 3️⃣ Measurement (Born Rule)

When measuring in the computational basis:

$$
P(0) = |\langle 0 | \psi \rangle|^2,
\quad
P(1) = |\langle 1 | \psi \rangle|^2
$$

After measurement, the state collapses to the observed basis vector.

**Example:**

$$
|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)
\Rightarrow
P(0) = P(1) = \frac{1}{2}
$$

---

## 🔄 4️⃣ Unitary Operations (Quantum Gates)

Quantum operations are **unitary**, meaning they preserve norms:

$$
U^\dagger U = U U^\dagger = I
$$

or equivalently:

$$
\|U|\psi\rangle\| = \||\psi\rangle\|
$$

---


## 🌀 5️⃣ Why It Matters

- **Superposition** encodes multiple classical states simultaneously.  
- **Complex amplitudes** allow **interference**, where probabilities add or cancel.  
- **Unitary operations** preserve total probability but rotate states to extract useful interference.

Hence, all quantum speedups come from:
> **Unitary transformations + measurement.**

---

📘 *This section connects linear algebra, probability, and complex numbers — forming the mathematical backbone of quantum computation.*
