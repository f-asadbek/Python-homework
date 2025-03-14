import pandas as pd

# Task 1
df_json = pd.read_json('iris.json')
mean_value = df_json.mean(numeric_only=True)
median_value = df_json.median(numeric_only=True)
standard_deviation_value = df_json.std(numeric_only=True)

print(f"""
Mean Value: \n{median_value},
Median Value: \n{median_value},
Standard Deviation: \n{standard_deviation_value}
    """)

# Task 2
df_xlsx = pd.read_excel('titanic.xlsx')
df_xlsx.dropna()
min_age = df_xlsx['Age'].min()
max_age = df_xlsx['Age'].max()
sum_age = df_xlsx['Age'].sum()

print(f"""
Min age: \n{min_age}
Max age: \n{max_age}
Sum of ages: \n{sum_age}
""")

# Task 3
df_csv = pd.read_csv('movie.csv')
max_likes = df_csv['director_facebook_likes'].max()
longest_movies = df_csv.nlargest(5, 'duration')[['director_name']]
print("The highest liked movie:", max_likes)
print("Top 5 the longest movies and their director names:\n", longest_movies)

# Task 4
df_parquet = pd.read_parquet('flights')
missing_values = df_parquet.isnull().sum()
print("Missing values in each column:\n", missing_values)
df_parquet.fillna(df_parquet.mean(numeric_only=True), inplace=True)
print("\nMissing values after filling:\n", df_parquet.isnull().sum())