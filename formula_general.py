#Este programa da solución a ecuaciones de segundo grado por medio de la fórmula general.
#Lectura de coeficientes
#Importar bibliotecas
import math
def formula_general(a,b,c):
  if a==0:
    return "No es una ecuación cuadrática"
  dis=b**2-4*a*c
  if dis<0:
    return "No tiene soluciones reales."
  elif dis==0:
    x=-b/(2*a)
    return f"Una solución real: x={x}"
  else:
    x1=(-b+math.sqrt(dis))/(2*a)
    x2=(-b-math.sqrt(dis))/(2*a)
    return f"Dos soluciones reales: x1={x1}, x2={x2}"
    
if __name__=="__main__":
  print("Solución a la ecuación ax^2+bx+c=0")
  a=float(input("coeficiente a="))
  b=float(input("coeficiente b="))
  c=float(input("coeficiente c="))

resultado=formula_general(a,b,c)
print(resultado)
