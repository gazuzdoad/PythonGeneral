#Este programa gráfica funciones
#Valores
X=[]
Y=[]
for x in range(-20,21,1):
   y=2*x+5
   X.append(x)
   Y.append(y) 
print(X)
print(Y)
ymin=min(Y)
ymax=max(Y)
print(ymin,ymax)

#Grafica
for j in range(ymax,ymin,1):
    fila=""    
    for i in range(-20,21,1):
        
        if i==0:
            fila+="+"
        elif j==0:
            fila+="+"
        elif j==Y(ymax-j):
            fila+="*"
        else:
            fila+=" "
    print(fila)
