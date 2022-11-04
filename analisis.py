#En primer lugar vamos a importar las librerías necesarias para el análisis de datos
import pandas as pd
import numpy as np

#Cargamos el archivo csv y lo mostramos
data=pd.read_csv('vehicles.csv')
data.head() 

#Vamos a ver el tamaño del dataframe
data.shape