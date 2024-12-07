import pandas as pd                         # Para la manipulación y análisis de datos
import numpy as np                          # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt             # Para generar gráficas a partir de los datos
import seaborn as sns

def exe(filename):
    Datos = pd.read_csv(filename)
    corr_matrix = Datos.corr() # Genera matriz de correlación
    get_heatmap(corr_matrix)
    return corr_matrix


def get_heatmap(corr_matrix):
    plt.figure(figsize=(14,7))
    inf_matrix = np.triu(corr_matrix)
    sns.heatmap(corr_matrix, cmap = "RdBu_r", annot = True, mask = inf_matrix) # Genera mapa de calor
    plt.savefig('static/heatmap.png', bbox_inches='tight')
    return 0