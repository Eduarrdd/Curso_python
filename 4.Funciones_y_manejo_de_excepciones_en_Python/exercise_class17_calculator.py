## Calculadora con funciones

def add (a, b):
	return a + b

def substraction (a, b):
	return a - b

def multiply (a, b):
	return a * b

def divide (a, b):
	return a / b

def calculator ():
	while True:
		print('Selecciona una operación')
		print('1. Suma')
		print('2. Resta')
		print('3. Multiplicación')
		print('4. División')
		print('5. Salir de la calculadora')
		opciones = [1, 2, 3, 4, 5]
		option = int(input('Ingrese una opción (1, 2, 3, 4, 5) '))
		if option in opciones:
			print('Vamos a comenzar con el cálculo...')
		else:
			print('                             Por favor agrega una opción correcta'.upper())

		if option == 5:
			print('Saliendo de la calculadora...')
			break

		if option in [1, 2, 3, 4]:
			num1 = float(input('Ingresa el primer número: '))
			num2 = float(input('Ingresa el segundo número: '))
			
			if option == 1:
				print(f'La suma de {num1} y {num2}, es igual a: ', add(num1, num2))
				break
			elif option == 2:
				print(f'La resta de {num1} y {num2}, es igual a: ', substraction(num1, num2))
				break
			elif option == 3:
				print(f'La multiplicación de {num1} y {num2}, es igual a: ', multiply(num1, num2))
				break
			elif option == 4:
				print(f'La división de {num1} y {num2}, es igual a: ', divide(num1, num2))
				break
			else:
				print('Esta opción no es valida. Intenta de nuevo')
                
calculator()