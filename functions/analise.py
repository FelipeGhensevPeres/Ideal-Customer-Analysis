import pandas as pd



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