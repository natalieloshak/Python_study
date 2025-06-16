class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не дорівнює нулю")
        if b < 0:
            a = -a
            b = -b
        self.a = a
        self.b = b

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __add__(self, other):
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Fraction(a, b)

    def __sub__(self, other):
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Fraction(a, b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


# юніт тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == "Fraction: 21, 18"  # 3/6 + 2/3 = 9/18 + 12/18 = 21/18
f_d = f_b * f_a
assert str(f_d) == "Fraction: 6, 18"  # (3*2)/(6*3) = 6/18
f_e = f_a - f_b
assert str(f_e) == "Fraction: 3, 18"  # 2/3 - 3/6 = 12/18 - 9/18 = 3/18

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print("OK")
