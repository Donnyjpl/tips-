
# Tips clave para una prueba técnica de Python

# 1. Conceptos básicos de Python
# Variables, operadores, condicionales, bucles y list comprehensions.
squares = [x**2 for x in range(10)]
print(squares)  # Ejemplo de list comprehension

# 2. Funciones
# Definición de funciones y uso de lambda.
def suma(a, b):
    return a + b

f = lambda x: x + 2  # Ejemplo de función lambda
print(suma(3, 5))
print(f(4))

# 3. Manejo de errores
# Uso de try, except, else, y finally.
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print("Operación exitosa.")
finally:
    print("Bloque finally ejecutado.")

# 4. Estructuras de datos
# Listas, diccionarios y sets.
lista = [1, 2, 3, 4]
diccionario = {"clave1": "valor1", "clave2": "valor2"}
conjunto = {1, 2, 3, 4}

print(lista, diccionario, conjunto)

# 5. Manipulación de strings
# Uso de métodos como strip(), split(), join(), y f-strings.
nombre = "Juan"
saludo = f"Hola, {nombre}"
print(saludo)

# 6. Módulos y bibliotecas estándar
# Uso de módulos como math, random, datetime.
import math
print(math.sqrt(16))  # Raíz cuadrada de 16

# 7. Programación orientada a objetos (POO)
# Definición de clases, objetos, herencia, y uso de __init__.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona = Persona("Pedro", 30)
persona.saludar()

# 8. Comprensión de archivos
# Cómo leer y escribir archivos usando 'with' y open().
with open('archivo.txt', 'w') as f:
    f.write("Este es un archivo de ejemplo.")

# 9. Optimización del código
# Buenas prácticas y análisis de la eficiencia del código (Big O).

# 10. Pruebas unitarias
# Escribir pruebas usando unittest o pytest.

# 11. Trucos y consejos rápidos
# Uso del operador ternario, enumerate(), y zip().
n = 5
resultado = "Par" if n % 2 == 0 else "Impar"
print(resultado)

# 12. Generadores
# Uso de yield para manejar grandes cantidades de datos.
def generador():
    for i in range(5):
        yield i

for num in generador():
    print(num)

