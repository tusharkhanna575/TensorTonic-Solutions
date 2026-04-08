import numpy as np
from scipy import stats
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean = np.mean(x)
    median = np.median(x)
    mode = stats.mode(x).mode

    return (mean, median, mode)