import numpy as np

def entanglement_entropy(ps):
    #calculate the entanglement entropy from Schmidt coefficient

    entropy = 0
    for kk in ps:
        if kk != 0:
            entropy += kk**2*np.log2(kk**2)
        else:
            pass
    return -entropy
