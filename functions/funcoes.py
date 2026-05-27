def corrigir_coluna(df,
                    coluna,
                    palavra_anomalica:str,
                    correcao:str):
    
    df[coluna] = df[coluna].replace({palavra_anomalica : correcao})
    
    return df