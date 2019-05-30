from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

sample1 = pd.read_csv('deputados.csv',usecols=['SQ_CANDIDATO','NR_VOTAVEL','CARGO_N','SITUCAO_N','RECEITA_TOTAL','QTD_VOTOS','CUSTO_VOTO','VR_TOTAL_BEM_CANDIDATO','Recursos_partido','Recursos_proprios','Recursos_outros_candidatos','Recursos_pessoas_fisicas','Rendimentos_aplicacoes','Financiamento_Coletivo','origens_nao_identificadas','Comercio_bens_ou_eventos','Doacoes_Internet','DESPESA_CONTRATADA'], sep=';', low_memory=False, encoding='latin-1').fillna(value = 0)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(sample1['QTD_VOTOS'], sample1['RECEITA_TOTAL'], sample1['CARGO_N'], c='r', marker='o')

ax.set_xlabel('Qtd Votos')
ax.set_ylabel('Rec Total')
ax.set_zlabel('Cargo')

plt.show()