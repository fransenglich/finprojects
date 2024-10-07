
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
numarray = df.to_numpy()

#print(numarray)

closes = numarray[:, 4]
plt.plot(closes)

plt.ylabel('Adjusted close')
plt.xlabel('Date')

# giving a title to my graph
plt.title('Simple predictions')

avgs = []

# Calculate and plot a moving average 30-days.

for i in range(0, len(closes)):
    tail = max(0, i - 30)
    val = sum(closes[tail:i]) / 30
    avgs.append(val)

plt.plot(avgs)

# function to show the plot
plt.show()

# Display the DataFrame (table)
#print(df)


