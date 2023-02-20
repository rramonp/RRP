#creando conjunto con set()
conjunto = set(["Dato 1", "Dato 2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 3"}

#teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6}

#verificando si es subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#verioficar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)


