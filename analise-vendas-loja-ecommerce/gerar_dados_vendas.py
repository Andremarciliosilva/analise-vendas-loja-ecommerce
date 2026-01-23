# Imports necessários

import random
import csv
from faker import Faker
fake = Faker("pt_BR")

# Categoria: Smartphones e Acessórios
# Produtos e preços: Smartphone: R$ 2.000,00 / Fone de Ouvido: R$ 200,00 / Carregador: R$ 100,00 / Smartwatch: R$ 1.000,00
smartphone_e_acessorios = {'smartphone': 2000, 'fone de ouvido': 200, 'carregador': 100, 'smartwatch': 1000}

# Categoria: Informática e Periféricos
# Produtos e preços: Notebook: R$ 4.000,00 / Monitor: 1.500,00 / Mouse: R$ 100,00
informatica_e_perifericos = {'notebook': 4000, 'monitor': 1500, 'mouse': 100}

# Categoria: Eletrodomésticos
# Produtos e preços: Ar-Condicionado: R$ 2.500,00 / Geladeira: R$ 5.000,00 / Fogão: R$ 1.500,00
eletrodomesticos = {'ar-condicionado': 2500, 'geladeira': 5000, 'fogao': 1500}

# Categoria: TV, Áudio e Vídeo
# Produtos e preços: Smart TV: R$ 4.000,00 / Soundbar: R$ 1.000,00 / Chromecast: R$ 200,00
tv_audio_video = {'smart tv': 4000, 'soundbar': 1000, 'chromecast': 200}

# Lista vazia pra adicionar os dados que serão gerados aleatoreamente
dados_gerados = []

# Função para gerar dados aleatórios
while len(dados_gerados) < 5: 
    dados_aleatorios = random.choice(list(smartphone_e_acessorios.items()) 
                                     + list(informatica_e_perifericos.items()) 
                                     + list(eletrodomesticos.items()) 
                                     + list(tv_audio_video.items())) 
    
    cliente = random.randint(1,10000)
    data = fake.date_between(start_date="-2y", end_date="today")

    if dados_aleatorios in smartphone_e_acessorios.items():
        categoria = 'Smartphones e Acessórios'
    elif dados_aleatorios in informatica_e_perifericos.items():
        categoria = 'Informática e Periféricos'
    elif dados_aleatorios in eletrodomesticos.items():
        categoria = 'Eletrodomésticos'
    else:
        categoria = 'TV, Áudio e Vídeo'
        
    dict_dados_aleatorios = {'cliente': cliente, 
                             'produto': dados_aleatorios[0], 
                             'preco': dados_aleatorios[1], 
                             'categoria': categoria, 
                             'data': data}
    
    dados_gerados.append(dict_dados_aleatorios,)

# Exibir os dados gerados
print(dados_gerados)

