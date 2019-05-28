import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import IsolationForest

### READ FILE.CSV
sample1 = pd.read_csv('teste1.csv',usecols=['NR_VOTAVEL','RECEITA_TOTAL','QTD_VOTOS','CUSTO_VOTO','VR_TOTAL_BEM_CANDIDATO','Recursos_partido','Recursos_proprios','Recursos_outros_candidatos','Recursos_pessoas_fisicas','Rendimentos_aplicacoes','Financiamento_Coletivo','origens_nao_identificadas'], sep=',', low_memory=False, encoding='latin-1')

sample = sample1.values
print(sample.shape)
#Isolation Forest
##
clf = IsolationForest(max_samples='auto', contamination=0.10, n_jobs=-1, behaviour="new") 
 #contamination pega uma porcentagem da base
#n_jobs define quantos nucleos de hardware serão usados

clf.fit(sample)#ajustando o modelo do isolation forest para a base

scores = clf.decision_function(sample)#classifica os candidatos de -1 a 1 onde quanto mais proximo de -1 mais anomalo

predict  = clf.predict(sample) #classifica os candidatos só entre -1 e 1 mostrar em um gráfico
#testar varios valores de contamination, quando começar a pegar candidatos que não são anomalias já pode parar

prop = (float(predict.tolist().count(-1)) / float(len(sample))) #propo~ção de outliers/base pode tirar

num_outliers = predict.tolist().count(-1) #numero de outliers

# #print prop

print(num_outliers)

outliers = []
outliers_position = []

result = scores.tolist()

while len(outliers) < num_outliers:
    outliers.append(scores.min())
    #O +1 serve para encontrar o elemento na tabela com o cabecalho
    outliers_position.append(scores.argmin())
    scores = np.delete(scores, scores.argmin())
    
print('IF')
print(outliers_position)

candidatosComAnomalias = sample1.iloc[outliers_position]

candidatosComAnomalias.to_csv('candidatos-com-anomalias2.csv', sep=';', index=False)
