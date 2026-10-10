import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

# 1. Acessa a página pelo servidor local
resposta = requests.get(URL, timeout=10)
resposta.raise_for_status()
resposta.encoding = "utf-8"

# 2. Faz a análise do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# 3. Localiza todos os cursos
cursos = soup.find_all("div", class_="curso")
print(f"Total de cursos encontrados: {len(cursos)}\n")

# 4. Extrai os dados de cada curso
for numero, curso in enumerate(cursos, start=1):
    nome = curso.find("h2", class_="nome").get_text(strip=True)
    area = curso.find("span", class_="area").get_text(strip=True)
    carga = curso.find("span", class_="carga").get_text(strip=True)

    print("=" * 45)
    print(f"Curso {numero}: {nome}")
    print(f"  Área: {area}")
    print(f"  Carga horária: {carga}")
    print("  Assuntos estudados:")

    # 5. Percorre a lista de assuntos do curso
    assuntos = curso.find("ul", class_="assuntos").find_all("li")
    for i, assunto in enumerate(assuntos, start=1):
        print(f"    {i}. {assunto.get_text(strip=True)}")

print("=" * 45)
