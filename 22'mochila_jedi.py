# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u 
# otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos 
# objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con 
# ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no 
# queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.

from random import randint

def usar_la_fuerza(mochila,objetos_sacados=0):
    if len(mochila) == 0:
        print()
        print("No se encontró el sable de luz.")
    
    objeto = mochila[randint(0, len(mochila)-1)]
    
    print('Objeto sacado:', objeto)
    
    if objeto == 'sable de luz':
        print()
        if objetos_sacados > 1:
            print(f"Se encontró el sable de luz después de sacar {objetos_sacados} objetos.")
        elif objetos_sacados == 1:
            print(f"Se encontró el sable de luz después de sacar 1 objeto.")
        else:
            print(f"Se encontró el sable de luz a la primera.")
            
        return objetos_sacados + 1
    else:
        mochila.remove(objeto)
        
    return usar_la_fuerza(mochila, objetos_sacados + 1)
        
   
mochila = ['piedra','papel','tijera','encendedor','tabaco','sable de luz','salchicha']

usar_la_fuerza(mochila)