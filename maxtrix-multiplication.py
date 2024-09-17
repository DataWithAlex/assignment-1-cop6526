from mpi4py import MPI
import numpy as np
import logging
import time  # Import the time module for tracking computation time

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Set up logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()

# Matrix and vector sizes
n = 1000  # Change this size for larger matrices

# Start tracking total computation time
total_start_time = time.time()

if rank == 0:
    # Master process: generate random matrix and vector
    matrix = np.random.rand(n, n)
    vector = np.random.rand(n)
    logger.info(f"Rank {rank}: Generated random matrix and vector.")
else:
    # Other processes: initialize empty matrix and vector
    matrix = None
    vector = np.empty(n, dtype='d')
    logger.info(f"Rank {rank}: Initialized empty matrix and vector placeholders.")

# Broadcast the vector to all processes
logger.info(f"Rank {rank}: Broadcasting vector from rank 0 to all processes.")
comm.Bcast(vector, root=0)
logger.info(f"Rank {rank}: Broadcast completed.")

# Scatter the matrix to all processes
rows_per_process = n // size
local_matrix = np.empty((rows_per_process, n), dtype='d')
logger.info(f"Rank {rank}: Scattering matrix: each process will receive {rows_per_process} rows.")
comm.Scatter(matrix, local_matrix, root=0)
logger.info(f"Rank {rank}: Matrix scatter completed.")

# Start timing the local computation
local_start_time = time.time()

# Perform local matrix-vector multiplication
logger.info(f"Rank {rank}: Performing local matrix-vector multiplication.")
local_result = np.dot(local_matrix, vector)

# End timing the local computation
local_end_time = time.time()
local_computation_time = local_end_time - local_start_time

logger.info(f"Rank {rank}: Local result computed: {local_result[:5]}...")  # Print only the first 5 elements for brevity
logger.info(f"Rank {rank}: Local computation time: {local_computation_time:.6f} seconds")

# Gather the local results back to the master process
if rank == 0:
    result = np.empty(n, dtype='d')
else:
    result = None

logger.info(f"Rank {rank}: Gathering results from all processes.")
comm.Gather(local_result, result, root=0)

# End tracking total computation time
total_end_time = time.time()
total_computation_time = total_end_time - total_start_time

if rank == 0:
    logger.info(f"Rank {rank}: Result of matrix-vector multiplication gathered: {result[:5]}...")  # Print only the first 5 elements for brevity
    logger.info(f"Rank {rank}: Total computation time: {total_computation_time:.6f} seconds")
    print("Result of matrix-vector multiplication is computed.")