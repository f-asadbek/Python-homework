import pandas as pd

df = pd.read_csv('data/movie.csv')

df_1 = df[['director_name', 'color']]
df_2 = df[['director_name', 'num_critic_for_reviews']]

df_left = pd.merge(df_1, df_2, on='director_name', how='left')
df_outer = pd.merge(df_1, df_2, on='director_name', how='outer')

print("The number of rows in left joined dataframe: ", len(df_left))
print("The number of rows in outer joined dataframe: ", len(df_outer))