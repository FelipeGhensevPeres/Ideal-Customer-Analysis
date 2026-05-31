# 📊 Ideal Customer Analysis

Projeto de análise de dados para identificar o perfil do cliente ideal de uma empresa de varejo com base no histórico de compras e no score de clientes.

O objetivo foi descobrir quais características estão mais presentes entre os clientes de maior valor, para que a empresa direcione campanhas, produtos e estratégias de marketing para o público com maior potencial de consumo.

---

# 🎯 Problema de Negócio

A empresa possui milhares de clientes com perfis diferentes e precisava responder algumas perguntas estratégicas

* Qual é o perfil dos melhores clientes?
* Quais características aparecem com maior frequência entre clientes de alto valor?
* Como direcionar campanhas e ações de marketing de forma mais eficiente?

Cada cliente recebeu uma nota de 1 a 100 baseada em seu comportamento de consumo.

---

# 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* Git
* GitHub

---

# 📂 Estrutura do Projeto

```text
Ideal-Customer-Analysis/
│
├── data/
│   └── clientes.csv
│
├── functions/
│   ├── __init__.py
│   ├── limpeza.py
│   ├── analise.py
│   └── vizualizacao.py
│
├── notebooks/
│   ├── main.ipynb
│   └── Perfil_Ideal_Cliente.ipynb
│
├── .gitignore
└── README.md
```

## Responsabilidade dos módulos

### limpeza.py

* Tratamento de dados
* Correção de inconsistências categóricas
* Conversão de tipos
* Remoção de valores nulos

### analise.py

* Funções de análise exploratória
* Segmentação dos clientes
* Criação de métricas e agrupamentos

### vizualizacao.py

* Funções reutilizáveis para geração de gráficos

---

# 🔄 Refatoração 

Durante a evolução do projeto fiz melhorias de organização e reutilização de código

* Reorganização da estrutura de diretórios
* Módulos reutilizáveis
* Separação de responsabilidades por arquivo
* Padronização dos dados categóricos
* Criação de funções para limpeza de dados
* Criação de funções reutilizáveis para gráficos
* Criação de funções reutilizáveis para análises exploratórias
* Configuração de `.gitignore`
* Controle de versão utilizando branches e merges com Git

---

# 📈 Etapas da Análise

## 🔹 Tratamento dos Dados

* Remoção de colunas desnecessárias
* Tratamento de valores nulos
* Conversão de tipos de dados
* Correção de problemas de texto
* Padronização de categorias

## 🔹 Análise Exploratória

Foram realizadas análises relacionadas a

* Profissão
* Faixa etária
* Faixa salarial
* Score dos clientes
* Segmentação dos clientes ideais

## 🔹 Definição do Perfil Ideal

Clientes com score igual ou superior a 70 foram considerados clientes ideais para a análise.

---

# 🔍 Principais Insights

## 🎭 Profissão

Profissões ligadas às áreas de arte e entretenimento tiveram maior frequência entre os clientes com melhores scores.

## 👤 Faixa Etária

Clientes acima de 65 anos concentraram a maior parcela dos melhores resultados.

## 💰 Renda

A maioria dos clientes ideais possui renda anual superior a **R$ 120.000**.

---

# 👤 Perfil do Cliente Ideal

O perfil identificado apresenta as seguintes características:

* Idade acima de 65 anos
* Alta renda anual
* Profissão ligada à área artística ou entretenimento
* Alto score de consumo e fidelização

---

# 💡 Estratégias Propostas

Com base nos resultados encontrados, a empresa pode:

* Direcionar campanhas para públicos de maior valor
* Criar ofertas premium para clientes de alta renda
* Personalizar a comunicação para públicos específicos
* Investir em ações voltadas para os segmentos artístico e de entretenimento
* Priorizar clientes com maior potencial de retenção e fidelização

---


### LinkedIn

https://www.linkedin.com/in/felipe-ghensev-peres-7a7427343/

