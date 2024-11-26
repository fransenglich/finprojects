

# Returns a list of the EWMAs for the returns `returns'
def compute_EWMAs(returns, weight = 0.94):

    print(f"type returns: {type(returns)}")
    print(f"returns: {returns}")
    retval = []
    previous_value = 0
    previous_i = None

    for i in range(len(returns))[1:]:
        previous_i = returns[i - 1]

        #print(f"i: {i}")
        new_value = weight * previous_value + (1 - weight) * previous_i ** 2
        previous_value = new_value
        retval.append(new_value)

    print(f"retval: {retval}")
    return retval

