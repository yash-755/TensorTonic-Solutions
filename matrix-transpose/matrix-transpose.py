import numpy as np

def matrix_transpose(A):
    A = np.array(A)

    if A.ndim != 2:
        raise ValueError("Input must be a 2D matrix")

    return A.T
    pass