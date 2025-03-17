import pandas as pd

df = pd.read_excel('data/titanic.xlsx')

#function
def func(age):
    return 'Child' if age < 18 else 'Adult'

df['Age_Group'] = df['Age'].apply(func)

print(df[['Age', 'Age_Group']])