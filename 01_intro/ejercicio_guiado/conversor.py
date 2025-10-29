numero_uno= input("pon un numero: ")

try:
  float (numero_uno)
  print(f"el numero es: {numero_uno}")  
except ValueError:
  print(f"el {numero_uno} tienes que poner un numero ❌ no un texto ")