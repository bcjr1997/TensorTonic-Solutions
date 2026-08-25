import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    p, q = np.array(p, dtype=float), np.array(q, dtype=float)
    
    positive_mask = p > 0

    p_positive = p[positive_mask]

    q_positive = np.clip(q[positive_mask], eps, None)

    return float(np.sum(p_positive * np.log(p_positive/q_positive)))
    