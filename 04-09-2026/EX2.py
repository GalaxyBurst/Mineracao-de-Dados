casos = [85, 100, 120]
media = 100
desvio = 10

for valor in casos:
    z = (valor - media) / desvio
    print(f"Valor: {valor}")
    print(f"Z-Score: {z}")

    if z > 0:
        posicao = "acima da média"
    elif z < 0:
        posicao = "abaixo da média"
    else:
        posicao = "exatamente na média"

    print(f"O valor {valor} está {posicao}.")

    if z > 0:
        print(f"O sinal positivo indica que o valor está acima da média.")
    elif z < 0:
        print(f"O sinal negativo indica que o valor está abaixo da média.")
    else:
        print(f"O sinal zero indica que o valor coincide com a média, sem desvio algum.")

    print("-" * 40)
