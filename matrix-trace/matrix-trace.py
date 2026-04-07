import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    ans = 0
    n,m = np.shape(A)
    for i in range(n):
        for j in range(i,m):
            if i == j:
                ans += A[i][j]

    return ans