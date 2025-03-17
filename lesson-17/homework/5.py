import pandas as pd

df = pd.read_parquet('data/flights')

df_group = df.groupby(['Year', 'Month']).agg(
    total_flights=('FlightNum', 'sum'),
    avg_delay=('ArrDelay', 'mean'),
    max_dep_delay=('DepDelay', 'max')
).reset_index()

print(df_group)