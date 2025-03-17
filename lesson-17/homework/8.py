import pandas as pd

df = pd.read_csv('data/movie.csv')

def duration(time):
    if time < 60:
        return "Short"
    elif 60 <= time < 120:
        return "Medium"
    else:
        return "Long"

df['duration_sorted'] = df['duration'].apply(duration)
print(df[['duration', 'duration_sorted']])