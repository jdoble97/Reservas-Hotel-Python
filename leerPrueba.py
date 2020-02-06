import json
from Reserva import Reserva
import os.path as path

with open('data.json') as json_file:
    data = json.load(json_file)
    objetos = []
    for x in data:
        atributos = []
        print(x)
        for k in x:
            print("Segundo for")
            atributos.append(x[k])
            print(k)
        objetos.append(Reserva(atributos[0],atributos[1],atributos[2],atributos[3],atributos[4]))
    for y in objetos:
        print(type(y))
 
if path.exists("data.json"):
    print("Hay un fichero con este nombre")
    print(path.realpath("data.json"))
else:
    print("No hay fichero con este nombre")