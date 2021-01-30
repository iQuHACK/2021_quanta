from qiskit import Aer, execute
from qiskit_ionq_provider import IonQProvider 
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_histogram
from qiskit.providers.jobstatus import JobStatus
from qiskit import QuantumCircuit
import math

with open(".ionqkey.txt") as keyfile:
    key = keyfile.readline().strip('\n')
#Call provider and set token value
provider = IonQProvider(token=key)#Call provider and set token value
