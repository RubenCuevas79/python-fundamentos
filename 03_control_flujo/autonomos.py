

gato= ["pipo","copo","luna","calcetines"]
  
   
for numero in gato: 
    print(f"nombres de los gatos es . {numero}")
    print(len(numero))


tabla=[1,2,3,4,5,6,7,8,9,10]
 
for i in tabla:
      for h in tabla:    
       print(f"{i} x {h}= {i * h}")

con = "gato123"  # contraseña guardada
# while es un bucle con True pide al usuario contra
while True:
    usuario = input("Introduce la contraseña: ")
    # con un condicional if compruebas la variable si conincide con
    if usuario == con:
        print("✅ Contraseña correcta. Bienvenido.")
        break  # sale del bucle
    else:
        print("📛 Contraseña incorrecta. Intenta de nuevo.")
    #else cuando la contraseña que introduces es la incorrecta