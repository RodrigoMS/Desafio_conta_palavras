from django.shortcuts import render

from collections import Counter

import re

def home(request):
    return render(request, 'index.html')

# Remove acentos e pontuações
def removerSimbolos(texto, cRemover):

	for x in cRemover:
		texto = texto.replace(x, '')

	return texto

def resultado(request):
	texto = request.GET['texto']

	textoSP = removerSimbolos(texto, ',.;:\'\"*-+_<>/?!@#$%&*=()\{\}[]')

	#Converte o texto em caixa baixa
	#Criando um array com as paravras do texto. 
	palavras = textoSP.lower().split()

	#Conta e retorna as ocorrências de cada palavra.
	ocorrencias = Counter(palavras)

	resultado = []
	#Adiciona no array "resultado" a palavra e quantidade de ocorrências.
	for palavra, quantidade in ocorrencias.items():
		resultado.append([quantidade, palavra])

	#ordena de forma descendente.
	ordenar = sorted(resultado, reverse=True)

	quantidade = len(ordenar)

	#Após ordenar pelo número de ocorrências, coloca em ordem alfabética.
	for i in range(0,len(ordenar)-1):
		for j in range(i+1,len(ordenar)):
			if ordenar[i][0] == ordenar[j][0] and ordenar[i][1] > ordenar[j][1]:
				x = ordenar[i]
				ordenar[i] = ordenar[j]
				ordenar[j] = x

	return render(request, 'resultado.html', {'texto': texto, 'quantPalavras': quantidade, 'ordenar': ordenar})
