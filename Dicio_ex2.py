
import re
from collections import defaultdict

def contar_palavras(arquivo):
    contador_palavras = defaultdict(int)
    
    with open(arquivo, 'r', encoding='latin-1') as file:
        texto = file.read()
        texto_limpo = re.sub(r'[^\w\s]', '', texto).lower() 
        palavras = texto_limpo.split()
        for palavra in palavras:
            contador_palavras[palavra] += 1      
    
    return contador_palavras

def ordenar_por_frequencia(contador_palavras):
    return dict(sorted(contador_palavras.items(), key=lambda item: item[1], reverse=True))

arquivo = 'c:/Users/Administrador/Documents/python/dicionario/estomago.txt'

contador_palavras = contar_palavras(arquivo)
contador_palavras_ordenado = ordenar_por_frequencia(contador_palavras)

for palavra, frequencia in contador_palavras_ordenado.items():
    print(f'{palavra}: {frequencia}')






