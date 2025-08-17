
# Variables

name = "Tony"
print(f"String: {name} -> {type(name)}")


age = 42
print(f"Int: {age} -> {age}")

height = 1.756
print(f"Float: {height} -> {type(height)}")

print(f"Float: {1e3} -> {type(1e3)}")

isAlive = True
print(f"Boolean: {isAlive} -> {isAlive}")

print(f"Números complejos: {3 + 4j} -> {type(3 + 4j)}")

print(f"NoneType: {None} -> {type(None)}")

print(f"{name} ({age}) — {height:.2f} m")




c = float(input("Introduce la temperatura en grados"))
print(type(c))
f = c * (9/5) + 32
print(f"{c:.2f} °C → {f:.2f} °F")