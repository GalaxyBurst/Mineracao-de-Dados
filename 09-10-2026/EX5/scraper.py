import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

# 1. Acessa a página pelo servidor local
resposta = requests.get(URL, timeout=10)
resposta.raise_for_status()
resposta.encoding = "utf-8"

# 2. Faz a análise do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# 3. Primeiro localiza cada seção do cardápio
secoes = soup.find_all("section", class_="secao")

print("CARDÁPIO")
print("=" * 55)

for secao in secoes:
    categoria = secao.find("h2", class_="categoria").get_text(strip=True)

    # 4. Depois percorre apenas os itens pertencentes a esta seção
    itens = secao.find_all("div", class_="item")

    print(f"\n{categoria.upper()} ({len(itens)} itens)")
    print("-" * 55)

    for item in itens:
        nome = item.find("h3", class_="nome").get_text(strip=True)
        descricao = item.find("p", class_="descricao").get_text(strip=True)
        preco = item.find("p", class_="preco").get_text(strip=True)

        print(f"  • {nome} — {preco}")
        print(f"      {descricao}")

print("\n" + "=" * 55)
