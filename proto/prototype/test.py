# QSTK Imports
import QSTK.qstktools.YahooDataPull as yahoo
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def main():
    ''' Main Function'''
    # get latest stock data for portfolio
    yahoo.main(path='../../QSData/Yahoo/', symbolsPath='../../QSData/Yahoo/Lists/myPortfolio.txt')

    # Creating an object of DataAccess Class
    c_dataobj = da.DataAccess('Yahoo')

    # Getting a list of symbols from Lists
    ls_symbols = c_dataobj.get_symbols_from_list('myPortfolio')
    #print "Symbols from the list : ", ls_symbols


    ls_syms_toread = ['FB','GOOGL', 'INFI', 'MDSY', 'NVDA', 'TSLA']

    # List of TimeStamps to read
    # set start date
    # set start date to yesterday
    now = dt.datetime.now()
    startdate = dt.datetime(now.year, now.month, now.day, 16) - dt.timedelta(days=1)
    backtrace_range = 30

    ldt_timestamps =  [startdate - dt.timedelta(days=i) for i in range(0, backtrace_range)]
    ldt_timestamps.reverse()

    # Reading the data
    # By default it'll read data from the default data provided,
    # But a path can be provided using either an environment variable or
    # as a prarameter.
    df_close = c_dataobj.get_data(ldt_timestamps, ls_syms_toread, "close").dropna()

    """
    # Plotting the prices with x-axis=timestamps
    plt.clf()
    plt.plot(ldt_timestamps, df_close)
    plt.legend(ls_syms_toread)
    plt.ylabel('Adjusted Close')
    plt.xlabel('Date')
    plt.show()
    """
    print df_close


if __name__ == '__main__':
    main()
