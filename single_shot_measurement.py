from qiskit import Aer, execute
from qiskit_ionq_provider import IonQProvider 
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_histogram
from qiskit.providers.jobstatus import JobStatus
import time

with open(".ionqkey.txt") as keyfile:
    key = keyfile.readline().strip('\n')

def single_shot(circ, single = True):
    provider = IonQProvider(token=key)
    qpu_backend = provider.get_backend("ionq_qpu")
    if single == False:
        shots = 1024
    else:
        shots = 1
    qpu_job = qpu_backend.run(circ, shots = shots)
    job_id = qpu_job.job_id()
    job = qpu_backend.retrieve_job(job_id)
    while job.status() is not JobStatus.DONE:
        print("Job is not done")
        job = qpu_backend.retrieve_job(job_id)
        time.sleep(5)
    print("Job done")
    qpu_result = qpu_job.result()
    counts = qpu_result.get_counts()
    return counts