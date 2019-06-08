# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import IsolationForest

### READ FILE.CSV
sample1 = pd.read_csv('deputados-nao-eleitos-brasil-Normalizado.csv',usecols=['SQ_CANDIDATO','CD_GENERO_N','CD_GRAU_INSTRUCAO_N','NR_PARTIDO_N','CD_OCUPACAO_N','CD_SITUCAO_N','CARGO_N','RECEITA_TOTAL_N','QTD_VOTOS_N','CUSTO_VOTO_N','DESPESA_CONTRATADA_N','VR_TOTAL_BEM_CANDIDATO_N'], sep=';', low_memory=False, encoding='latin-1').fillna(value = 0)

sample = sample1.values
print(sample.shape)
#Isolation Forest
##
clf = IsolationForest(max_samples='auto', contamination=0.0060, n_jobs=-1, behaviour="new") 
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

candidatosComAnomalias.to_csv('candidatos-com-anomalias0060.csv', sep=';', index=False)
