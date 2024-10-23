# Listas en Python
## Ejemplo con una lista de quehaceres

to_do = ['Lavar los platos', 'Barrer el cuarto', 'Organizar escritorio', 'Hacer la comida', 'Tirar la basura'];
print(to_do);

## En las listas, podemos guardar diferentes valores como strings, floats, integers, booleans and even lists.

mix = [1, 2, 'tres', True, 4.15, [1,2,3]];
print(mix);

## También podemos utilizar algunas funciones y obtener index de la lista

mix = [1, 2, 'tres', True, 4.15, [1,2,3]];
print(len(mix));

mix = [1, 2, 'tres', True, 4.15, [1,2,3]];
print("El sexto elemento es ", mix[5]);

## Slicing: técnica útil para extraer secuencias de listas, strings o tuplas.

numeros = [10, 20, 30, 40, 50, 60, 70]
sub_lista = numeros[1::2]
print(sub_lista);

## Método .append() para agregar un valor al final de la lista
mix = [1, 2, 'tres', True, 4.15, [1,2,3]];
mix.append('nuevo valor al final de la lista');
print(mix);


## Método .insert() para agregar un valor a la lista en posición que instruyamos

mix = [1, 2, 'tres', True, 4.15, [1,2,3]];
mix.insert(3,'nuevo valor en posición 3');
print(mix);

## Consultar index con .index() para saber posición de valor

mix = [1, 2, 'tres', True, 4.15, [1,2,3]];
index_mix = mix.index(2);
print(index_mix);


## Max y Min en para obtener valor menor y mayor en una lista en Python

numbers = [1, 2, 3, 90.3, 0.391, 173];
maximo_numbers = max(numbers);
minimo_numbers = min(numbers);
print(f'Número máximo: {maximo_numbers}');
print(f'Número mínimo: {minimo_numbers}');

## Eliminar valores en la lista, eliminar partes o la lisma completa

numbers = [1, 2, 3, 90.3, 0.391, 173];
del numbers[3];
print(numbers);
del numbers[0:2];
print(numbers);

### Eliminar lista
eliminar_lista = [1, 2, False, 'eliminar lista', [1,4, 90.5]];
print(eliminar_lista)
del eliminar_lista
print(eliminar_lista)