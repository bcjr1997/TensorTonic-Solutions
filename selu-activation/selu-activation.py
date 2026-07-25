import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    pass
    output = []

    for num in x:
        temp = num
        if num <= 0:
            temp = alpha * (math.exp(num) - 1)
        output.append(temp * lam)

    return output 
