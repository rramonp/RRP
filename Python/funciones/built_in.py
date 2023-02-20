numeros = [4,1,233,12,333,3333]

#encontrado el nº mayor de una lista
numero_mas_alto = max(numeros)
print(f"El numero mas alto es: {numero_mas_alto}")

#encontrado el nº mayor de una lista
numero_mas_bajo = min(numeros)
print(f"El numero mas bajo es: {numero_mas_bajo}")

#redondeando a X decimales
numero = 12.337365345533233
numero_redondeado = round(numero, 2)
print(f"{numero} redondeado con 2 decimales es {numero_redondeado}")

#funcion bool retorna False -> 0, vacio, False, None \ True -> distinto a 0, true, cadena, 
# datos no vacio
resultado_bool = bool(numeros)
print(resultado_bool)

#ALL retorna True, si todos los valores son verdaderos
resultado_all = all([234, "true", [111, 23]])
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(f"La suma de todos los numeros es {suma_total}")

