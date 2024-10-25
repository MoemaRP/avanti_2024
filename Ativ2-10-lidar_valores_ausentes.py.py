import pandas as pd

print(df.isnull().sum())
##Uma vez identificados os valores ausentes, algumas alternaivas são possíveis:

#Remover linhas com valores ausentes
df_clean = df.dropna()

#Remover colunas com qualquer valor ausente
df_clean = df.dropna(axis=1)

# Preencher com um valor específico
df_filled = df.fillna(0)

# Preencher com a média da coluna
df['coluna'] = df['coluna'].fillna(df['coluna'].mean())

# Preencher com a mediana
df['coluna'] = df['coluna'].fillna(df['coluna'].median())

# Preencher com o valor mais frequente (moda)
df['coluna'] = df['coluna'].fillna(df['coluna'].mode()[0])

#Preencher usando o valor anterior
df_ffill = df.fillna(method='ffill')

#Preencher usando o próximo valor
df_bfill = df.fillna(method='bfill')

#Fazer interpolação linear
df_interp = df.interpolate()

# Substituir NaN por uma nova categoria 'Desconhecido'
df['categoria'] = df['categoria'].fillna('Desconhecido')
