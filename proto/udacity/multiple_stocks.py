'''Utility functions'''

import os
import pandas as pd

def read_symbols(s_symbols_file):
    '''Read a list of symbols'''
    ls_symbols = []
    ffile = open(s_symbols_file, 'r')
    for line in ffile.readlines():
        str_line = str(line)
        if str_line.strip():
            ls_symbols.append(str_line.strip())
    ffile.close()
    return ls_symbols

def symbol_to_path(symbol, base_dir='data/Yahoo'):
    '''Return CSV file path given ticker symbol.'''
    return os.path.join(base_dir, '{}.csv'.format(str(symbol)))


def get_data(symbols, dates):
    '''Read stock data (adjusted close) for given symbols from CSV files.'''
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        if os.path.isfile(symbol_to_path(symbol)) :
            print "getting data for: {}".format(symbol)
            df_temp = pd.read_csv(symbol_to_path(symbol), index_col = 'Date',
                              parse_dates = True, usecols = ['Date','Adj Close'],
                              na_values = ['nan'])
            df_temp = df_temp.rename(columns = {'Adj Close':symbol})
            df = df.join(df_temp)
            if symbol == 'SPY': #drop dates when SPY did not trade
        	    df = df.dropna(subset=['SPY'])
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2016-01-01', '2016-11-28')

    # Choose stock symbols to read
    symbols = read_symbols('data/Yahoo/Lists/portfolio.txt')

    # Get stock data
    df = get_data(symbols, dates)
    #print df

    # Slicing: row slicing for dates
    # print df.ix['2016-10-01':'2016-11-28' ]
    #
    # Slicing: column slicing for symbols
    # print df[['MDSY', 'GOOGL']]
    # print df['GOOGL']
    #
    # Slicing: row and column
    # print df.ix['2016-11-01':'2016-11-28', ['MDSY', 'GOOGL'] ]

if __name__ == '__main__':
    test_run()
