import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

# 1. Acessa a página pelo servidor local
resposta = requests.get(URL, timeout=10)
resposta.raise_for_status()
resposta.encoding = "utf-8"

# 2. Faz a análise do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# 3. Localiza cada livro e extrai seus campos
livros = []
for item in soup.find_all("div", class_="livro"):
    # 4. Percorre os itens da lista de palavras-chave
    palavras = [li.get_text(strip=True)
                for li in item.find("ul", class_="palavras-chave").find_all("li")]

    livros.append({
        "titulo": item.find("h2", class_="titulo").get_text(strip=True),
        "autor": item.find("span", class_="autor").get_text(strip=True),
        "ano": item.find("span", class_="ano").get_text(strip=True),
        "genero": item.find("span", class_="genero").get_text(strip=True),
        "situacao": item.find("span", class_="situacao").get_text(strip=True),
        "palavras": palavras,
    })


def exibir(livro, numero):
    print(f"Livro {numero}: {livro['titulo']}")
    print(f"  Autor:     {livro['autor']}")
    print(f"  Ano:       {livro['ano']}")
    print(f"  Gênero:    {livro['genero']}")
    print(f"  Situação:  {livro['situacao']}")
    print(f"  Palavras-chave: {', '.join(livro['palavras'])}")
    print("-" * 50)


# 5. Exibe todos os livros
print(f"TODOS OS LIVROS ({len(livros)})")
print("=" * 50)
for i, livro in enumerate(livros, start=1):
    exibir(livro, i)

# 6. Exibe separadamente apenas os livros disponíveis
disponiveis = [l for l in livros if l["situacao"] == "Disponível"]

print()
print(f"LIVROS DISPONÍVEIS ({len(disponiveis)})")
print("=" * 50)
for i, livro in enumerate(disponiveis, start=1):
    exibir(livro, i)
