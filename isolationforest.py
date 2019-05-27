import pandas as pd
import numpy as np
import csv
from sklearn.ensemble import IsolationForest

### READ FILE.CSV
sample1 = pd.read_csv('deputados.csv',usecols=['NR_VOTAVEL','CARGO_N','SITUCAO_N','RECEITA_TOTAL','QTD_VOTOS','CUSTO_VOTO','VR_TOTAL_BEM_CANDIDATO','Recursos_partido','Recursos_proprios','Recursos_outros_candidatos','Recursos_pessoas_fisicas','Rendimentos_aplicacoes','Financiamento_Coletivo','origens_nao_identificadas','Comercio_bens_ou_eventos','Doacoes_Internet','DESPESA_CONTRATADA'], sep=';', low_memory=False, encoding='latin-1').fillna(value = 0)

sample = sample1.values

#Isolation Forest
##
clf = IsolationForest(max_samples='auto', contamination=0.005, n_jobs=-1, behaviour="new", verbose=1)
clf.fit(sample)

scores = clf.decision_function(sample)

predict  = clf.predict(sample)

prop = (float(predict.tolist().count(-1)) / float(len(sample)))

num_outliers = predict.tolist().count(-1)

#print prop

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

print(candidatosComAnomalias)

candidatosComAnomalias.to_csv('candidatos-com-anomalias.csv', sep=';', index=False)
