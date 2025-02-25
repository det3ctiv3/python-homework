import math
class Vector:
    def __init__(self, *components):
        self.components = tuple(components)

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar multiplication requires a number.")
        return Vector(*(a * scalar for a in self.components))

    def __matmul__(self, other):  # Dot product using @ operator
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))


# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)  # Vector(5, 7, 9)
print(v1 - v2)  # Vector(-3, -3, -3)
print(v1 * 2)  # Vector(2, 4, 6)
print(v1 @ v2)  # 32 (dot product)
print(v1.magnitude())  # 3.74...
print(v1.normalize())  # Vector(0.27, 0.53, 0.80)
