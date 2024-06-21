def mesclar_dicionarios(dicionario1, dicionario2):
    novo_dicionario = dicionario1.copy() 
    
    for chave, valor in dicionario2.items():
        if chave in novo_dicionario:
            if valor > novo_dicionario[chave]:
                novo_dicionario[chave] = valor
        else:
            novo_dicionario[chave] = valor
    return novo_dicionario

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 3, 'c': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado) 
