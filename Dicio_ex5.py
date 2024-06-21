def coletar_dados():
    votos = []
    for i in range(1, 4):
        candidato = input(f"Digite o nome do candidato {i}: ")
        qtd_votos = int(input(f"Digite a quantidade de votos para {candidato}: "))
        votos.append({'candidato': candidato, 'votos': qtd_votos})
    return votos

def resultado_votacao(votos):
    resultado = {}
    total_votos = 0

    for voto in votos:
        candidato = voto['candidato']
        qtd_votos = voto['votos']
        total_votos += qtd_votos
        if candidato in resultado:
            resultado[candidato] += qtd_votos
        else:
            resultado[candidato] = qtd_votos

    for candidato in resultado:
        total_candidato = resultado[candidato]
        percentual = (total_candidato / total_votos) * 100
        resultado[candidato] = (total_candidato, percentual)

    return resultado

votos = coletar_dados()

resultado = resultado_votacao(votos)

for candidato, (total, percentual) in resultado.items():
    print(f"Candidato: {candidato} - Total de votos: {total} - Percentual: {percentual:.2f}%")


