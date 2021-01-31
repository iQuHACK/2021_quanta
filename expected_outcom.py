from qiskit import Aer, execute
from qiskit.visualization.utils import _bloch_multivector_data
import numpy as np
import math

def expected_outcome(circ):
    # Caculates the probability of measurign 0 for each qubit
    state_sim = Aer.get_backend('statevector_simulator')
    sim = execute(circ, state_sim, shots=1000)
    state_sim_result = sim.result()
    state_vec = state_sim_result.get_statevector(decimals=3)
    p0s = []
    for kk in _bloch_multivector_data(state_vec):
        if kk[2] != 0:
            if kk[2] > 0:
                theta = np.arccos(math.floor(kk[2]/np.sum(np.asarray(kk)**2))
            else:
                theta = np.arccos(math.ceil(kk[2]/np.sum(np.asarray(kk)**2))
        else:
            theta = np.pi/2
        p0 = round(np.cos(theta/2)**2,2)
        p0s.append(p0)

    return p0s
