# Remoção de valores nulos
# Organização das datas
# Remoção de duplicatas se houver
# Padronização das datas conforme a norma nacional NBR 5892:2019 "dd/mm/yyyy”
# Calcular o valor total da venda “Preço x Quantidade"



import pandas as pd

def transformar_dados(caminho_entrada="output/dados_vendas_bronze.csv", caminho_saida="output/dados_vendas_silver.csv"):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv(caminho_entrada, na_values=[""])
    print(f"Registros originais: {len(df)}")

    # Remover registros com valores nulos 
    df_clean = df.dropna(subset=['cliente', 'produto', 'preco', 'categoria', 'quantidade', 'data'])
    valores_removidos = len(df) - len(df_clean)
    print(f"A quantidade atual de registros é {len(df_clean)}, foram removidos {valores_removidos} por conterem valores nulos.")

    # Remover duplicatas, se houver
    df_clean = df_clean.drop_duplicates()
    print(f"A quantidade atual de registros é {len(df_clean)} após a remoção de duplicatas.")

    # Padronizar a coluna de datas para o formato "dd/mm/yyyy"
    df_clean['data'] = pd.to_datetime(df_clean['data'], errors='coerce').dt.strftime('%d/%m/%Y')
    print("As datas foram padronizadas para o formato dd/mm/yyyy.")

    # Ordenar datas em ordem decrescente
    df_clean = df_clean.sort_values(by='data', ascending=False)
    print("As datas foram ordenadas em ordem decrescente.")

    # Calcular o valor total da venda
    df_clean['valor_total'] = df_clean['preco'] * df_clean['quantidade']
    print("A coluna 'valor_total' foi adicionada ao DataFrame.")

    # Salvar os dados transformados em um novo arquivo CSV
    df_clean.to_csv(caminho_saida, index=False)

    return df_clean