import pandas as pd

df = pd.read_parquet('data/flights')

def flight_pipeline(df):
    df['DepDelay'] = pd.to_numeric(df['DepDelay'], errors='coerce')
    df = df.dropna(subset=['DepDelay'])

    df = df[df['DepDelay'] > 30]

    df['AirTime'].replace(0, 1, inplace=True)
    df['AirTime'].fillna(1, inplace=True)

    df['Delay_Per_Hour'] = df['DepDelay'] / df['AirTime']
    return df

df_processed = flight_pipeline(df)
print(df_processed[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())