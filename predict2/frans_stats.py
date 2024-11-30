
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

# Question is how to define the window over `returns', currently it is not
# rolling, but expanding.
def compute_SD(returns):

    retval = []
    previous_value = 0
    mean = 0

    for i in range(len(returns)):
        r = returns[i]
        mean = sum(returns[0:i]) / (i + 1)

        print(f"mean: {mean}")

        sd = (r - mean) ** 2
        # FIXME
        retval.append(sd)

    return retval


class OLS:
    def __init__(self):
        self.intercept = None
        self.coefficients = None

    # @par X is an NxM array
    # @par y is Nx1
    # Writes result to @par coefficients.
    def fit(self, X, y):
        ones = np.ones((len(X), 1))
        print(f"ones: {ones}")
        X = np.concatenate((ones, X), axis = 1)

        # The OLS equation:
        # (X^T * X)^-1 * X^T * y
        XT = X.T
        XTX = XT.dot(X)
        print(f"XTX: {XTX}")
        XTX_inv = np.linalg.inv(XTX)
        print(f"XTX_inv: {XTX_inv}")
        XTy = XT.dot(y)
        print(f"XTy: {XTy}")

        # XTX^-1 . XTy
        self.coefficients = XTX_inv.dot(XTy)
        print(f"self.coefficients: {self.coefficients}")


    def predict(self, X):
        # Match the model built in fit()
        ones = np.ones((len(X), 1))

        X = np.concatenate((ones, X), axis = 1)

        return X.dot(self.coefficients)

