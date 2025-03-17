import pandas as pd
import sqlite3

# connect 'chinook.db' database
connection = sqlite3.connect('data/chinook.db')

# select customers and invoices tables
df_customers = pd.read_sql('SELECT CustomerId, FirstName, LastName FROM customers', con=connection)
df_invoices = pd.read_sql('SELECT CustomerID, InvoiceId FROM invoices', con=connection)

connection.close()

# merging tables
df_merge = pd.merge(df_customers, df_invoices, how='inner', on='CustomerId')

# total number of invoices for each customer
invoice_count = (
    df_merge
    .groupby(['CustomerId', 'FirstName', 'LastName'])
    .size()
    .reset_index(name='Total Invoices')
    .sort_values(by='Total Invoices', ascending=False)
)

print(invoice_count)