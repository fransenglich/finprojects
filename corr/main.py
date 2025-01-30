import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta   
 
import numpy as np

def compute_beta_IBM():
    market: pd.DataFrame = pd.read_csv("SPY.csv")
    asset = pd.read_csv("IBM.csv")

    combined = pd.concat([market["4. close"], asset["4. close"]], axis = 1)

    covar = combined.cov().iloc[0].iloc[1]
    var_m = market["4. close"].var()

    beta = covar / var_m

    print(covar, var_m, beta)
    # yields beta = 0.2973. According to Yahoo Finance 5Y monthly is 0.71,
    # so this is reasonable result.


# TODO actually compute monthly
def compute_beta_IBM5Y():
    start_date  = (datetime.today() - relativedelta(months = 12 * 5))

    market: pd.DataFrame = pd.read_csv("SPY5Y.csv", parse_dates = ['date'])
    market = market[market["date"] >= start_date]

    asset = pd.read_csv("IBM5Y.csv", parse_dates = ['date'])
    asset = asset[asset["date"] >= start_date]

    combined = pd.concat([market["4. close"], asset["4. close"]], axis = 1)

    covar = combined.cov().iloc[0].iloc[1]
    var_m = market["4. close"].var()

    beta = covar / var_m

    print(covar, var_m, beta)
    # Yields beta = 0.3190. According to Yahoo Finance 5Y monthly is 0.71.
    #
    # https://quant.stackexchange.com/questions/15797/how-does-yahoo-finance-calculate-beta


def main():
    compute_beta_IBM5Y()


main()