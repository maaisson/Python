import pandas as pd

# Realiza a leitura do csv direto no pandas
df = pd.read_csv('dataset_filmes_gigante.csv', encoding='utf-8')

# remove os filmes com ano maior que 2025
df = df[df['Ano'] < 2025]

# remove  os filmes com duração negativa
df = df[df['Duração (min)'] >= 0]

# remove os filmes com nota IMDB negativa
df=df[df['Nota IMDB'].between(0, 10)]

# mostra a quantindade de filmes por diretor
filmes_por_diretor = df['Diretor'].value_counts()
print("Número de filmes por diretor:")
print(filmes_por_diretor)

# Mostra os filmes com as melhores notas no IMDB
melhores_filmes = df.groupby('Título')['Nota IMDB'].mean().sort_values(ascending=False)
print("\nFilmes com a melhor nota no IMDb:")
print(melhores_filmes)

# Mostra os filmes com as piores notas no IMDB
piores_filmes = df.groupby('Título')['Nota IMDB'].mean().sort_values(ascending=True)
print("\nFilmes com a pior nota no IMDb:")
print(piores_filmes)

# Mostra o filme com a maior duração
filme_mais_longo = df.loc[df['Duração (min)'].idxmax()]
print("\nFilme com maior duração:")
print(filme_mais_longo)

# Mostra o filme com a menor duração
filme_mais_curto = df.loc[df['Duração (min)'].idxmin()]
print("\nFilme com menor duração:")
print(filme_mais_curto)

# Salva o csv tratado após o processo de ETL
df.to_csv('dataset_filmes_corrigido.csv', index=False, encoding='utf-8')
