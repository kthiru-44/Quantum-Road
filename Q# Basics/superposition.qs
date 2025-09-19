

// 1.

import Std.Diagnostics.*;

operation Main() : Result {
    use q = Qubit();
    Message("Initialized qubit:");
    DumpMachine(); 
    Message(" ");
    H(q);
    Message("Qubit after applying H:");
    DumpMachine();
    Message(" ");
    let randomBit = M(q);
    Message("Qubit after the measurement:");
    DumpMachine(); 
    Message(" ");
    Reset(q);
    Message("Qubit after resetting:");
    DumpMachine(); 
    Message(" ");
    return randomBit;
}


// 2. 

// To get a different probablity for zero and one each time , we skew the qubit before applying h 
// We do that by rotatiing on y axis by an angle 2cos^-1(sqrt(Probablity of |0>))

import Std.Diagnostics.*;
import Std.Math.*;

operation skewedrandomBit() : Result {

    use q = Qubit();

    let P = 0.333333;
    Ry(2.0 * ArcCos(Sqrt(P)), q);

    Message("The qubit is in the desired state.");
    DumpMachine();
    Message(" ");
    Message("Your skewed random bit is:");
    let skewedrandomBit = M(q);
    Reset(q);
    return skewedrandomBit;
}

// 3. 

// To measure multiple qubits at the same time we assign multiple qubits them and measure them along z 

import Std.Diagnostics.*;
import Std.Convert.*;

operation Multiplebits() : Int {
    use qubits = Qubit[3];
    ApplyToEach(H, qubits);
    Message("The qubit register in a uniform superposition: ");
    DumpMachine();
    let result = MeasureEachZ(qubits);
    Message("Measuring the qubits collapses the superposition to a basis state.");
    DumpMachine();
    ResetAll(qubits);
    return ResultArrayAsInt(result);
}

