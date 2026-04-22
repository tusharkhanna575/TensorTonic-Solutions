from math import log1p

def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    return [log1p(i) for i in values]