def filtrar_dicionario():
    dicionario = {}
    
    print("Digite os pares chave-valor para o dicionário (chave:valor), digite 'fim' para encerrar:")
    while True:
        dados= input()
        if dados == "fim":
            break
        chave, valor = dados.split(":")
        dicionario[chave.strip()] = int(valor.strip())

    print("Digite as chaves que deseja filtrar, separadas por vírgula:")
    chaves_filtradas = input().split(",")
    chaves_filtradas = [chave.strip() for chave in chaves_filtradas]

    novo_dicionario = {}
    for chave in chaves_filtradas:
        if chave in dicionario:
            novo_dicionario[chave] = dicionario[chave]

    return novo_dicionario

resultado = filtrar_dicionario()
print("Dicionário filtrado:", resultado)

