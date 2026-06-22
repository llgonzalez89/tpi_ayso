# Lista vacía para almacenar las notas
notas = []

# Solicitar tres notas
for i in range(3):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

# Calcular promedio
promedio = sum(notas) / len(notas)

# Mostrar resultado
print(f"El promedio es: {promedio:.2f}")