import perceval as pcvl
import math
import numpy as np
from perceval.utils import Encoding, PostSelect, Matrix
from perceval.components import Circuit, Port, Unitary

#first part
def get_CCZ() -> pcvl.Processor:

    processor = pcvl.Processor("MPS", 6)
    T = Matrix( [[1,0], [0, np.exp(1j*np.pi/4)]] )
    Tdg = Matrix( [[1,0], [0, np.exp(-1j*np.pi/4)]] )
    processor.add((2,3,4,5), pcvl.catalog["klm cnot"].build_processor())
    processor.add((4,5), Unitary(Tdg))
    processor.add((0,1,4,5), pcvl.catalog["klm cnot"].build_processor())
    processor.add((4,5), Unitary(T))
    processor.add((2,3,4,5), pcvl.catalog["klm cnot"].build_processor())
    processor.add((4,5), Unitary(Tdg))
    processor.add((0,1,4,5), pcvl.catalog["klm cnot"].build_processor())
    processor.add((4,5), Unitary(T))
    processor.add((0,1), Unitary(T))
    processor.add((0,1,2,3), pcvl.catalog["klm cnot"].build_processor())
    processor.add((0,1), Unitary(T))
    processor.add((2,3), Unitary(Tdg))
    processor.add((0,1,2,3), pcvl.catalog["klm cnot"].build_processor())

    return processor

#second part
def special_CZ() -> pcvl.Processor:

    processor = pcvl.Processor("MPS", 8)
    CZCZ = Matrix( [[1,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0], [0,0,1,0,0,0,0,0], [0,0,0,-1,0,0,0,0], [0,0,0,0,1,0,0,0], [0,0,0,0,0,-1,0,0], [0,0,0,0,0,0,1,0], [0,0,0,0,0,0,0,1]] )
    processor.add((0,1,2,3,4,5,6,7), Unitary(CZCZ))

    return processor
