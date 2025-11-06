# Usamos el bucle 'while True' para que el proceso se repita indefinidamente.
# Programa que pide dos números y los suma hasta que el usuario escriba 'salir'

while True:
    print("\n= SUMAR")
    
    # Pedimos el primer número como texto
    numero_uno = input("Dime el primer número (o 'salir'): ")
    
    # Si el usuario quiere salir
    if numero_uno.lower() == 'salir':
        print("¡Hasta pronto! ")
        break
    
    # Intentamos convertir a número
    try:
        numero_uno = float(numero_uno)
    except ValueError:
        print("❌ Error: Por favor, introduce un número válido.")
        continue  # Vuelve al inicio del bucle

    # Pedimos el segundo número
    numero_dos = input("Dime el segundo número (o 'salir'): ")
    
    if numero_dos.lower() == 'salir':
        print("¡Hasta pronto! ")
        break
    
    try:
        numero_dos = float(numero_dos)
    except ValueError:
        print("❌ Error: Por favor, introduce un número válido.")
        continue

    # Hacemos la suma
    suma = numero_uno + numero_dos
    print(f"✅ La suma de {numero_uno} + {numero_dos} = {suma}")