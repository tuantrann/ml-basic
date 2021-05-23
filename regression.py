import pandas as pd
import quandl

df = quandl.get('EURONEXT/GOGL')
df = df[['Open', 'High', 'Low', 'Last', 'Volume']]

df['HL_PCT'] = (df['High'] - df['Last']) / df['Last'] * 100
df['PCT_change'] = (df['Last'] - df['Open']) / df['Open'] * 100

df = df[['Last', 'HL_PCT', 'PCT_change', 'Volume']]
# Feature is one column in the data (the input that is used to output the label)

forecast_col = 'Last'