import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x, dtype=float)
    
    # 1. Operate on the last axis (-1 handles both 1D and 2D rows automatically)
    # 2. keepdims=True ensures the shape matches for proper broadcasting subtraction/division
    x_max = np.max(x, axis=-1, keepdims=True)
    exp_x = np.exp(x - x_max)
    
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)