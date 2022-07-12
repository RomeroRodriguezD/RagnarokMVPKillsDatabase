import pandas as pd

csvmvps = pd.read_csv('Lista MVP.csv')
lista_mvps = []

for i in csvmvps.Amdarais:  #Creamos la lista utilizando la columna "Amdarais" del CSV.
    lista_mvps.append(i)

print(lista_mvps)