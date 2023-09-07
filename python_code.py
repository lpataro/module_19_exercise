# código de geração do gráfico

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='blues')
  grafico.set(title='Evolução do Preço da Gasolina | SP/julho/2021', xlabel ='dia', ylabel='Preço')

plt.savefig('evolucao_preco_gasolina.png')