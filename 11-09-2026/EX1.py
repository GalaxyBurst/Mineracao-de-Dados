import numpy as np
from sklearn.ensemble import IsolationForest

vendas = np.array([
    [80],
    [85],
    [90],
    [88],
    [92],
    [87],
    [95],
    [89],
    [91],
    [400]
])

modelo = IsolationForest(n_estimators=5,
                          contamination=1 / len(vendas),
                          random_state=42
)

modelo.fit(vendas)

classificacoes = modelo.predict(vendas)

print("Valores de vendas:        ", vendas[:, 0])
print("Classificações (1/-1):    ", classificacoes)

anomalias = vendas[classificacoes == -1]
print("\nValor(es) sinalizado(s) como anomalia pelo modelo:", anomalias[:, 0])

# ---------------------------------------------------------------
# Por que uma venda muito alta (ex.: 400) pode não ser um erro?
# ---------------------------------------------------------------
# - Promoção: um desconto pode ter gerando um pico de vendas legítimo.
# - Encomenda: um cliente pode ter feito um pedido grande de uma só vez; incomum, mas plausivel.
#
# O modelo apenas SINALIZA o valor como outlier; cabe a uma pessoa investigar 
# o contexto real por trás.

# ---------------------------------------------------------------
# Pergunta para discussão: o valor 400 deve ser removido automaticamente?
# ---------------------------------------------------------------
# Não necessariamente. Removê-lo automaticamente pode descartar uma
# informação valiosa, alem de violar an convenções de IQR.
