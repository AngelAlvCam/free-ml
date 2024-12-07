import pandas as pd                 # Para la manipulación y análisis de los datos
from apyori import apriori

def exe(filename, support, confidence, lift):
    DatosTransacciones = pd.read_csv(filename)
    TransaccionesLista = DatosTransacciones.stack().groupby(level=0).apply(list).tolist()
    reglas = apriori(TransaccionesLista,min_support=support,min_confidence=confidence,min_lift=lift)
    resultados = list(reglas)
    return resultados

