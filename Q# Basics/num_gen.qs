import Std.Convert.*;
import Std.Math.*;

operation Main() : Int {
    let max = 128;
    Message($"The Random Number Generated : ");

    return Randomnumbergenerator(max);
}

operation Randomnumbergenerator(max : Int) : Int {

    mutable bits = [];
    let nBits = BitSizeI(max);
    for idxBit in 1..nBits {
        set bits += [GenerateRandomBit()];
    }
    let sample = ResultArrayAsInt(bits);

    return sample > max ? Randomnumbergenerator(max) | sample ;
}

operation GenerateRandomBit() : Result{

    use q = Qubit();
    H(q);
    let result = M(q);

    Reset(q);

    return result

}