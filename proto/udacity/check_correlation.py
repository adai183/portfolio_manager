import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# Internal imports
import multiple_stocks as ms
import statistical_analysis as sa

# Read data
symbols = ['CRUS', 'AAPL']
dates = pd.date_range('2016-01-01', '2016-12-01')
df = ms.get_data(symbols, dates)


# normalize price
normalized_price = sa.normalize_data(df)

# get dayly returns
na_rets = sa.compute_daily_returns(normalized_price)


plt.clf()
# check correlation CRUS : AAPL
plt.scatter(na_rets['AAPL'], na_rets['CRUS'], c='blue')
plt.show()
