import re
import requests
from bs4 import BeautifulSoup
import csv

# Alunos: Victor e Thiago Lima
url = "https://pokemondb.net/pokedex/all"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'id': 'pokedex'})

fire_pokemon_list = []

dex_number_pattern = re.compile(r'^\d+$')  
stat_pattern = re.compile(r'^\d+$') 
type_pattern = re.compile(r'^[A-Za-z,\s]+$')  

pokemon_count = 0

rows = table.find_all('tr')[1:]  

for row in rows:
    if pokemon_count >= 10:  
        break

    cells = row.find_all('td')

    try:
        dex_number = cells[0].text.strip().zfill(4) 
        name = cells[1].text.strip()  
        types = ', '.join([t.text.strip() for t in cells[2].find_all('a')])  
        hp = cells[4].text.strip()  
        attack = cells[5].text.strip()  
        defense = cells[6].text.strip()  

        if not dex_number_pattern.match(dex_number):
            raise ValueError(f"Dex Number inválido: {dex_number}")
        if not type_pattern.match(types):
            raise ValueError(f"Tipos inválidos: {types}")
        if not all(stat_pattern.match(stat) for stat in [hp, attack, defense]):
            raise ValueError(f"Um ou mais stats inválidos para {name}")

        if "Fire" in types:
            fire_pokemon = {
                "Dex Number": dex_number,
                "Name": name,
                "HP": hp,
                "Attack": attack,
                "Defense": defense
            }
            fire_pokemon_list.append(fire_pokemon)
            pokemon_count += 1 

            print(f"{fire_pokemon}")

    except Exception as e:
        print(f"Erro ao processar linha: {e}")
        continue

with open('fire_pokemon_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Dex Number", "Name", "HP", "Attack", "Defense"])
    writer.writeheader()  
    writer.writerows(fire_pokemon_list)  

print("\nArquivo 'fire_pokemon_data.csv' gerado com sucesso!")
