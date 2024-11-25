
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("dataset.csv")
    numarray = df.to_numpy()

    closes = numarray[:, 4] # Column "Adj_Close"

    plt.subplot(122)

    plt.plot(closes)

    plt.subplot(121)

    returns = df['Adj_Close'].pct_change()

    plt.plot(returns)

    plt.savefig("output_graph.png")
    plt.savefig("output_graph.svg")

    plt.show()

main()
