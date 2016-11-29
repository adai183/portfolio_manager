import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

ls_symbols = ['FB','GOOGL', 'NVDA', 'TSLA']
dt_start = dt.datetime(2016, 1, 1)
dt_end = dt.datetime(2016, 11, 28)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))

na_price = d_data['close'].values

# normalize price
na_normalized_price = na_price / na_price[0, :]
# plt.plot(ldt_timestamps, na_price)
# plt.show()

# get dayly returns
na_rets = na_normalized_price.copy()
tsu.returnize0(na_rets)
# plt.plot(ldt_timestamps, na_rets)
# plt.show()

plt.clf()
# check correlation GOOGL : FB
plt.scatter(na_rets[:, 0], na_rets[:, 1], c='blue')
plt.show()
