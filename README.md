# Quantum Tiq-Taq-Toe
Kyle Debry, Felix Knollmann, Xiaoyang Shi


## Team: Quanta

## Abstract
The Quantum Tiq-Taq-Toe is a 1 vs. 1 game similar to it's classical counterpart. The game board is made of 9 qubits arranged in a 3 x 3 grid, initialized in the |0> + |1> state. Each player is allowed to do one of the two single qubit gates or a controlled-NOT gate each turn. Each qubit can only be manipulated by a single qubit gate once but it can be used as the control qubit for the CNOT without limit. After each gate is implemented, a simulation of the result will be shown, with redness proportional to the probability of measuring |0> and blueness proportional to the probability of measuring |1> (purple for |0> + |1>). After each player has made 10 moves or there is no qubit that hasn't been acted on by a single qubit gate, the whole circuit will be passed through the IonQ's 9-qubit machine. The winner will be the one who has more counts of winning patterns game (same patterns as in a classical Tiq-Taq-Toe but with cross and circles replaced by |0> and |1>).  

## How to run the code
The game is based on Pygame so first run\
`pip install pygame`.\
To get the final result from the IonQ machine, a file named `.ionqkey.txt` needs to be created at the local directory and it should include the API key. Once these are setup, run\
`python TiqTaqToe.py`.\
Once the game is running, the game proceeds in turns. In a turn, players first pick a gate by clicking on the icons on the left of the window and then click to choose the qubit this gate should act on. For the CNOT gate, the first click of qubit will set the control qubit and the second click will set the target qubit.


## Software Dependencies
Qiskit and its dependencies\
Pygame

## Date
2021-01-30


## Side project: telephone!
For kicks we had the ionQ QC play telephone with itself. We input a number as a bitstring, then swap the values back and forth a given number of times. The swaps represent the whispers between neighbors. This effectively demonstrates the accumulation of error over many operations on the quantum computer.
