# Homework-1 COP(6526)

This repository provides a Python implementation of parallel matrix-vector multiplication using MPI (Message Passing Interface). The code leverages the `mpi4py` library to distribute computation across multiple processes, enhancing performance and efficiency.

Report can be accessed at `Homework-1-Alex-Sciuto-COP6526.pdf` in the above files. 

```
assignment-1-cop6526/
├── myenv/
├── Homework-1-Alex-Sciuto-COP6526.pdf
├── assignment-1.ipynb
├── maxtrix-multiplication.py
├── requirements.txt
└── README.md
```

I included the python libraries used to run this code in `assignment-1.ipynb`. You can install those specific packages using the following commands:

```bash
pip install -r requirements.txt
```

## How to Run

1. **Clone the Repository:**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/DataWithAlex/assignment-1-cop6526.git
   cd assignment-1-cop6526
   ```

2.	**Run the Script with MPI:**

To execute the matrix-vector multiplication script across multiple processes, use the mpiexec command. For example, to run with `2` processes:

```bash
mpiexec -n 2 python matrix-multiplication.py
```

Replace `2` with the desired number of processes.

2.	**Run the Script with MPI in `assignment-1.ipynb:**

You can also execure the code directly within the `assignment-1.ipynb` notebook file by running the following command:

```bash
!mpiexec -n 2 python matrix-multiplication.py
```

3.	**Expected Output:**

For the above command, here is the output you would get:

```bash
2024-09-17 12:36:28 [INFO] Rank 1: Initialized empty matrix and vector placeholders.
2024-09-17 12:36:28 [INFO] Rank 1: Broadcasting vector from rank 0 to all processes.
2024-09-17 12:36:28 [INFO] Rank 0: Generated random matrix and vector.
2024-09-17 12:36:28 [INFO] Rank 0: Broadcasting vector from rank 0 to all processes.
2024-09-17 12:36:28 [INFO] Rank 0: Broadcast completed.
2024-09-17 12:36:28 [INFO] Rank 0: Scattering matrix: each process will receive 500 rows.
2024-09-17 12:36:28 [INFO] Rank 1: Broadcast completed.
2024-09-17 12:36:28 [INFO] Rank 1: Scattering matrix: each process will receive 500 rows.
2024-09-17 12:36:28 [INFO] Rank 1: Matrix scatter completed.
2024-09-17 12:36:28 [INFO] Rank 1: Performing local matrix-vector multiplication.
2024-09-17 12:36:28 [INFO] Rank 0: Matrix scatter completed.
2024-09-17 12:36:28 [INFO] Rank 0: Performing local matrix-vector multiplication.
2024-09-17 12:36:28 [INFO] Rank 1: Local result computed: [248.56277831 243.65929634 256.8254286  253.48377645 245.10409473]...
2024-09-17 12:36:28 [INFO] Rank 1: Local computation time: 0.000167 seconds
2024-09-17 12:36:28 [INFO] Rank 1: Gathering results from all processes.
2024-09-17 12:36:28 [INFO] Rank 0: Local result computed: [248.53301436 247.77791774 241.99700993 254.81127472 240.81912635]...
2024-09-17 12:36:28 [INFO] Rank 0: Local computation time: 0.000339 seconds
2024-09-17 12:36:28 [INFO] Rank 0: Gathering results from all processes.
Result of matrix-vector multiplication is computed.
2024-09-17 12:36:28 [INFO] Rank 0: Result of matrix-vector multiplication gathered: [248.53301436 247.77791774 241.99700993 254.81127472 240.81912635]...
2024-09-17 12:36:28 [INFO] Rank 0: Total computation time: 0.016090 seconds
```