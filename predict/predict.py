
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt

class MyOLS:
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
        XTy = XT.dot(y)

        # XTX^-1 . XTy
        self.coefficients = XTX_inv.dot(XTy)
        print(f"self.coefficients: {self.coefficients}")


    def predict(self, X):
        # Match the model built in fit()
        ones = np.ones((len(X), 1))

        X = np.concatenate((ones, X), axis = 1)

        return X.dot(self.coefficients)

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4] # Column "Adj_Close"

    plt.subplot(122)

    plt.plot(closes)

    plt.ylabel("Prices")
    plt.xlabel("Observations (time)")

    plt.suptitle("Predictions of NYSE ticker EW")

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

    # Calculate an estimator with OLS on prices
    # ----------------- START price OLS -----------------

    # Converts to a column of lists.
    def toColumn(lst):
        myRange = range(len(lst))

        retval = [[r] for r in myRange]

        return retval

    X = toColumn(closes)
    y = closes

    print(f"closes: {closes}")
    print(f"X: {X}")
    print(f"y: {y}")

    mols_prices = MyOLS()
    mols_prices.fit(X, y)

    ypred = mols_prices.predict(X)
    print(f"ypred: {ypred}")

    plt.plot(ypred)

    # Graph stuff
    plt.legend(["Adjusted closes", "30-days MA", "9-months MA", "OLS prediction"])

    # ----------------- END price OLS -----------------

    # https://poe.com/chat/3tfn7woo1ypl15zji5y
    # https://www.quora.com/Why-is-it-wrong-to-run-regressions-on-prices-and-right-to-run-them-on-returns
    def closesToReturns(closes):
        returns = []
        previous = 0.0

        for pt in closes:
            returns.append((pt - previous) / previous if previous else (pt - previous) / pt)
            previous = returns[-1]

        return returns

    plt.subplot(121)

    returns = df['Adj_Close'].pct_change()

    y = returns
    plt.plot(returns)

    X = toColumn(returns)

    mols_returns = MyOLS()
    mols_returns.fit(X, y)

    returns_ypred = mols_returns.predict(X)

    plt.plot(returns_ypred)

    plt.ylabel("Returns")
    plt.xlabel("Observations (time)")

    plt.legend(["Returns", "OLS fit"])

    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    print(f"coeffs: {mols_returns.coefficients}")
    print(f"mean: {stats.mean(returns)}")
    plt.show()

main()
