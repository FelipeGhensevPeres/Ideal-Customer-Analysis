import pandas as pd

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