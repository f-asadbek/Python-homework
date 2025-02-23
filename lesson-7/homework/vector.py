import math

class Vector:
    def __init__(self, *elements):
        self.elements = elements
    def __str__(self):
        return f"Vector{self.elements}"
    def __add__(self, other):
        if len(self.elements) != len(other.elements):
            raise Exception("Different dimensions are involved")
        return Vector(*(a + b for a, b in zip(self.elements, other.elements)))
    def __sub__(self, other):
        if len(self.elements) != len(other.elements):
            raise Exception("Different dimensions are involved")
        return Vector(*(a - b for a, b in zip(self.elements, other.elements)))
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.elements) != len(other.elements):
                raise Exception("Different dimensions are involved")
            return Vector(*(a * b for a, b in zip(self.elements, other.elements)))
        elif isinstance(other, int):
            return Vector(*(other * a for a in self.elements))
    def magnitude(self):
        return math.sqrt(sum(pow(a, 2) for a in self.elements))
    def normalization(self):
        return Vector(*(a / math.sqrt(sum(pow(a, 2) for a in self.elements)) for a in self.elements))


a = tuple(map(int, input("Enter vector coordinates: ").split()))
b = tuple(map(int, input("Enter vector coordinates: ").split()))
n = int(input("Enter a number: "))

v1 = Vector(*a)
v2 = Vector(*b)

print(f"""
The vectors:
{v1}
{v2}

Addition(v1 + v2):
{v1 + v2}

Subtraction(v2 - v1): 
{v2 - v1}

Dot product(v1 * v2):
{v1 * v2}

Scalar multiplication:
v1 * n: {v1 * n}
v2 * n: {v2 * n}

Magnitude:
v1: {round(v1.magnitude(), 3)}
v2: {round(v2.magnitude(), 3)}

Normalization:
v1: {v1.normalization()}    
v2: {v2.normalization()}
""")