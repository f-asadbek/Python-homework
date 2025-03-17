import pandas as pd

df = pd.read_csv('data/employee.csv')

def normalize(group):
    min_salary = group['BASE_SALARY'].min()
    max_salary = group['BASE_SALARY'].max()

    if min_salary == max_salary:
        group['NORMALIZED_SALARY'] = 1
    else:
        group['NORMALIZED_SALARY'] = (group['BASE_SALARY'] - min_salary) / (max_salary - min_salary)

    return group

df = df.groupby('DEPARTMENT', group_keys=False).apply(normalize)

print(df[['DEPARTMENT', 'BASE_SALARY', 'NORMALIZED_SALARY']])