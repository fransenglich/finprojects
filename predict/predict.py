
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class MyOLS:
    def __init__(self):
        self.intercept = None
        self.coefficients = None

    # X is an NxM array
    # y is Nx1
    def fit(self, X, y):
        ones = np.ones((len(X), 1))
        print(f"ones: {ones}")
        X = np.concatenate((ones, X), axis = 1)

        # The OLS equation:
        # (X^T * X)^-1 * X^T * y
        XT = X.T
        XTX = XT.dot(X)
        XTX_inv = np.linalg.inv(XTX)
        XTy = XT.dot(y)

        self.coefficients = XTX_inv.dot(XTy)


    def predict(self, X):
        # Match the model built in fit()
        ones = np.ones((len(X), 1))

        X = np.concatenate((ones, X), axis = 1)

        return X.dot(self.coefficients)

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4]
    #closes = closes[0:10] # TODO TEMP

    plt.plot(closes)

    plt.ylabel("Share value")
    plt.xlabel("Time")

    plt.title("Simple predictions")

    # Calculate return and plot a moving average of `days'-days.
    def calcAvgs(days):
        avgs = []

        for i in range(0, len(closes)):
            tail = max(0, i - days)
            val = sum(closes[tail:i]) / days
            avgs.append(val)

        return avgs

    plt.plot(calcAvgs(30))
    plt.plot(calcAvgs(30 * 9))

    # Calculate an estimator with OLS
    # ----------------- OLS -----------------
    X = list(range(len(closes)))
    y = closes

    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([1, 2, 3, 4, 5])


    print(f"y: {y}")
    print(f"X: {X}")

    mols = MyOLS()
    mols.fit(X, y)

    ypred = mols.predict(X)
    print(f"ypred: {ypred}")

    plt.plot(ypred)
    # ----------------- OLS -----------------


    # Graph stuff
    plt.legend(["Adjusted closes", "30-days MA", "9-months MA", "OLS prediction"])

    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.show()

main()
