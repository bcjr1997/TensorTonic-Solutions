def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    output = []
    for num in x:
        temp = num
        if num <= 0:
            temp = alpha * (math.exp(num) - 1)
        output.append(temp)
    return output