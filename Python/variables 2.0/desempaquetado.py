#creando los datos
datos_tupla = ("Lucas", "Rafa",1000)
datos_lista = ["Lucas", "Rafa",1000]

#desempaquetado
nombre,apellidos,subscriptores = datos_tupla
nombre1,apellidos1,subscriptores1 = datos_lista

datos_lista[1] = "Ramon"

print(datos_lista[1])