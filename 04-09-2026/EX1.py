media = 100
desvio = 5
valor = 115

distancia = valor - media
print(f"Distancia: {distancia}")

quantidadeDesvios = distancia / desvio
print(f"Quantidade de Desvios: {quantidadeDesvios}")

z = (valor - media) / desvio
print(f"Z-Score: {z}")

print(f"O valor {valor} está {z} desvios-padrão acima da média.")
print(f"Como estamos usando |Z| > 3 como regra prática de alerta, esse valor está exatamente no limite dessa referência.")
print(f"É um candidato a outlier, não uma certeza.")