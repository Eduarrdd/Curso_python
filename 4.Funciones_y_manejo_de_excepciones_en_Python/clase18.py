## Función Lambda

add = lambda a, b: a + b
print(add(35, 5))

# Ejemplo de uso de lambda con función map()

numeros = [1, 2, 3, 4]
resultado = list(map(lambda x: x ** 2, numeros))
print(resultado)

## Obteniendo números pares del 0 al 10

numbers = range(11)
pares = list(filter(lambda x: x%2 == 0, numbers))
print(pares)