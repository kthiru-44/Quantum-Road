🧠 Quantum Measurement & Uncertainty in Qiskit

    This project simulates how quantum measurements behave in different bases (Z, X, Y) and visualizes the Heisenberg uncertainty principle using Qiskit and Aer simulators.
    
    We explore how rotating a qubit before measurement changes the observed outcomes, and how uncertainty varies with state orientation—analogous to how physical measurements in quantum systems like spin behave.


1️⃣ Z-Basis then X-Basis Measurement

    Start in the computational basis (|0⟩).
    
    First measure directly in the Z-basis.
    
    Then rotate using H and measure in the X-basis.
    
    Simulates sequential Stern–Gerlach experiments with magnets aligned in Z and then X directions.
    
    Histograms show probabilities of both measurements.

2️⃣ X-Basis then Z-Basis Measurement

    Begin by rotating the state with a Hadamard gate.
    
    First measure in the X-basis.
    
    Then rotate back and measure in the Z-basis.
    
    Demonstrates measurement collapse and basis dependence.
    
    You’ll observe similar randomness due to quantum indeterminacy.

3️⃣ Graphing the Uncertainty Principle

    Prepare a parameterized quantum state using RY(θ).
    
    Measure expectation values of X, Y, and Z observables.
    
    Compute:
    
    ⟨X⟩, ⟨Y⟩, ⟨Z⟩
    
    ΔX = √(1 - ⟨X⟩²)
    
    ΔZ = √(1 - ⟨Z⟩²)
    
    Product ΔX · ΔZ
    
    📈 Plots show how uncertainty changes with θ and that uncertainty product behaves consistently with Heisenberg's principle.

4️⃣ Higher Y Expectation Visualization

    Adds an additional rotation RZ(π/4) to the previous circuit.
    
    Increases the Y-component of the spin.
    
    Again measures ⟨X⟩, ⟨Y⟩, ⟨Z⟩ and computes uncertainties.
    
    Shows how preparing the state differently changes the observed uncertainties.

🔬 Measurement Analogy

    In real experiments:
    
    Rotating a Stern–Gerlach magnet changes the spin component being measured (X, Y, or Z).
    
    In Qiskit:
    
    Z-basis → measure directly.
    
    X-basis → apply Hadamard (H), then measure.
    
    Y-basis → apply Sdg + H, then measure.
    
    Thus: basis change = magnet rotation.

📊 Example Results

    Repeated measurements yield consistent results after collapse.
    
    RY(θ) state shows varying uncertainties based on orientation.
    
    High ⟨Y⟩ states modify ΔX and ΔZ behavior.
    
    ΔX · ΔZ ≥ threshold, showing uncertainty trade-offs.


    Each experiment prints the measurement counts and shows histograms or plots.


📖 References

    Qiskit Documentation: https://qiskit.org
    
    Heisenberg Uncertainty Principle: Wikipedia
