
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
    #print(f"returns: {returns}")

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


    # ----------------------------------- OLS
    # Goal: list of B, predict next value (+1) with the B.
    # Then we have an OLS prediction

    # Our list of regression coefficients
    B = []

    ols_window_size = 20 * 2 # 2 financial months
    all_time = list(range(len(returns)))

    # We do a rolling window and compute an OLS B for every step.
    for i in range(len(returns) - ols_window_size):
        print(f"i: {i}")

        y = returns[i + ols_window_size:i + ols_window_size * 2]

        X = all_time[i + ols_window_size:i + ols_window_size * 2]

        print(f"len(y): {len(y)}")
        print(f"len(X): {len(X)}")

        if len(X) < ols_window_size:
            break

        model = sm.OLS(y, X)
        res = model.fit()

        # We only have one independent, so one coef.
        B.append(res.params.iloc[0])

        print(f"len(y): {len(y)}")
        print(f"len(X): {len(X)}")

    print(f"len(B): {len(B)}")
    print(f"len(returns): {len(returns)}")

    # y_hat(t) = B * x(t)
    y_hat = [B[i] * returns[i + ols_window_size] for i in range(len(B))]


    # ----------------------------------- Graph stuff
    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.show()

main()
