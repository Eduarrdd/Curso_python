# Diccionario en Python

numbers = {
	1:"Uno",
	2:"Dos",
	3:"Tres"
};
print(numbers);
print(type(numbers));


## Eliminar claves en diccionarios

personal_information = {
	"Nombre":"Eduardo",
	"Edad": 24,
	"Ciudad": "México",
	"Rol": "Data analyst"
};
print(personal_information);

del personal_information["Rol"];
print(personal_information);

## Modificando valores en diccionarios

personal_information = {
	"Nombre":"Eduardo",
	"Edad": 24,
	"Ciudad": "México",
	"Rol": "Data analyst"
};
print(personal_information);

personal_information["Edad"] = 25;
print(personal_information["Edad"]);


## Método .keys() para iterar las claves de un diccionario

objetos = {
	"Objeto":"Computadora",
	"Memoria Ram":"16 GB",
	"Memoria Interna":"1 TB",
	"Tarjeta Madre":"Asus",
	"Procesador":"AMD"
};
print(objetos);

clave = objetos.keys();
lista_claves = list(clave);
print(clave);
print(lista_claves);


## Utilizando el método .values() para obtener los valores del diccionario

valores = objetos.values();
lista_valores = list(valores);

print(valores);
print(lista_valores);

## Método .items()

objetos = {
	"Objeto":"Computadora",
	"Memoria Ram":"16 GB",
	"Memoria Interna":"1 TB",
	"Tarjeta Madre":"Asus",
	"Procesador":"AMD"
};
print(objetos);

pares = objetos.items();
lista_pares = list(pares);

print(pares);
print(lista_pares);
