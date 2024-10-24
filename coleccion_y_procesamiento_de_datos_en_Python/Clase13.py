# List comprehensions en Python: una forma concisa y sencilla de hacer listas en Python

cuadrados = [x**2 for x in range(10)];
print(cuadrados);

suma_constante = [x+2 for x in range(15)];
print(suma_constante);

## Otro ejemplo cambiando temperatura Celsius a Fahrenheit

Celsius = [-5, 0, 10, 15, 25, 30, 35, 40, 50];
temperatura = [(temp * 9/5) + 32 for temp in Celsius];
print(temperatura);


matriz = [
	[1, 2, 3,],
	[4, 5, 6],
	[7, 8, 9]
];
print(matriz);


transposed = [[row[i] for row in matriz] for i in range(len(matriz[0]))];
print(transposed);