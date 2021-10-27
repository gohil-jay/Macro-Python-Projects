"""
!pip install quandl
"""

import quandl, math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

auth_tok = "TOKEN_HERE"
data = quandl.get("EOD/AAPL", trim_start = "2000-12-12", trim_end = "2020-12-30", authtoken=auth_tok)

data = data[['Adj_Open',  'Adj_High',  'Adj_Low',  'Adj_Close', 'Adj_Volume']]
data['HL_PCT'] = (data['Adj_High'] - data['Adj_Low']) / data['Adj_Close'] * 100.0
data['PCT_change'] = (data['Adj_Close'] - data['Adj_Open']) / data['Adj_Open'] * 100.0
data = data[['Adj_Close', 'HL_PCT', 'PCT_change', 'Adj_Volume']]

print("Visualizing correlation between features using heatmap -->\n")
sns.heatmap(data.corr(method='pearson'), cmap='Blues')
