# -*- coding: latin-1 -*-
import pandas as pd
import csv
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf8')

sample = pd.read_csv('candidatos.csv',usecols=['NR_CANDIDATO','DT_NASCIMENTO','DS_GRAU_INSTRUCAO','DS_GENERO','DS_ESTADO_CIVIL','DS_COR_RACA','NM_MUNICIPIO_NASCIMENTO'], sep=';', low_memory=False, encoding='latin-1').fillna(value = 0)
values = sample.values

outliers = pd.read_csv('candidatos-com-anomalias2.csv', usecols=['NR_VOTAVEL'], sep=';', low_memory=False, encoding='latin-1').fillna(value=0).values

arff = '@relation laranjas'
arff += '\n\n'
arff += '@attribute idade { <20, 20-40, 40+ }\n'
arff += '@attribute genero { MASCULINO, FEMININO, N/A }\n'
arff += '@attribute grau_instrucao { ENSINO INCOMPLETO, ENSINO MEDIO COMPLETO, SUPERIOR COMPLETO }\n'
arff += '@attribute estado_civil { SOLTEIRO(A), DIVORCIADO(A), CASADO(A), VIÚVO(A) }\n'
arff += '@attribute cor {PRETA, PARDA, BRANCA }\n'
arff += '@attribute cidade_nascimento { RECIFE, INTERIOR }'
arff += '@attribute investigado { SIM, NAO }'
arff += '\n\n'
arff += '@data\n'

for value in values:

	# Get city in value[1]
	city = value[1]
	if city != 'RECIFE':
		arff += 'INTERIOR'
	else:
		arff += city
	arff += ','

	# Get age by birth date in value[2]
	birth = datetime.datetime.strptime(value[2], '%d/%m/%Y')
	today = datetime.date.today()
	age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
	if age <= 20:
		arff += '<20'
	elif age > 20 and age < 40:
		arff += '20-40'
	else:
		arff += '40+'
	arff += ','

	# Get gender in value[3]
	gender = value[3]
	if gender != "FEMININO" and gender != "MASCULINO":
		arff += 'N/A'
	else:
		arff += gender
	arff += ','

	# Get school level in value [4]
	school =  value[4]
	if school == "SUPERIOR COMPLETO":
		arff += 'SUPERIOR COMPLETO'
	elif school == "ENSINO MÉDIO COMPLETO" or school == "SUPERIOR INCOMPLETO":
		arff += 'ENSINO MEDIO COMPLETO'
	else:
		arff += 'ENSINO INCOMPLETO'
	arff += ','

	# Get civil status in value[5]
	status = value[5]
	if status == 'VIÚVO(A)':
		arff += "VIUVO(A)"
	else: 
		arff += status 
	arff += ','

	# Get color in value[6]
	arff += value[6]
	arff += ','

	# Check if outlier
	if value[0] in outliers:
		arff += 'SIM'
	else:
		arff += 'NAO'

	arff += '\n'

print(arff)

file = open('weka.arff', 'w+')
file.write(arff)
file.close()
