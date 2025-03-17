import pandas as pd

# read csv file
df = pd.read_csv('data/movie.csv')

# grouping
df_group = df.groupby(['color', 'director_name']).agg(
    total_reviews=('num_critic_for_reviews', 'sum'),
    avg_duration=('duration', 'mean')
).reset_index()

print(df_group)