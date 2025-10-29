nombre= input("Nombre del Gato: ")
edad= input("edad del gato: ")
try:
  int(edad)
  print (f"nombre del gato {nombre} la edad del gato es : {edad} ")
except ValueError:
  print(edad , "❌ tienes que poner un numero entero ")