
import pandas as pd
import numpy as np
import frans_stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4] # Column "Adj_Close"
    returns = df['Adj_Close'].pct_change()
    print(f"returns: {returns}")

    # Get rid of nan, pct_change() produced it, computing the EWMA fails with it.
    returns[0] = 0

    plt.title("Prediction explorations")

    plt.subplot(411)
    plt.plot(closes)
    plt.legend(["Adjusted closes"])

    plt.subplot(412)
    plt.plot(returns)
    plt.legend(["Returns"])

    # Smallest possible to get high resolution. SD is undefined for 1 value.
    sd_window_size = 2

    print(f"sd_window_size: {sd_window_size}")
    sd = returns.rolling(sd_window_size).std() * (250 ** 0.5)

    print(f"sd: {sd}")
    print(f"type sd: {type(sd)}")

    plt.subplot(413)
    plt.plot(sd)
    plt.legend(["Standard deviation"])

    # ----------------------------------- EWMA

    ewmas = frans_stats.compute_EWMA(returns)

    plt.subplot(414)
    plt.plot(ewmas)
    plt.legend(["EWMA"])

    # ----------------------------------- Onwards
    # Now we have our nice time series `returns' and volatility in `ewmas'.

    # Goal: list of B, predict next value (+1) with the B.
    # Then we have an OLS prediction

    B = []

    ols_window_size = 20 * 2 # 2 finance months

    retlen = len(returns)

    # Discrete time, our X
    fulltime = list(range(ols_window_size, retlen - ols_window_size))
    print(f"len(fulltime): {len(fulltime)}")
    print(f"len(returns): {len(returns)}")

    fulltime2 = list(range(ols_window_size, retlen))

    # A rolling window
    for i in fulltime:
        y = returns[i:i + ols_window_size]

        print(f"i: {i}")
        print(f"fulltime.len: {len(fulltime)}")
        X = fulltime2[i:i + ols_window_size]

        print(f"y.len: {len(y)}")
        print(f"X.len: {len(X)}")

        model = sm.OLS(y, X)
        res = model.fit()

        B.append(res.params.iloc[0])

    print(type(B))

    print(dir(res))
    print(res.summary())
    print(f"params: {res.params}")

    # ----------------------------------- Graph stuff
    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.show()

main()
