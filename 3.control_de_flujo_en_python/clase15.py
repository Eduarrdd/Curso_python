# Bucles e iteradores

## Bucle 'for'
numbers = [1, 2, 3, 4, 5];
for i in numbers:
	print('Números: ', i);

## For y y el uso de range()
for i in range(0, 5):
	print(i);


# For y condicional if 

fruits = ['Naranja', 'Manzana', 'Pera', 'Uva', 'Melón'];
for fruta in fruits:
	print(fruta);
	if fruta == 'Manzana':
		print('Hay manzana en la lista');


# Bucle while

x = 0

while x < 5:
	print(x);
	x += 0.5;

## Bucle while y condicional if
x = 0

while x < 5:
	x += 0.5
	print(x)
	if x == 2.0:
	    break

