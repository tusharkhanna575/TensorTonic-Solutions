import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    ans = 0
    if len(x) != len(y):
        raise ValueError
    for i in range(len(x)):
        ans += abs(x[i] - y[i])
    return ans