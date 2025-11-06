try:
    numero = input("Escribe un numero :")  
    numero_entero= int(numero)

    if   numero_entero > 0:
     print(f"el {numero_entero} es positivo")
    elif numero_entero < 0:
        # Verifica si es menor que cero (ej: -1, -2, -3...)
        print(f"❌ El número {numero_entero} es NEGATIVO.")
        
    else:
        # Por descarte, si no es mayor que cero y no es menor que cero, es CERO
        print(f"💡 El número {numero_entero} es CERO.")
        
# 3. Manejo de la Excepción
except ValueError:
    # Este bloque se ejecuta si int() falla (el usuario escribió texto o un decimal)
    print(f"👀 Error de valor: Has escrito una cadena de texto o un decimal, no un número entero válido.")
