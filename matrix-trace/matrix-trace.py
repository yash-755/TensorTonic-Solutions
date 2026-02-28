import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A = np.array(A)

    if A.ndim != 2:
        raise ValueError("Input must be a 2D matrix")

    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square")

    return float(np.trace(A))
    pass
