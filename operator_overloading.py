class Multiplier:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Multiplier):
            return Multiplier(self.value * other.value)
        elif isinstance(other, (int, float)):
            return Multiplier(self.value * other)
        else:
            raise TypeError("Unsupported operand type.")

    def __str__(self):
        return f"Multiplier({self.value})"


m1 = Multiplier(5)

m2 = m1 + Multiplier(3)
print(m2)  # Output: Multiplier(15)

m3 = m1 + 2
print(m3)  # Output: Multiplier(10)
