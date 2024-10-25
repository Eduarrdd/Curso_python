# Generadores e iteradores en Python

my_list = [1, 2, 3, 4];
my_iter = iter(my_list)
"""print(type(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))"""


## Iterar en cadenas con for

text = 'Hola';
cadena = iter(text);

for char in cadena:
	print(char);


## Creando iterador para números impares

limite = 10

odd_iter = iter(range(1, limite+1, 2))

for num in odd_iter:
	print(num);


## Generador: para secuencias de número que se puedan iterar.

def my_generator():
	yield 1
	yield 2
	yield 3

for value in my_generator():
	print(value);