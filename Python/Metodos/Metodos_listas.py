
lista = [1, 11123, 12, 333334, True, False]
print(lista)
print("La lista tiene", len(lista), "elementos")
 
# Añadir a lista con APPEND (lo coloca al final)
lista.append(input("Introduce el valor a añadir a la lista: "))

# Añadir a lista un elemento con INSERT (permite elegir posición)
nuevo_dato = input("Que dato quieres añadir a la lista: ")
posicion_nuevo_dato = int(input("En que posición quieres añadirlo: "))
lista.insert(posicion_nuevo_dato, nuevo_dato)

# Añadir varios elementos con EXTEND (AÑADIMOS NUEVA LISTA EN LA ACTUAL)
valor1 = int(input("Introduce el numero º1 de la nueva lista a añadir a la actual: "))
valor2 = int(input("Introduce el numero º2 de la nueva lista a añadir a la actual: "))
lista.extend([valor1,valor2])

# Eliminar valor de lista con POP(posicion)
# -1 Ultimo, -2 Penultimo, etc
eliminar_posicion = int(input("Introduce la posicion del valor de la lista que quieres eliminar: "))
lista.pop(eliminar_posicion)

#Eliminar elemento por su valor con REMOVE
eliminar_valor = int(input("Introduce el valor de la lista que quieres eliminar: "))
lista.remove(eliminar_valor)

# Eliminar todos los elementos de una lista con CLEAR
lista.clear()

# Ordenar lista de forma ascendente con SORT
lista.sort() # Descendente con lista.sort(reserve=True)

# Invertir los elementos con REVERSE
lista.reverse()

# Verificar si elemento esta en lista y devolver posisicon
elemento_a_buscar = int(input("Que valor deseas encontrar? "))
elemento_encontrado = lista.index(elemento_a_buscar)
print("Tu elemento estaba en la posicion:", elemento_encontrado)

print("")
print("Tu lista ahora es:", lista)
print("La lista ahora tiene", len(lista), "elementos")

lista.sort()
print("")
print("Lista ordenada:", lista)
print("")
