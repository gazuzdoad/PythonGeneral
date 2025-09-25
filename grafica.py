#Este programa gráfica funciones
for x in range(1,41,1):
    fila=""    
    for y in range(1,41,1):
        
        if x==21:
            fila+="+"
        elif y==21:
            fila+="+"
        else:
            fila+=" "
    print(fila)
