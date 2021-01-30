from qiskit import Aer, execute
from qiskit_ionq_provider import IonQProvider 
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_histogram
from qiskit.providers.jobstatus import JobStatus
import time

with open(".ionqkey.txt") as keyfile:
    key = keyfile.readline().strip('\n')

def single_shot(circ):
    provider = IonQProvider(token=key)
    qpu_backend = provider.get_backend("ionq_qpu")
    qpu_job = qpu_backend.run(circ)
    job_id = qpu_job_bell.job_id()
    job = qpu_backend.retrieve_job(job_id)
    while job.status() is not JobStatus.DONE:
        print("Job status is not DONE")
        job = qpu_backend.retrieve_job(job_id)
        time.sleep(5)
    if qpu_job_bell.status() is JobStatus.DONE:
    
    
    qpu_result_bell = qpu_job_bell.result()
   
    else:
        