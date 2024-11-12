
# Description

This does some basic statistics of a stock ticker. Picked inspiration from this page:

<https://www.getsuper.ai/post/6-financial-analytics-project-ideas-for-resume>

The code was inspired by a LinkedIn post by Riwaj Pokhrel, Ph.D.

Using OLS is unsuitable for this dataset, because its assumptions doesn't hold. For instance linearity and homoscedasticity are not fulfilled, based on eyeballing. I believe this is the explanation to that the intercept is negative.

# Dataset

See file dataset.csv. Historical stock prices of Edwards Lifesciences Corporation (EW) within time span from 2000-03-26 to 2017-09-09.

The dataset has no blanks, and is considered clean.

# Result

![Output graph](output_graph.svg)

