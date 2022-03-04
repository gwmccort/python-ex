import pandas as pd

df = pd.read_csv('Data/transactions.csv')

# add month, day & year
df[['month', 'day', 'year']] = df['Date'].str.split('/', expand=True)

df.to_csv('Data/new-tx.csv')
