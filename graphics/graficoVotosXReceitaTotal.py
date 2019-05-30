import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sample1 = pd.read_csv('deputados.csv',usecols=['SQ_CANDIDATO','NR_VOTAVEL','CARGO_N','SITUCAO_N','RECEITA_TOTAL','QTD_VOTOS','CUSTO_VOTO','VR_TOTAL_BEM_CANDIDATO','Recursos_partido','Recursos_proprios','Recursos_outros_candidatos','Recursos_pessoas_fisicas','Rendimentos_aplicacoes','Financiamento_Coletivo','origens_nao_identificadas','Comercio_bens_ou_eventos','Doacoes_Internet','DESPESA_CONTRATADA'], sep=';', low_memory=False, encoding='latin-1').fillna(value = 0)
# print(sample1)

plt.scatter(sample1['QTD_VOTOS'], sample1['RECEITA_TOTAL'])
plt.xlabel('Quantidade de Votos')
plt.ylabel('Receita Total')
plt.title('Candidatos a Deputados 2018')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.show()