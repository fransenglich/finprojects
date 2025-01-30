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


# TODO Correctly do monthly.
def compute_beta_IBM():
    start_date  = (datetime.today() - relativedelta(months = 12 * 5))

    market: pd.DataFrame = pd.read_csv("SPY.csv", parse_dates = ['date'])
    market = market[market["date"] >= start_date]
    print(market)
    market = market[market["date"].dt.day == start_date.day]
    print(market.to_string())

    asset = pd.read_csv("IBM.csv", parse_dates = ['date'])
    asset = asset[asset["date"] >= start_date]
    asset = asset[asset["date"].dt.day == start_date.day]

    combined = pd.concat([market["4. close"], asset["4. close"]], axis = 1)

    #print(combined)
    covar = combined.cov().iloc[0].iloc[1]
    var_m = market["4. close"].var()

    # B = cov(r_i, r_m)/var(r_m)
    beta = covar / var_m

    print(start_date, start_date.day, covar, var_m, beta)
    # Yields beta = 0.3101. According to Yahoo Finance 5Y monthly is 0.71.
    #
    # https://quant.stackexchange.com/questions/15797/how-does-yahoo-finance-calculate-beta


def main():
    compute_beta_IBM()


main()