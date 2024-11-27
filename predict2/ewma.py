

# Returns a list of the EWMAs (variance) for the returns `returns'
# mean is assumed to be 0.
def compute_EWMA(returns, weight = 0.94):
    print(f"type returns: {type(returns)}")
    print(f"returns: {returns}")

    retval = []
    previous_value = 0

    for i in returns:
        new_value = weight * previous_value + (1 - weight) * (i ** 2)
        previous_value = new_value
        retval.append(new_value)

    print(f"retval: {retval}")
    return retval

