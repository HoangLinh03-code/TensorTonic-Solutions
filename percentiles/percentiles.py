import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    np.sort(x)
    np.sort(q)
    return np.percentile(x,q, method='linear')