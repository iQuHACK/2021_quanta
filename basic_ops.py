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
import math

with open(".ionqkey.txt") as keyfile:
    key = keyfile.readline().strip('\n')
#Call provider and set token value
provider = IonQProvider(token=key)#Call provider and set token value

# initialize board with side length n (currently allows 1 (trivial), 2 and 3). Adds an ancilla qubit for each team. Each qubit is associated with a classical channel for readout.
def initialize(n):
    circ = QuantumCircuit(n*n,n*n)
    circ.h(range(n*n))
    return circ

# entangle the team qubit with a chosen location on the board (numbered starting at 1 from the upper left corner and proceeding left to right by row.)
def add_cnot(circ,control,target):
    circ.cx(control,target)
    return circ

#rotation
def add_ry(circ, team, loc):
	if team==1:
		theta = math.pi/2.
	else: theta = -math.pi/2.
	circ.ry(theta, loc)
	return circ

#measure final state, n is the side length of the board
def add_measurement(circ,n):
	circ.measure(range(n*n),range(n*n))
	return circ