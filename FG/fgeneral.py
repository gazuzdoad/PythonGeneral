#Este programa cálcula la fórmula general
import math
import tkinter as tk
from tkinter import messagebox
#Crear la ventana principal
root = tk.Tk()
root.title("Solución de ax²+bx+c=0")
root.geometry("500x500")
#Arreglo de campos y etiquetas
e1=tk.Label(root, text="Valor de a:")
e1.pack()  
a1=tk.Entry(root)
a1.pack() 
e2=tk.Label(root, text="Valor de b:")
e2.pack()
b1=tk.Entry(root)
b1.pack()
e3=tk.Label(root, text="Valor de c:")
e3.pack()
c1=tk.Entry(root)
c1.pack()   
#Etiqueta y  para mostrar el resultado
res=tk.Label(root, text="Resultado:")
res.pack()

#Función para calcular la solución

def calcular_solucion():
    try:
        a = float(a1.get())
        b = float(b1.get())
        c = float(c1.get())
    except ValueError:
        # Muestra un mensaje de error al usuario
        tk.messagebox.showerror("Error", "Por favor ingresa valores numéricos en todos los campos.")
        return
    #Discriminante
    dis=math.pow(b,2)-4*a*c
    if dis<0:
        resultado="Resultado","No existe solución real"
    elif dis==0:
        x=-b/(2*a)
        resultado="Resultado","Solución única: x=%.2f" %x
    else:
        x1=(-b+math.sqrt(dis))/(2*a)
        x2=(-b-math.sqrt(dis))/(2*a)
        resultado="Resultado","Soluciones: x1=%.2f y x2=%.2f" %(x1,x2)
    res.config(text=resultado)


#Botón para calcular
boton_calcular=tk.Button(root, text="Calcular", command=calcular_solucion)
boton_calcular.pack()

boton=tk.Button(root, text="Cerrar", command=root.destroy)
boton.pack()
#Posiccion de los elementos
e1.place(x=50,y=50)
e2.place(x=50,y=100)
e3.place(x=50,y=150)
a1.place(x=200,y=50)    
b1.place(x=200,y=100)
c1.place(x=200,y=150)
res.place(x=50,y=300)
boton_calcular.place(x=50,y=200)
boton.place(x=50,y=250)    


root.mainloop()
