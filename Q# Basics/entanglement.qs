import Std.Diagnostics.*;

// For First Bell State |Φ+⟩ = (|00⟩ + |11⟩) / √2

operation Main() : (Result, Result) {
    use (q1, q2) = (Qubit(), Qubit());

    H(q1);
    CNOT(q1, q2);

    DumpMachine();

    let (m1, m2) = (M(q1), M(q2));
    Reset(q1);
    Reset(q2);

    return (m1, m2);
}