import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Criar a tabela, caso não exista
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
""")
conn.commit()

# Inserir os dados, se necessário
# cursor.executemany('''
# INSERT INTO clientes (nome, idade, cidade) VALUES (?, ?, ?)
# ''', [
#     ('Ana Souza', 25, 'São Paulo'),
#     ('Carlos Mendes', 34, 'Rio de Janeiro'),
#     ('Mariana Lima', 29, 'Belo Horizonte'),
#     ('João Pereira', 42, 'Curitiba'),
#     ('Fernanda Alves', 31, 'Porto Alegre'),
#     ('Ricardo Martins', 27, 'São Paulo'),
#     ('Paula Fernandes', 38, 'Brasília'),
#     ('Lucas Oliveira', 22, 'Salvador'),
#     ('Camila Rocha', 35, 'Recife'),
#     ('Bruno Santos', 40, 'Fortaleza')
# ])
# conn.commit()

# Agora, faça a consulta
cursor.execute('SELECT * from clientes')

# Exibir os resultados
for linha in cursor.fetchall():
    print(linha)

# Fechar a conexão
conn.close()
