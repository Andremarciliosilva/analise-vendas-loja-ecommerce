# Imports necessários

import random
import pandas as pd
import csv
from faker import Faker
fake = Faker("pt_BR")

# Categoria: Smartphones e Acessórios
# Produtos e preços: Smartphone: R$ 2.000,00 / Fone de Ouvido: R$ 200,00 / Carregador: R$ 100,00 / Smartwatch: R$ 1.000,00
smartphone_e_acessorios = {'smartphone': 2000, 'fone de ouvido': 200, 'carregador': 100, 'smartwatch': 1000, 'capinha': ''}

# Categoria: Informática e Periféricos
# Produtos e preços: Notebook: R$ 4.000,00 / Monitor: 1.500,00 / Mouse: R$ 100,00
informatica_e_perifericos = {'notebook': 4000, 'monitor': 1500, 'mouse': 100, 'teclado': ''}

# Categoria: Eletrodomésticos
# Produtos e preços: Ar-Condicionado: R$ 2.500,00 / Geladeira: R$ 5.000,00 / Fogão: R$ 1.500,00
eletrodomesticos = {'ar-condicionado': 2500, 'geladeira': 5000, 'fogao': 1500, 'micro-ondas': ''}

# Categoria: TV, Áudio e Vídeo
# Produtos e preços: Smart TV: R$ 4.000,00 / Soundbar: R$ 1.000,00 / Chromecast: R$ 200,00
tv_audio_video = {'smart tv': 4000, 'soundbar': 1000, 'chromecast': 200 , 'home theater': ''}

# Função para gerar dados aleatórios

def gerar_dados(num_vendas, caminho_saida="output/dados_bronze.csv"):
    dados_gerados = []

    # Lista de todos os produtos com suas categorias
    produtos = []

    for produto, preco in smartphone_e_acessorios.items():
        produtos.append((produto, preco, "Smartphones e Acessórios"))

    for produto, preco in informatica_e_perifericos.items():
        produtos.append((produto, preco, "Informática e Periféricos"))

    for produto, preco in eletrodomesticos.items():
        produtos.append((produto, preco, "Eletrodomésticos"))

    for produto, preco in tv_audio_video.items():
        produtos.append((produto, preco, "TV, Áudio e Vídeo"))

    # Geração do dicionário com dados aleatórios
    for _ in range(num_vendas):
        produto, preco, categoria = random.choice(produtos)

        cliente = random.randint(1, 10000)
        quantidade = random.randint(1, 5)
        data = fake.date_between(start_date="-2y", end_date="today")

        dados_gerados.append({
            'cliente': cliente,
            'produto': produto,
            'preco': preco,
            'categoria': categoria,
            'quantidade': quantidade,
            'data': data
        })

    # Cria DataFrame 
    df = pd.DataFrame(dados_gerados)

    # Salva em csv
    df.to_csv(
        caminho_saida,
        index=False,
        quoting=csv.QUOTE_NONNUMERIC
    )

    # Retorna o DataFrame gerado
    return df
    