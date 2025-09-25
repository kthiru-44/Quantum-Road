# 🧭 Stern–Gerlach Experiment in Qiskit

This project simulates the **Stern–Gerlach experiment** using Qiskit and Aer simulators.  
The real Stern–Gerlach experiment (1922) showed that silver atoms passing through a magnetic field split into **two discrete beams**, corresponding to **quantized spin angular momentum** values (+ℏ/2 and −ℏ/2).  

Here, we reproduce these ideas on qubits by preparing states, measuring them along different axes, and comparing results.


📂 File: Stern-Gerlach.py
The script is structured into independent experiments.
👉 Run one section at a time (comment/uncomment code blocks).

1️⃣ Arbitrary State – Multiple Measurements

    Prepares a random qubit state a|0⟩ + b|1⟩.
    
    Measures repeatedly in the Z-basis.

    Histogram shows probabilities of 0 (spin-up) vs 1 (spin-down).

2️⃣ Creating Random Spins

    Uses random rotations (Rx, Rz) to generate different spin orientations.
    
    Simulates an ensemble of particles.
    
    Shows that measurement outcomes distribute according to orientation.

3️⃣ Repeated Measurements

    Prepares a superposition with H|0⟩.
    
    Measures twice into two classical registers.
    
    Demonstrates collapse: once measured, the outcome is fixed for subsequent measurements.

4️⃣ Measuring Along Different Axes

    Z-axis: direct measurement (measure).
    
    X-axis: apply H then measure.
    
    Y-axis: apply Sdg, then H, then measure.
    
    Shows how changing the measurement basis changes observed probabilities.

🔬 Stern–Gerlach Analogy
   
    In the lab: rotating the magnetic field changes which spin component is measured (Z, X, or Y).
    
    In Qiskit: rotating the qubit state before measurement simulates this.
    
    Z-basis → measure
    
    X-basis → H then measure
    
    Y-basis → Sdg, then H, then measure
    
    Thus, basis change = rotating Stern–Gerlach magnet.

📊 Example Results

    Arbitrary state in Z-basis → outcomes weighted by |a|² and |b|².
    
    Repeated measurements → first result is random, but repeats remain the same.
    
    X-basis measurement of ∣0⟩
    ∣0⟩ → ~50/50 split between 0 and 1.

🚀 How to Run

    Run the script:
    
    python Stern-Gerlach.py
    Comment/uncomment experiment blocks as needed (### 1, ### 2, etc.).
    
    Each experiment prints counts and shows a histogram.




