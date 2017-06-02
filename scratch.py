import requests
import pandas as pd

#%% Constants:
api_key = '42pwVGC7x4TYPy1pCa4N'
columns = ['ticker','date','opening','high','low','closing','volume',
           'ex-dividend','split_ratio','adj_opening','adj_high',
           'adj_low','adj_closing','adj_volume']

#%% User input:
ticker = 'GOOG'

#%% Generated from input:
# Acquire data:
url = 'https://www.quandl.com/api/v3/datatables/' + \
    'WIKI/PRICES.json?ticker={0}&api_key={1}'.format(ticker,api_key)
r = requests.get(url)

data = pd.DataFrame(r.json()['datatable']['data'])
data.columns = columns

