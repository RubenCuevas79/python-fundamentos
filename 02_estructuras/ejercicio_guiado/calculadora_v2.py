"""
Calculadora v2 - Cuatro operaciones básicas
============================================

En esta segunda versión expandirás la calculadora para que pueda realizar
las cuatro operaciones básicas: suma, resta, multiplicación y división.

Conceptos aplicados:
- Operadores aritméticos (+, -, *, /)
- Condicionales if/elif/else
- F-strings para formateo profesional
- Manejo básico de tipos numéricos

Instrucciones:
1. Pide dos números al usuario
2. Pregunta qué operación desea realizar
3. Usa if/elif/else para realizar la operación correspondiente
4. Muestra el resultado con f-strings formateados
"""

# TODO 1: Pide el primer número al usuario y conviértelo a float
# num1 = ...
numero_a= float(input("pon un muero "))



# TODO 2: Pide el segundo número al usuario y conviértelo a float
# num2 = ...
numero_b= float(input("pon el segundo numero "))

# TODO 3: Pregunta qué operación desea realizar
# Pista: input("¿Qué operación deseas realizar? (+, -, *, /): ")
# operacion = ...
operacion = input(" ¿Qué operación quieres realizar? (+ , - , / ):")


# TODO 4: Realiza la operación correspondiente usando if/elif/else
# Pista: Compara la variable 'operacion' con "+", "-", "*", "/"
#
# if operacion == "+":
#     resultado = num1 + num2
# elif operacion == "-":
#     ...
# elif operacion == "*":
#     ...
# elif operacion == "/":
#     ...
# else:
#     print("❌ Operación no válida")
if operacion == "+":
    resul= numero_a + numero_b
elif operacion == "-":
    resul= numero_a - numero_b
elif operacion == "*":
    resul= numero_a * numero_b
elif operacion == "/":
    resul= numero_a / numero_b
else:
   mal= print("❌ operación no válida")

# TODO 5: Muestra el resultado usando f-strings
# Pista: f"El resultado de {num1} {operacion} {num2} = {resultado:.2f}"
# El :.2f muestra solo 2 decimales
# print(f"...")
print(f"el resultado del numero uno  {numero_a} y la operacion realizada es {operacion} del numero dos {numero_b} el resultado es {resul:.2f}")


# ¡Perfecto! Ahora tu calculadora puede hacer las 4 operaciones básicas
#
# Ejemplos para probar:
# - 10 + 5 → debe dar 15.00
# - 10 - 3 → debe dar 7.00
# - 4 * 5 → debe dar 20.00
# - 10 / 3 → debe dar 3.33
# - 10 % 3 → (si pruebas una operación no válida, debe mostrar mensaje de error)
#
# 💡 Nota: Si intentas dividir por cero (10 / 0), Python mostrará un error.
#    Esto lo arreglaremos en la v3 con validación de entrada.
