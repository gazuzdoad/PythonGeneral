#Este programa juega tik-tak-toe generando número aleatorio
#En cada ciclo vamos a generar 2 números aleatorios que van a generar coordenadas x y y.
import random
almacen=[]
for i in range(1,5):
    x=random.randint(0,2)
    y=random.randint(0,2)
    print(x,y)
    almacen.append((x,y))
print(almacen)    

