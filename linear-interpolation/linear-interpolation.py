def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    for index in range(len(values)):
        if values[index] is None:
            values[index] = values[0] + ((index - 0) / (len(values) - 1)) * (values[len(values) - 1] - values[0])

    return values