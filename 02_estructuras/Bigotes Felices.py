try:
   gato_uno=int(input ("macar el peso del primer gato: "))
   gato_dos= int(input ("macar el peso del segundo gato: "))
   gato_tres=int(input ("macar el peso del tercer gato: "))

   if gato_uno >= 0:
     input(f"el primer gato es {gato_uno} kg")

   else:
      input(f"el peso del primer gato no puede ser negativo")

   if gato_dos >= 0:
     input(f"el segundo gato es {gato_dos} kg")

   else:
      input(f"el peso del segundo gato no puede ser negativo")

   if gato_tres >= 0:
     input(f"el peso del tercer gato es {gato_tres} kg")

   else:
      input(f"el peso del tercer gato no puede ser negativo")    
except ValueError:
      input(f"❌ lo que has puesto no es un numero")