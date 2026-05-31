import pandas as pd
import matplotlib.pyplot as plt

# FUNÇÃO - CORRIGIR NOME DE LINHAS 
def corrigir_coluna(df,
                    coluna,
                    palavra_anomalica:str,
                    correcao:str):
    
    df[coluna] = df[coluna].replace({palavra_anomalica : correcao})
    
    return df



# FUNÇÃO - REMOVER COLUNA
def remover_coluna(df,
                   coluna):
    
    return df.drop(columns=coluna)



# FUNCÃO - REMOVER VALORES NULOS
def remover_nulos(df):
    
    return df.dropna()



# FUNÇÃO - CONVERTER COLUNA NUMÉRICA
def converter_para_numerico(df,coluna):
    
    df[coluna] = pd.to_numeric(df[coluna],
                               errors='coerce')


    return df



# FUÇÃO - REMOVER NULOS DE COLUNA ESPECÍFICA
def remover_nulos_coluna(df,coluna):
    
    return df.dropna(subset=[coluna])



# FUNÇÃO - CRIAR GRÁFICOS
def criar_grafico_barras(dados,
                         titulo,
                         xlabel,
                         ylabel,
                         rotacao=0):
    
    plt.figure(figsize=(10,5))
    
    dados.plot(kind='bar')
    

    plt.title = titulo
    plt.xlabel = xlabel
    plt.ylabel = ylabel
    plt.xticks(rotation=rotacao)
    
    plt.grid(axis='y',
             linestyle='--',
             alpha=0.3)
    
    
    
    
    plt.tight_layout()
    
    plt.show()



# FUNÇÃO FILTRAR CLIENTES IDEAIS
def filtrar_clientes_ideais(df,nota_minima):
    
    return df[df['Nota (1-100)'] >= nota_minima]



# FUNÇÃO DISTRIBUIÇÃO DE FAIXA ETÁRIA
def criar_faixa_etaria(df):

    return pd.cut(df['Idade'],
                     bins=[18,25,35,45,55,65,100]).value_counts().sort_index()


# FUNÇÃO DISTRIBUIÇÃO SALARIAL
def criar_faixa_salarial(df):

    return pd.cut(df['Salario Anual (R$)'],
                        bins=[0,30000,60000,90000,120000,
                        df['Salario Anual (R$)'].max()]).value_counts().sort_index()
    
    
    
# FUNÇÃO PARA OBTER AS PROFISSÕES DOS CLIENTES IDEAIS
def obter_profissoes_ci(df):
    
    return df['Profissao'].value_counts()