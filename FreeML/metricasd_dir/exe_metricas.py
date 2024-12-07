import pandas as pd                 # Para la manipulación y análisis de los datos
from sklearn.preprocessing import StandardScaler, MinMaxScaler  
from scipy.spatial.distance import cdist    # Para el cálculo de distancias
from scipy.spatial import distance

def exe(filename, metrica, tipo_estandarizacion):
    Datos = pd.read_csv(filename)
    datos_std = std_data(Datos,tipo_estandarizacion)
    distancia = dist_met(datos_std, metrica)
    return distancia

def std_data(datos,tipo):
    if (tipo == '0'):
        estandarizar = StandardScaler()
        datos_std = estandarizar.fit_transform(datos)
    else:   # if tipo == normalizar
        minmax = MinMaxScaler()
        datos_std = minmax.fit_transform(datos)
    return datos_std

def dist_met(datos,metrica):
    if (metrica == '0'):  # Euclidea
        return cdist(datos, datos, metric='euclidean')
    elif (metrica == '1'):    # Chebyshev
        return cdist(datos, datos, metric='chebyshev')
    elif (metrica == '2'):    # Manhattan
        return cdist(datos, datos, metric='cityblock')