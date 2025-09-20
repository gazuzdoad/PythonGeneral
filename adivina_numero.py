#Este programa genera un número aleaorio entre 1 y 5.
#importar biblioteca
import random
def aleatorio():
    return random.randint(1,5)
    

if __name__=="__main__":


    print("Adivina un número entre 1 y 5")
    ran=aleatorio()
    
    while True:
        numero=int(input("Adivina="))
        if numero>5 or numero<1:
            print("Debe ser un número entre 1 y 5")
            False
        elif numero==ran:
            print(f"!Fecilicades adivinaste¡ el número es {numero}")
            True
            break
        else:
            print(f"{ran} no es igual a tu respuesta {numero}")
            print("Prueba de nuevo")
            False
