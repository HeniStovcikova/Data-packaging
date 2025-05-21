from math import gcd

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:  # Záporný menovateľ presunieme hore
            self.numerator *= -1
            self.denominator *= -1

    def __add__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        return isinstance(other, Fraction) and self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"


def test_fraction():

    assert str(Fraction(2, 4)) == "1/2"
    assert str(Fraction(6, -8)) == "-3/4"
    assert str(Fraction(-6, -8)) == "3/4"
    assert str(Fraction(0, 5)) == "0"

    # Sčítanie
    assert str(Fraction(1, 2) + Fraction(1, 3)) == "5/6"

    # Odčítanie
    assert str(Fraction(3, 4) - Fraction(1, 4)) == "1/2"

    # Násobenie
    assert str(Fraction(2, 3) * Fraction(3, 4)) == "1/2"

    # Delenie
    assert str(Fraction(1, 2) / Fraction(1, 4)) == "2"

    # Porovnanie
    assert Fraction(2, 4) == Fraction(1, 2)
    assert Fraction(3, -6) == Fraction(-1, 2)

    print("Všetky testy prešli úspešne ✅")

test_fraction()