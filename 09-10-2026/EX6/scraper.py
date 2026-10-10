import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:8000/index.html"

# 1. Acessa a página pelo servidor local
resposta = requests.get(URL, timeout=10)
resposta.raise_for_status()
resposta.encoding = "utf-8"

# 2. Faz a análise do HTML
soup = BeautifulSoup(resposta.text, "html.parser")

# 3. Localiza todos os eventos
eventos = soup.find_all("div", class_="evento")
print(f"AGENDA DE EVENTOS ({len(eventos)})")

com_varios_palestrantes = []

for numero, evento in enumerate(eventos, start=1):
    nome = evento.find("h2", class_="nome").get_text(strip=True)
    data = evento.find("span", class_="data").get_text(strip=True)
    horario = evento.find("span", class_="horario").get_text(strip=True)
    local = evento.find("span", class_="local").get_text(strip=True)

    # 4. Cada palestrante é um elemento separado: find_all devolve todos
    palestrantes = [p.get_text(strip=True)
                    for p in evento.find_all("span", class_="palestrante")]

    # 5. Texto e href do link de inscrição
    link = evento.find("a", class_="inscricao")
    texto_link = link.get_text(strip=True)
    href_link = link["href"]

    print("=" * 60)
    print(f"Evento {numero}: {nome}")
    print(f"  Data:    {data}")
    print(f"  Horário: {horario}")
    print(f"  Local:   {local}")
    print(f"  Palestrante(s): {', '.join(palestrantes)}")
    if len(palestrantes) > 1:
        print(f"  >> Este evento possui MAIS DE UM palestrante ({len(palestrantes)})")
        com_varios_palestrantes.append(nome)
    print(f"  Link (texto): {texto_link}")
    print(f"  Link (href):  {href_link}")

print("=" * 60)

# 6. Resumo dos eventos com mais de um palestrante
print()
print("EVENTOS COM MAIS DE UM PALESTRANTE:")
for nome in com_varios_palestrantes:
    print(f"  - {nome}")
