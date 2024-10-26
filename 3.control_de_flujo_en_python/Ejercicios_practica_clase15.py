#**Imprimir números del 1 al 10**  
    #Escribe un bucle `for` que imprima los números del 1 al 10, inclusive.

for i in range(1, 11):
    print(i, end=" ");


#**Imprimir caracteres de una cadena**  
    #Escribe un bucle `for` que imprima cada carácter de la cadena `"Python"` en líneas separadas.


x = 'python'
for i in x:
    print(i);


#**Imprimir números del 1 al 100**  
    #Escribe un bucle `for` que imprima los números del 1 al 100 en una sola línea, separados por un espacio.

for i in range(1, 101):
    print(i, end=" ");

#**Imprimir el cuadrado de los números**  
    #Utiliza un bucle `for` para imprimir el cuadrado de los números del 1 al 10.

for i in range(1, 11):
    print(i ** 2, end= " ");


#**Sumar números pares en un rango**  
    #Escribe un bucle `for` que sume todos los números pares entre 1 y 50. Al final, imprime la suma total.

for i in range(1, 50):
    suma = i * 2;
    if i %2 == 0:
        print(suma);

#**Imprimir elementos de una lista en mayúsculas**  
    #Dada una lista de palabras `["python", "java", "c++", "javascript"]`, escribe un bucle `for` que imprima cada palabra en mayúsculas.

mayusculas = ["python", "java", "c++", "javascript"]
for i in mayusculas:
    print(i.upper())

# **Imprimir números mayores a 5**  
    #Dada la lista `[3, 5, 7, 9, 2, 8, 1]`, escribe un bucle `for` con un `if` que imprima solo los números mayores a 5.

numeros = [3, 5, 7, 9, 2, 8, 1];
for i in numeros:
    if i > 5:
        print(i, end=" ");


## while exercises

