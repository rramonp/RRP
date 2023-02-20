#No funciona en conjuntos
animales = ["pez", "perro", "gato", "loro", "cocodrilo"]
numeros = (12, 23, 45, 12, 45)

"""
#recorriendo la lista animales
for animal in animales:
     print(f'Ahora la variable animal es igual a: {animal}')
   
#recorriendo lista numeros multiplicando cada valor por 10
for numero in numeros:
    resultado = numero *10
     print(f"Tu numero multiplicado por 10 es: {resultado}")
   
#recorriendo dos listas del mismo tamaño al mismo tiempo con zip
for animal, numero in zip(animales,numeros):
    print(f"Recorriendo lista animales: {animal}")
    print(f"Recorriendo lista animales: {numero}")
       
#recorriendo con range
for num in range(20):
    print(num)
    
#forma no optima de recorrer lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
"""   
 
#forma correcta de recorrer una lista con su indice con enumerate
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice} y el valor es: {valor}")
    
#usando el for/else
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el índice es: {indice} y el valor es: {valor}")
else:
    print("FIN")
    
    
    
    
    
    
    
    
    
    