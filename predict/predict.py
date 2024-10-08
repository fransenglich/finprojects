
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
numarray = df.to_numpy()

closes = numarray[:, 4]

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

# Let's calculate an estimator with OLS
y = range(len(closes))
Bhat = y/closes
print("Bhat: " + str(Bhat))

plt.legend(["Adjusted closes", "30-days MA", "9-months MA"])

plt.savefig("output_graph.png")
plt.savefig("output_graph.svg")

plt.show()
