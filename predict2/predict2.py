
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4] # Column "Adj_Close"
    returns = df['Adj_Close'].pct_change()

    plt.title("Prediction explorations")


    plt.subplot(311)
    plt.plot(closes)
    plt.legend(["Adjusted closes"])

    plt.subplot(312)
    plt.plot(returns)
    plt.legend(["Returns"])

    window_size = 5
    variance = returns.rolling(window_size).std() * (250 ** 0.5)

    plt.subplot(313)
    plt.plot(variance)

    print(f"variance: {variance}")
    print(f"type variance: {type(variance)}")

    # Graph stuff
    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.legend(["Variance"])
    plt.show()

main()
