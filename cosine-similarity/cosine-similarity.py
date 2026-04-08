import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    num = np.dot(a, b)
    deno = np.linalg.norm(a) * np.linalg.norm(b)
    if num == 0:
        return 0
    return num / deno