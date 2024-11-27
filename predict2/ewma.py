
# Returns a list of the EWMAs (variance) for the returns `returns'
def compute_EWMA(returns, weight = 0.94, mean = 0):
    print(f"type returns: {type(returns)}")
    print(f"returns: {returns}")

    retval = []
    previous_value = 0

    for i in returns:
        new_value = weight * previous_value + (1 - weight) * ((i - mean) ** 2)
        previous_value = new_value
        retval.append(new_value)

    print(f"retval: {retval}")
    return retval

