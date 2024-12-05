# extrai_dados_pokemon               Projeto de Scraping de Pokémon do Tipo Fogo
site onde vai extrair os dados:https://pokemondb.net/pokedex/all

Objetivo
O objetivo deste projeto é realizar scraping na página do site Pokémon DB para extrair informações sobre os Pokémon do tipo Fire (Fogo). As informações coletadas incluem:

Número na Pokédex
Nome do Pokémon
Tipos do Pokémon
Estatísticas de HP (Health Points), Ataque e Defesa
Esses dados são filtrados e validados, e os Pokémon do tipo Fire são salvos em um arquivo CSV denominado fire_pokemon_data.csv.

Tecnologias Utilizadas
Python: Linguagem de programação utilizada para o desenvolvimento do script.
requests: Biblioteca para realizar requisições HTTP e obter o conteúdo da página.
BeautifulSoup: Biblioteca para parsear o conteúdo HTML da página.
csv: Biblioteca para gerar e salvar os dados extraídos em um arquivo CSV.
re: Biblioteca para trabalhar com expressões regulares, utilizada para validar os dados extraídos.
Como Funciona
Requisição e Parsing:

O script faz uma requisição HTTP para a URL do site de Pokémon.
O conteúdo da página é processado utilizando o BeautifulSoup para facilitar a extração de informações.
Extração de Dados:

A partir da página, é localizada a tabela que contém as informações dos Pokémon.
Para cada Pokémon, são extraídos os seguintes dados:
Número na Pokédex
Nome
Tipos
HP, Ataque e Defesa
Validação de Dados:

Os dados extraídos são validados utilizando expressões regulares:
O número da Pokédex deve ser composto apenas por números.
Os tipos devem ser compostos apenas por letras e espaços.
As estatísticas (HP, Ataque e Defesa) devem ser números válidos.
Caso algum dado não passe na validação, um erro é gerado e a linha é ignorada.
Filtragem de Pokémon do Tipo "Fire":

Apenas os Pokémon que contêm "Fire" em seus tipos são selecionados.
Geração de Arquivo CSV:

Após a coleta e validação dos dados, os Pokémon do tipo Fire são salvos em um arquivo CSV com os seguintes campos:
Dex Number: Número na Pokédex
Name: Nome do Pokémon
HP: HP (Health Points)
Attack: Ataque
Defense: Defesa
Limitação de Pokémon:

O script coleta dados de no máximo 10 Pokémon do tipo Fire.
Como Executar o Projeto
Requisitos:

Certifique-se de que o Python 3 está instalado em sua máquina.
Instale as bibliotecas necessárias utilizando o pip:
bash
Copiar código
pip install requests beautifulsoup4
Executando o Script:

Basta rodar o script Python:
bash
Copiar código
python scraper.py
Resultado:

O script irá gerar um arquivo CSV chamado fire_pokemon_data.csv com os dados dos 10 primeiros Pokémon do tipo Fire encontrados na página.
Exemplo de Saída
O arquivo CSV gerado terá o seguinte formato:csv

resultado gerado no csv
Dex Number,Name,HP,Attack,Defense
0001,Bulbasaur,45,49,49
0002,Ivysaur,60,62,63
Contribuição
Este projeto foi desenvolvido por Victor e Thiago Lima como parte de uma atividade de aprendizado em scraping e manipulação de dados.
