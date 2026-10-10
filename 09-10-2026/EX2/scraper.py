import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

# 1. Acessa a página pelo servidor local
resposta = requests.get(URL, timeout=10)
resposta.raise_for_status()
resposta.encoding = "utf-8"

# 2. Faz a análise do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# 3. Localiza todos os produtos e extrai os dados
produtos = []
for item in soup.find_all("div", class_="produto"):
    produtos.append({
        "nome": item.find("h2", class_="nome").get_text(strip=True),
        "fabricante": item.find("span", class_="fabricante").get_text(strip=True),
        "categoria": item.find("span", class_="categoria").get_text(strip=True),
        "preco": item.find("span", class_="preco").get_text(strip=True),
        "estoque": item.find("span", class_="estoque").get_text(strip=True),
    })


def exibir(produto, numero):
    print(f"Produto {numero}: {produto['nome']}")
    print(f"  Fabricante: {produto['fabricante']}")
    print(f"  Categoria:  {produto['categoria']}")
    print(f"  Preço:      {produto['preco']}")
    print(f"  Estoque:    {produto['estoque']}")
    print("-" * 45)


# 4. Exibe todos os produtos
print(f"TODOS OS PRODUTOS ({len(produtos)})")
print("=" * 45)
for i, produto in enumerate(produtos, start=1):
    exibir(produto, i)

# 5. Exibe apenas os produtos disponíveis
disponiveis = [p for p in produtos if p["estoque"] == "Disponível"]

print()
print(f"PRODUTOS DISPONÍVEIS ({len(disponiveis)})")
print("=" * 45)
for i, produto in enumerate(disponiveis, start=1):
    exibir(produto, i)
