import numpy as np
from sklearn.ensemble import IsolationForest

latencias = np.array([
    [25],
    [30],
    [45],
    [60],
    [35],
    [50],
    [65],
    [28],
    [40],
    [55],
    [220],
    [310]
])

modelo = IsolationForest(n_estimators=5,
                          contamination=2 / len(latencias),
                          random_state=42
)

modelo.fit(latencias)

classificacoes = modelo.predict(latencias)

print("Latências medidas (ms):   ", latencias[:, 0])
print("Classificações (1/-1):    ", classificacoes)

anomalias = latencias[classificacoes == -1]
print("\nValor(es) sinalizado(s) como anomalia pelo modelo:", anomalias[:, 0])

# ---------------------------------------------------------------
# Explicação dos candidatos identificados (220 ms e 310 ms)
# ---------------------------------------------------------------
# Esses dois valores divergem do padrão da rede (20-70 ms),
# por isso o modelo os isola com mais facilidade.

# ---------------------------------------------------------------
# Pergunta para discussão: uma latência alta sempre representa uma falha?
# ---------------------------------------------------------------
# Não necessariamente. Uma latência alta isolada pode ser apenas uma
# variação normal da rede, sem indicar um problema real ou persistente.
