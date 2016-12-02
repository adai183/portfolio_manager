"""Fill missing values"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Internal imports
import multiple_stocks as ms
import statistical_analysis as sa

def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    ##########################################################
    pass  # TODO: Your code here (DO NOT modify anything else)
    ##########################################################
    df_data.fillna(method='ffill', inplace=True)
    df_data.fillna(method='bfill', inplace=True)
    return df_data


def test_run():
    """Function called by Test Run."""
    # Read data
    symbol_list = ["SHOP", "GFNCP"]  # list of symbols
    start_date = "2005-12-31"
    end_date = "2016-12-07"
    dates = pd.date_range(start_date, end_date)  # date range as index
    df_data = ms.get_data(symbol_list, dates)  # get data for each symbol

    # Fill missing values
    fill_missing_values(df_data)

    # Plot
    sa.plot_data(df_data)


if __name__ == "__main__":
    test_run()
