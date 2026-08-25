import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    y_true, y_score = np.array(y_true), np.array(y_score)
    sample_loss = np.maximum(0, margin - (y_true * y_score))

    if reduction == "mean":
        return float(sample_loss.mean())
    elif reduction == "sum":
        return float(sample_loss.sum())
    elif reduction == "none":
        return sample_loss  # Note: Returns np.ndarray if raw elementwise loss is requested
    else:
        raise ValueError(f"Invalid reduction option: {reduction}. Expected 'mean', 'sum', or 'none'.")