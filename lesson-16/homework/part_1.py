import sqlite3
import pandas as pd

# Task 1
with sqlite3.connect('chinook.db') as connection:
    df_customers = pd.read_sql("SELECT * FROM customers", con=connection)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    print(df_customers.head(10))

# Task 2
df_json = pd.read_json('iris.json')
print("The shape of json file:", df_json.shape)
print("Column names:", df_json.columns.to_list())

# Task 3
df_xlsx = pd.read_excel('titanic.xlsx')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df_xlsx.head())

# Task 4
df_parquet = pd.read_parquet('flights')
print(df_parquet.info())

# Task 5
df_csv = pd.read_csv('movie.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df_csv.sample(10))