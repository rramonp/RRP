diccionario = dict(nombre="lucas", apellido="ramon")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto", "rancio"]): "jaja"}

#creando diccionarios con fromkeys() valor por defecto none
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() valor por defecto a "No se"
diccionario2 = dict.fromkeys(["nombre", "apellido"], "No se")

print(diccionario2["apellido"])


