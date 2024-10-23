# Método slice() para la generación de un objeto y poder reutilizarlo

a = [1, 2, 3, 4, 5, 6];
b = a;
print(a);
print(b);

## Cuando realizamos un cambio en a, el cambio ocurre automáticamente en b. Aunque no hayamos dado instrucción a b
## Este cambio es dado a que ambas variables, apuntan al mismo espacio en memoria

del a[2];
print(a);
print(b);

## Función id: saber el espacio en memoria de las variables

a = [1, 2, 3, 4, 5, 6];
b = a;
print(id(a));
print(id(b));

## Método slice: copear o extraer datos de una lista

a = [1, 2, 3, 4, 5, 6];
b = a
c = a[:]
print(id(a));
print(id(b));
print(id(c));

## Al realizar un cambio, ahora, ya no tendremos el mismo problema.

a = [1, 2, 3, 4, 5, 6];
b = a
c = a[:]
a.append(7);
print(a);
print(b);
print(c);

## Función .copy(), otra forma de copear

lista1 = [1,2,3,4,5];
lista2 = lista1.copy();
lista2.append(6);
print(lista1);
print(lista2);