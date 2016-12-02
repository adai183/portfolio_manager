import pandas as pd
import matplotlib.pyplot as plt
import os
# Internal imports
import multiple_stocks as ms
import statistical_analysis  as sa


def is_bollinger_crasher(df):
    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm = sa.get_rolling_mean(df, window=20)
    # 2. Compute rolling standard deviation
    rstd = sa.get_rolling_std(df, window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = sa.get_bollinger_bands(rm, rstd)
    
    if df.get_value(-1) < lower_band.get_value(-1):
       return True
    else:
        return False

def bollinger_info(df):
    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm = sa.get_rolling_mean(df, window=20)
    # 2. Compute rolling standard deviation
    rstd = sa.get_rolling_std(df, window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = sa.get_bollinger_bands(rm, rstd)
    
    print df.name + " :"
    print df.get_value(-1)
    print lower_band.get_value(-1)
       

    


def test_run():
    dates = pd.date_range('2016-01-01', '2016-12-01')
    # Read data
    print "Get symbols ....."
    symbols = ms.read_symbols('data/Yahoo/Lists/nasdaq_all.txt')
    # Get stock data
    print 'Get stock data ......'
    df_test = ms.get_data(symbols, dates)
   
    # get bollinger crashers
    crashers_list = []
    for symbol in symbols:
        #print "analyzing: " + symbol
        if os.path.isfile(ms.symbol_to_path(symbol)) is False:
            print "Could not analyze {}".format(symbol)
        else:
            if is_bollinger_crasher(df_test[symbol]):
                print symbol
                crashers_list.append(symbol)
    for e in crashers_list:
        print e

    # for symbol in symbols:
    #     #print "analyzing: " + symbol
    #     if os.path.isfile(ms.symbol_to_path(symbol)) is False:
    #         print "Could not analyze {}".format(symbol)
    #     else:
    #         bollinger_info(df_test[symbol])


if __name__ == '__main__':
    test_run()
    
