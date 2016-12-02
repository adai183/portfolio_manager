import pandas as pd
import matplotlib.pyplot as plt
import os
# Internal imports
import multiple_stocks as ms

def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe."""
    return df / df.ix[0,:]

def plot_data(df, title='Stock prices'):
    '''Plot stock prices'''
    ax = df.plot(title=title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()

def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    plot_data( df.ix[start_index:end_index, columns], title='Selected Data')
    plt.show()

def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    return pd.rolling_std(values, window=window)


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band

def plot_rolling_mean(df):
    # Plot data, retain matplotlib axis object
    ax = df.plot(title='Rolling Mean', label=df.name)

    # Compute rolling mean using a 20-day window
    rm = get_rolling_mean(df, window=20)

    # Add rolling mean to same plot
    rm.plot(label='Rolling Mean', ax=ax)

    #  Add axis lables and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')

    plt.show()

def bollinger_viz(df, window=20, pdf=False):
    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm = get_rolling_mean(df, window=window)

    # 2. Compute rolling standard deviation
    rstd = get_rolling_std(df, window=window)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm, rstd)

    # Plot raw values, rolling mean and Bollinger Bands
    ax = df.plot(title="Bollinger Bands", label=df.name)
    rm.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # mark specifix x-axis range
    ax.axvspan('2016-11-21', '2016-12-01', color='red', alpha=0.5)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')


    # Check wether to show the figure or save as pdf
    if pdf:
        plt.savefig('./information/Bollinger_crashers/'+df.name+'_bollinger_viz.pdf', format='pdf')
        plt.close()
    else:
        plt.show()

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy() #copy given df to match size and column names
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0  #set daily returns for row 0 to 0
    return daily_returns

def compute_cumulative_return(df, start_date, end_date):
    """Compute and return the cumulative return."""
    
    return daily_returns




def test_run():
    dates = pd.date_range('2016-01-01', '2016-12-01')
    # Read data
    print "Get symbols ....."
    symbols = ms.read_symbols('data/Yahoo/Lists/potential_buy.txt')
    # Get stock data
    print 'Get stock data ......'
    df_test = ms.get_data(symbols, dates)
    
    # do bollinger viz for all portfolio stocks
    for symbol in symbols:
        print "viz: " + symbol
        if os.path.isfile(ms.symbol_to_path(symbol)) is False:
            print "Could not analyze {}".format(symbol)
        else:
            bollinger_viz(df_test[symbol], window=20, pdf=True)

    # # compare daily results
    # plot_data(compute_daily_returns(df_test))



if __name__ == '__main__':
    test_run()
