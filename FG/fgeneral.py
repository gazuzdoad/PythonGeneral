#Este programa cálcula la fórmula general
import math
a=float(input("Dame el valor de a: "))  
b=float(input("Dame el valor de b: "))
c=float(input("Dame el valor de c: "))  
#Calculamos el discriminante de la ecuación
dis=math.pow(b,2)-4*a*c
if dis<0:
    print("No hay solución real")
elif dis==0:
    x=-b/(2*a)
    print(f"Hay una solución real:{x}")
else:
    x1=(-b+math.sqrt(dis))/(2*a)
    x2=(-b-math.sqrt(dis))/(2*a)
    print(f"Hay dos soluciones reales: {x1} y {x2}")    
print("Fin del programa")
    
