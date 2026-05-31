import matplotlib.pyplot as plt



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



