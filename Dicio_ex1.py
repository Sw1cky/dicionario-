def contagem_caracteres(s):
    contagem = {}
    for letra in s:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

frase = input("Digite uma frase: ")
resultado = contagem_caracteres(frase)
print(resultado)
