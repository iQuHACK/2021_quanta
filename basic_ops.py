# Basic operations on qubits for Tiq-Taq-Toe
#import Aer here, before calling qiskit_ionq_provider
from qiskit import Aer, execute
# import all the other stuff
from qiskit_ionq_provider import IonQProvider 
from qiskit.quantum_info import entropy, DensityMatrix, partial_trace
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_histogram
from qiskit.providers.jobstatus import JobStatus
from qiskit import QuantumCircuit

with open(".ionqkey.txt") as keyfile:
    key = keyfile.readline().strip('\n')
#Call provider and set token value
provider = IonQProvider(token=key)#Call provider and set token value

# initialize board with side length n (currently allows 1 (trivial), 2 and 3). Adds an ancilla qubit for each team. Each qubit is associated with a classical channel for readout.
def initialize(n):
    qc = QuantumCircuit(n*n+2,n*n+2)
    qc.h([0,1])
    return qc

# entangle the team qubit with a chosen location on the board (numbered starting at 1 from the upper left corner and proceeding left to right by row.)
def entangle(qcircuit,team,bit):
    qc=qcircuit
    qc.cx(team,bit-1)
    return qc