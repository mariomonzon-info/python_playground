# Ejercicio 3 — función con anotaciones de tipo
# 
# Define una función que convierta °C → °F:
# 
# Nombre: c_to_f
# 
# Firma: def c_to_f(c: float) -> float:
# 
# Debe devolver el resultado (no imprimirlo).

def c_to_f(celsius: float) -> float:
    return celsius * (9/5) + 32

print(c_to_f(0))
print(c_to_f(37))
print(c_to_f(100))