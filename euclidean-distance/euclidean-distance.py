import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    ans = 0
    if len(x) != len(y):
        raise ValueError
    for i in range(min(len(x), len(y))):
        ans += (x[i] - y[i]) ** 2
    return ans ** 0.5