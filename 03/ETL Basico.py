import pandas as pd
import sqlite3

df = pd.read_csv('.\\03\\funcionarios.csv')

df['NOME'] = df['NOME'].str.upper()

conn = sqlite3.connect('.\\03\\funcionarios.db')

df.to_sql('funcionarios', conn, if_exists='replace', index=False)

loaded_data = pd.read_sql('SELECT * FROM funcionarios', conn)
print(loaded_data)
conn.close()