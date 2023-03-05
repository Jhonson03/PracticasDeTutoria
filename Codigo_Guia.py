#Primer ejemplo asignacion

Variable1 = 20
Variable2 = 35

Variable1 += Variable2

print(Variable1)

#Segundo ejemplo asignacion

Variable3 = int(input("Ingrese un numero -> "))
Variable4 = int(input("Ingrese su segundo numero -> "))

Variable3 -= Variable4

print(Variable3)

#Primer ejemplo de concatenacion

Variable5 = "Hola"
Variable6 = "Mundo"

print(Variable5+ " "+ Variable6)

#Segundo ejemplo de concatenacion

Variable7 = "Bienvenido"
Variable8 = "a la sesion de tutoria"

print(f"{Variable7} {Variable8}")

#Tercer ejemplo de concatenacion

Variable9 = "Fundamentos"
Variable10 = "de Programacion"

print('{} {}'.format(Variable9, Variable10))


#Primer Ejemplo de Busqueda

Varriable11 = ("Nombre1", "Nombre2", "Nombre3", "Nombre4")
print(Varriable11.count("Nombre2"))
#Retorna el valor de 1

#Ejemplo 2 de busqueda en subcadenas

cadena = "El arte desafia a la tecnologia y la tecnologia inspira al arte"

print(cadena.find("arte"))
print(cadena.find("\ntecnologia"))
print(cadena.find("\ninspira"))

#Primer Ejemplo de extraccion

Cadena2 = "Esta es una cadena"
subcadena = Cadena2[:18]
print(subcadena)

Cadena3 = "Un programador que escriba un codigo limpio"
Cadena4 = "entiende perfectamente el problema antes de escribir el codigo"

rango = slice(3, 18)

SubCadena1 = Cadena3[rango]
SubCadena2 = Cadena4[rango]

print(f"La subcadena 1 {SubCadena1}")
print(f"La subcadena 2 {SubCadena2}")

#Primer Ejemplo de Comparacion

num1 = 4
num2 = 7

Res1 = num1 < num2

print(Res1)

CadenaText1 = "Si puedes imaginarlo puedes programarlo"
CadenaText2 = "Si Puedes Imaginarlo Puedes Imaginarlo"

Res2 = CadenaText1 == CadenaText2

print(Res2)
