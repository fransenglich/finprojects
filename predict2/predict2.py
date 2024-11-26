
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4] # Column "Adj_Close"
    returns = df['Adj_Close'].pct_change()
    print(f"returns: {returns}")

    plt.title("Prediction explorations")

    plt.subplot(411)
    plt.plot(closes)
    plt.legend(["Adjusted closes"])

    plt.subplot(412)
    plt.plot(returns)
    plt.legend(["Returns"])

    window_size = 2 # FIXME 1 leads to NaN for all data, don't know why.
    print(f"window_size: {window_size}")
    sd = returns.rolling(window_size).std() * (250 ** 0.5)

    print(f"sd: {sd}")
    print(f"type sd: {type(sd)}")

    plt.subplot(413)
    plt.plot(sd)
    plt.legend(["Standard deviation"])

    # ----------------------------------- EWMA

    # It is expected that returns is returns in the form of a pandas Series
    # object.
    # Returns a list of the EWMAs
    def compute_EWMAs(returns):
        print(f"type returns: {type(returns)}")
        print(f"returns: {returns}")
        L = 0.94 # The lambda parameter
        retval = []
        as_list = returns.to_list()
        previous_value = 0

        for i in returns[1:]:
            #print(f"i: {i}")
            new_value = L * previous_value + (1 - L) * i ** 2
            previous_value = new_value
            retval.append(new_value)

        print(f"retval: {retval}")
        return retval

    ewmas = compute_EWMAs(returns)

    plt.subplot(414)
    plt.plot(ewmas)
    plt.legend(["EWMA"])

    # ----------------------------------- Onwards
    # Now we have our nice time series `returns' and variance in `ewmas'.

    # ----------------------------------- Graph stuff
    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.show()

main()
