import pandas as pd
from tabulate import tabulate
from conexao import get_db_connection
from sqlalchemy import text, Float

def execute_query(connection, query):
    with connection.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        columns = result.keys()
    return pd.DataFrame(rows, columns=columns)

def format_and_print(df):
    df['soma'] = df['soma'].apply(lambda x: f"{x:,.2f}")
    print(tabulate(df, headers='keys', tablefmt='psql'))

def main():
    df = pd.read_csv('.\\05\\transactions.csv', dtype={'amount': float})
    df = df[df['amount'] >= 0]

    conn = get_db_connection()
    df.to_sql('transactions', conn, if_exists='replace', index=False, dtype={'amount': Float})

    queries = [
        'SELECT currency as moeda, category as categoria, status, sum(amount) as soma FROM transactions Group By moeda, status, categoria ORDER BY moeda, categoria, status;',
        'SELECT currency as moeda, status, sum(amount) as soma FROM transactions Group By moeda, status ORDER BY status;',
        'SELECT currency as moeda, category as categoria, sum(amount) as soma FROM transactions Group By moeda, categoria ORDER BY categoria;'
    ]

    for query in queries:
        df = execute_query(conn, query)
        format_and_print(df)

if __name__ == "__main__":
    main()
