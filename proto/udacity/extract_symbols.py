import pandas as pd

df_temp = pd.read_csv('./data/companylist.csv')


with pd.option_context('display.max_rows', 9999999999999999, 'display.max_columns', 0):
    f = open('./data/Yahoo/Lists/nasdaq_all.txt', 'a')
    print >> f, df_temp['Symbol'].to_string(index=False)
    f.close()
