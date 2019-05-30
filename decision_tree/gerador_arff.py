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
arff += '@attribute cidade_nascimento {RECIFE,INTERIOR}\n'
arff += '@attribute idade {<30,30-40,40-50,50+}\n'
arff += '@attribute genero {MASCULINO,FEMININO}\n'
arff += '@attribute grau_instrucao {INCOMPLETO,MEDIO,SUPERIOR}\n'
arff += '@attribute estado_civil {SOLTEIRO(A),DIVORCIADO(A),CASADO(A),VIUVO(A),SEPARADO(A)}\n'
arff += '@attribute cor {PRETA,PARDA,BRANCA,INDIGENA,AMARELA}\n'
arff += '@attribute investigado {SIM,NAO}'
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
	if age <= 30:
		arff += '<30'
	elif age > 30 and age <= 40:
		arff += '30-40'
	elif age > 40 and age <= 50:
		arff += '40-50'
	else:
		arff += '50+'
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
		arff += 'SUPERIOR'
	elif school == "ENSINO MÉDIO COMPLETO" or school == "SUPERIOR INCOMPLETO":
		arff += 'MEDIO'
	else:
		arff += 'INCOMPLETO'
	arff += ','

	# Get civil status in value[5]
	status = value[5]
	if status == 'VIÚVO(A)':
		arff += "VIUVO(A)"
	elif status == 'SEPARADO(A) JUDICIALMENTE':
		arff += 'SEPARADO(A)'
	else: 
		arff += status 
	arff += ','

	# Get color in value[6]
	cor = value[6]
	if cor == 'INDÍGENA':
		arff += 'INDIGENA'
	else:
		arff += value[6]

	arff += ','

	# Check if outlier
	if value[0] in outliers:
		arff += 'SIM'
	else:
		arff += 'NAO'
	arff += '\n'

print(arff)

file = open('arvore_candidatos_laranja.arff', 'w+')
file.write(arff)
file.close()
