def greet():
	print('Hola mundo')

greet()


def greet(name, last_name = 0):
	print(f'Hola {name} {last_name}, gusto verte nuevamente.')
"""
greet('Edu', 'Salazar')
greet(last_name = 'Reyes', name = 'Gerardo')
greet(last_name = input('Ingresa tu nombre: '), name = input('Ingresa tu apellido: '))"""


