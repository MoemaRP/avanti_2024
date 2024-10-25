import pandas as pd

coluna_selecionada = df['nome_da_coluna']
linhas_filtradas = df[df['nome_da_coluna'] > valor]
resultado = df.loc[df['nome_da_coluna'] > valor, 'outra_coluna']