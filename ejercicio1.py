class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

punto_a = Punto(3, 5)
punto_b = Punto(3, 5)

# Aunque tienen los mismos valores, son objetos DISTINTOS
print(punto_a == punto_b)   # False (por defecto compara identidad)
print(punto_a is punto_b)   # False (son objetos diferentes en memoria)

# Modificar uno no afecta al otro
punto_a.x = 100
print(punto_a.x)   # 100
print(punto_b.x)   # 3  ← no cambió
