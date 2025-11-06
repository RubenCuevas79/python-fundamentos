
# Pedimos datos
num_gatos = int(input("¿Cuántos gatos hay?: "))
cuidador_a = input("Nombre del cuidador del Turno A: ")
cuidador_b = input("Nombre del cuidador del Turno B: ")

# Listas para turnos
turno_a = []
turno_b = []

# Asignación alternada
for i in range(1, num_gatos + 1):
    nombre_gato = input(f"Nombre del gato {i}: ")

    # Si el número del gato es impar -> Turno A, si es par -> Turno B
    if i % 2 == 1:
        turno_a.append(nombre_gato)
    else:
        turno_b.append(nombre_gato)

# Resultado
print("\n🐾 Asignación de gatos por turnos:")
print(f"\nTurno A - Cuidador: {cuidador_a}")
for gato in turno_a:
    print(f"  🐱 {gato}")

print(f"\nTurno B - Cuidador: {cuidador_b}")
for gato in turno_b:
    print(f"  🐱 {gato}")


