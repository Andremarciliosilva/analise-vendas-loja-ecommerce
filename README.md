# 📊 Análise de Vendas Para Loja de E-commerce

## 🧰 Stack Tecnológica

- **Linguagem:** Python
- **Bibliotecas:** Pandas, NumPy, Matplotlib
- **Análise:** Jupyter Notebook
- **Versionamento:** Git & GitHub
- **Gerenciamento de dependências e ambientes:** Poetry


## 📌 Visão Geral
Este projeto tem como objetivo transformar dados brutos de vendas de um e-commerce em **insights acionáveis para o negócio**, utilizando técnicas de análise de dados e fundamentos de Engenharia de Dados.

A solução foi desenvolvida para apoiar decisões estratégicas relacionadas a **estoque, marketing, sazonalidade e expansão regional**, substituindo decisões baseadas em intuição por uma abordagem **feita através dos dados**.

---

## 🎯 Contexto de Negócio
A empresa analisada é um e-commerce em fase de crescimento, com um volume cada vez maior de transações diárias. Apesar da grande quantidade de dados disponíveis, a ausência de análises estruturadas gera diversos desafios:

- Falta de visibilidade sobre produtos mais e menos vendidos  
- Gestão de estoque ineficiente  
- Campanhas de marketing genéricas e com baixo ROI  
- Dificuldade em identificar padrões sazonais  
- Expansão regional sem embasamento analítico  

O principal problema é a **ausência de informações claras e confiáveis** para apoiar a tomada de decisão.

---

## 🧠 Objetivos do Projeto
O projeto busca responder a quatro perguntas-chave do negócio:

- **O que vender?**  
  Identificar os produtos com melhor desempenho para otimizar o portfólio e o estoque.

- **Onde focar?**  
  Entender quais categorias de produtos geram maior receita.

- **Quando agir?**  
  Analisar a evolução das vendas ao longo do tempo para identificar tendências e sazonalidades.

- **Para onde expandir?**  
  Mapear a distribuição geográfica das vendas para identificar os mercados mais promissores.

---

## 🛠️ Solução Proposta
A solução consiste na:

1. Consolidação dos dados históricos de vendas  
2. Limpeza e tratamento dos dados  
3. Análise exploratória e geração de métricas de negócio  
4. Criação de visualizações para suporte à decisão  

O foco está em aplicar boas práticas de análise de dados com uma visão clara de negócio.

## 📘 Documentação Complementar

Além da documentação técnica, este projeto conta com um material complementar que descreve o planejamento, organização das atividades e metodologia de desenvolvimento:

➡️ [`lista-de-tarefas.md`](lista-de-tarefas.md)

---

## 📈 Resultados Esperados e Benefícios de Negócio

**Otimização de Estoque**  
Redução de custos com armazenamento e menor risco de ruptura de produtos.

**Marketing Direcionado**  
Campanhas segmentadas por categoria e região, aumentando o ROI.

**Planejamento Estratégico**  
Melhor previsibilidade de demanda com base em tendências históricas.

**Cultura Data-Driven**  
Decisões baseadas em dados concretos em vez de intuição.

---

## 🏗️ Estrutura do Projeto

```text
📁 analise-vendas-loja-ecommerce
│
├── 📁 dados                    # Camadas do pipeline
│   ├── 🥉 bronze               # Dados brutos
│   ├── 🥈 silver               # Dados tratados
│   └── 🥇 gold                 # Dados prontos para análise
│
├── 📁 notebooks/               # Exploração e ETL
│   ├── 📊 analise_vendas.ipynb
│   └── ⚙️ etl.ipynb
│
├── 📁 output/                  # Arquivos finais
│   ├── 🗂️ dados_bronze.csv
│   ├── 🗂️ dados_silver.csv
│   └── 🗂️ dados_gold.csv
│
📁 requisitos-de-negocio/       # Documentação
│   └── 📄 requisitos-de-negocio.pdf
│
├── LICENCE
│
├── poetry.lock
│
├── pyproject.toml
│
└── 📄 README.md
```

## 🏛️ Arquitetura do Pipeline de Dados

A arquitetura do projeto segue o modelo de camadas **Bronze / Silver / Gold**

```text
           🧪 Geração de Dados (Faker)
                     │
                     ▼
            📥 Ingestão de Dados
                     │
                     ▼
              🥉 Bronze Layer
           (dados brutos em CSV)
                     │
                     ▼
        🔄 Limpeza e Transformações
      - remoção de nulos  
      - padronização de datas  
      - conversão de tipos  
                     │
                     ▼
              🥈 Silver Layer
        (dados tratados e validados)
                     │
                     ▼
         📊 Agregações Analíticas
      - faturamento por categoria  
      - vendas por cidade  
      - evolução mensal  
                     │
                     ▼
              🥇 Gold Layer
      (dados prontos para análise)
                     │
                     ▼
        📈 Visualizações e Insights
      - gráficos em Matplotlib  
      - análises exploratórias  
```

## 🔹 Descrição das Camadas

### 🥉 Bronze — Dados Brutos
- Dados gerados artificialmente com Faker  
- Nenhuma transformação aplicada  
- Objetivo: preservar os dados originais  

### 🥈 Silver — Dados Tratados
- Remoção de valores nulos  
- Padronização de datas  
- Conversão de tipos  
- Validação de consistência  

### 🥇 Gold — Dados Analíticos
- Agregações por categoria, cidade e mês  
- Métricas prontas para consumo  
- Base para visualizações e tomada de decisão  

---

## 🧠 Aprendizados

- Como organizar e estruturar um projeto
- Conceito de camadas bronze, silver e gold
- Pensamento crítico, sempre procurando identificar coisas que possivelmente poderiam dar errado
- Utilização do Poetry, recurso que permite gerenciar as dependência e trabalhar em um ambiente isolado de maneira a não gerar conflito com outros projetos
- Criação de biblioteca e como utilzar os métodos criados nela
- Tratamento de dados com Pandas
- Resolução de problemas de negócio, transformando dados brutos em insights

👤 **Autor**  
André Silva 