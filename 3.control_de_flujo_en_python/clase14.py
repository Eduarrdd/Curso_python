# Estructuras condicionales

## If

x = 5
if x > 5:
	print("X es mayor a 5");
if not x > 5:
	print("X no es mayor a 5. Intenta nuevamente");

## Estructura 'if-else'

x = 10
if x >= 10:
	print("X es igual o mayor a 10");
else:
	print("X no es igual o mayor a 10");

## Estructura 'if-elif-else'

x = 10

if x > 10:
	print("x es mayor a 10");
elif x == 10:
	print("x es igual a 10");
else:
	print("x es menor a 10");


## Validando dos variables

x = 10
y = 15

if x > 5 and y > 20:
	print("x es mayor que 5 Y y es mayor que 20");
if x > 5 or y > 20:
	print("x es mayor que 5 O y es mayor que 20");
if not y > 20:
	print("y no es mayor que 20");

