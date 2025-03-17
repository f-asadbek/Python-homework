import pandas as pd

df = pd.read_excel('data/titanic.xlsx')

def titanic_pipeline(df):
    df = df[df['Survived'] == 1]

    df['Age'].fillna(df['Age'].mean(), inplace=True)

    df['Fare_Per_Age'] = df['Fare'] / df['Age']

    return df

df_processed = titanic_pipeline(df)
print(df_processed[['Survived', 'Age', 'Fare', 'Fare_Per_Age']])