import pandas as pd

# Task 1
df_json = pd.read_json('iris.json')
columns = [column.lower() for column in df_json.columns]
df_json.columns = columns
print(df_json[['sepallength', 'sepalwidth']])

# Task 2
df_xlsx = pd.read_excel('titanic.xlsx')
df_filtered = df_xlsx[df_xlsx['Age'] > 30]
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df_filtered)
number_of_genders = pd.Series(df_xlsx['Sex']).value_counts()
print(number_of_genders)

# Task 3
df_parquet = pd.read_parquet('flights')
print(df_parquet[['Origin', 'Dest', 'CarrierDelay']])
print("The number of unique destinations:", df_parquet['Dest'].nunique())

# Task 4
df_csv = pd.read_csv('movie.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df_csv[df_csv['duration'] > 120])
print(df_csv.sort_values(by='director_facebook_likes', ascending=False))
