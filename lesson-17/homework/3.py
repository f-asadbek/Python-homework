import pandas as pd

df = pd.read_excel('data/titanic.xlsx')

df_new = df.groupby('Pclass').agg(
    Average_Age=('Age', 'mean'),
    Total_Fare=('Fare', 'sum'),
    Passenger_Count=('PassengerId', 'count')
).reset_index()

print(df_new)