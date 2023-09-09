# código de geração do gráfico

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico.set(title='Preços da Gasolina em Julho 2021, São Paulo', xlabel='Dia do Mês', ylabel='Preço do dia')
plt.savefig('gasolina.png')
