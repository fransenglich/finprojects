
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4] # Column "Adj_Close"
    returns = df['Adj_Close'].pct_change()

    plt.subplot(311)
    plt.plot(closes)

    plt.subplot(312)
    plt.plot(returns)

    window_size = 1
    variance = returns.rolling(window_size).std() * (250 ** 0.5)

    plt.subplot(313)
    plt.plot(variance)
    print(f"variance: {variance}")

    # Graph stuff
    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.show()

main()
