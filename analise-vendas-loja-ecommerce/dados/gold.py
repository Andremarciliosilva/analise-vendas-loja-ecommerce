def carregar_dados(caminho_entrada, caminho_saida):
    import pandas as pd

    # Carregar os dados do arquivo CSV para um DataFrame do Pandas
    df_gold = pd.read_csv(caminho_entrada)

    # Salvar os dados transformados em um novo arquivo CSV
    df_gold.to_csv(caminho_saida, index=False)

    # Exibir as primeiras linhas do DataFrame para verificação
    print("Dados carregados com sucesso. Aqui estão as primeiras linhas:")

    return df_gold