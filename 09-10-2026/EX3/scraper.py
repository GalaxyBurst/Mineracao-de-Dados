import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"
CATEGORIA_ESCOLHIDA = "Tecnologia"

# 1. Acessa a página pelo servidor local
resposta = requests.get(URL, timeout=10)
resposta.raise_for_status()
resposta.encoding = "utf-8"

# 2. Faz a análise do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# 3. Localiza todas as notícias e extrai os campos
noticias = []
for item in soup.find_all("article", class_="noticia"):
    noticias.append({
        "categoria": item.find("p", class_="categoria").get_text(strip=True),
        "titulo": item.find("h2", class_="titulo").get_text(strip=True),
        "data": item.find("p", class_="data").get_text(strip=True),
        "resumo": item.find("p", class_="resumo").get_text(strip=True),
        "autor": item.find("p", class_="autor").get_text(strip=True),
    })

# 4. Exibe cada notícia em um bloco organizado
print(f"NOTÍCIAS ENCONTRADAS ({len(noticias)})")
for i, n in enumerate(noticias, start=1):
    print("=" * 60)
    print(f"Notícia {i}")
    print(f"  Categoria: {n['categoria']}")
    print(f"  Título:    {n['titulo']}")
    print(f"  Data:      {n['data']}")
    print(f"  Resumo:    {n['resumo']}")
    print(f"  Autor:     {n['autor']}")
print("=" * 60)

# 5. Exibe apenas os títulos da categoria escolhida
titulos = [n["titulo"] for n in noticias if n["categoria"] == CATEGORIA_ESCOLHIDA]

print()
print(f"TÍTULOS DA CATEGORIA '{CATEGORIA_ESCOLHIDA}' ({len(titulos)})")
for titulo in titulos:
    print(f"  - {titulo}")
