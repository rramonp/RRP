#creando funcion con parametros
def preguntas():
    nombre = input("Dime tu nombre: ")
    apellido = input("Dime tu apellido: ")
    genero = input("Dime tu genero [h][m][n/s]")
    genero.lower()
    if genero == "h":
        genero = "Hombre"
    elif genero == "m":
        genero = "Mujer"
    else:
        genero = "Amor"
    return nombre, apellido, genero

def respuesta(nombre1, apellido1, genero1):
    print(f"Tu nombre es: {nombre1} tu apellido es {apellido1} y tu genero es {genero1}")
    
nombre1, apellido1, genero1 = preguntas()
respuesta(nombre1, apellido1, genero1)

















