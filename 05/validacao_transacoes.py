import pandas as pd
from tabulate import tabulate
from conexao import get_db_connection
from sqlalchemy import text, Float

df = pd.read_csv('.\\05\\transactions.csv', dtype={'amount': float})

df = df[df['amount'] >= 0]

conn = get_db_connection()

df.to_sql('transactions', conn, if_exists='replace', index=False, dtype={'amount': Float})

with conn.connect() as connection:
    t = text('SELECT currency as moeda, category as categoria, status, sum(amount) as soma FROM transactions Group By moeda, status, categoria ORDER BY categoria, status;')    
    result = connection.execute(t)	
    rows = result.fetchall()
    columns = result.keys()

df = pd.DataFrame(rows, columns=columns)
df['soma'] = df['soma'].apply(lambda x: f"{x:,.2f}")
print(tabulate(df, headers='keys', tablefmt='psql'))

with conn.connect() as connection:
    t = text('SELECT currency as moeda, status, sum(amount) as soma FROM transactions Group By moeda, status ORDER BY status;')    
    result = connection.execute(t)	
    rows = result.fetchall()
    columns = result.keys()

df = pd.DataFrame(rows, columns=columns)

df['soma'] = df['soma'].apply(lambda x: f"{x:,.2f}")

print(tabulate(df, headers='keys', tablefmt='psql'))

with conn.connect() as connection:
    t = text('SELECT currency as moeda, category as categoria, sum(amount) as soma FROM transactions Group By moeda, categoria ORDER BY categoria;')    
    result = connection.execute(t)	
    rows = result.fetchall()
    columns = result.keys()

df = pd.DataFrame(rows, columns=columns)
df['soma'] = df['soma'].apply(lambda x: f"{x:,.2f}")
print(tabulate(df, headers='keys', tablefmt='psql'))





