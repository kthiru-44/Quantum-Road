

import Microsoft.Quantum.Diagnostics.*;
import Microsoft.Quantum.Intrinsic.*;
import Microsoft.Quantum.Measurement.*;

operation Main() : Result[] {

    use (message, bob) = (Qubit(), Qubit());

    let stateInitializerBasisTuples = [
        ("|0〉", I, PauliZ),
        ("|1〉", X, PauliZ),
        ("|+〉", SetToPlus, PauliX),
        ("|-〉", SetToMinus, PauliX)
    ];

    mutable results = [];
    for (state, initializer, basis) in stateInitializerBasisTuples {

        initializer(message);
        Message($"Teleporting state {state}");
        DumpMachine();

        Teleport(message, bob);
        Message($"Received state {state}");
        DumpMachine();

        let result = Measure([basis], [bob]);
        set results += [result];
        ResetAll([message, bob]);
    }

    return results;
}

operation Teleport(message : Qubit, bob : Qubit) : Unit {

    use alice = Qubit();

    H(alice);
    CNOT(alice, bob);

    CNOT(message, alice);
    H(message);

    if M(message) == One {
        Z(bob);
    }
    if M(alice) == One {
        X(bob);
    }

    Reset(alice);
}

/// Sets a qubit in state |0⟩ to |+⟩
operation SetToPlus(q : Qubit) : Unit is Adj + Ctl {
    H(q);
}


/// Sets a qubit in state |0⟩ to |−⟩
operation SetToMinus(q : Qubit) : Unit is Adj + Ctl {
    X(q);
    H(q);
}