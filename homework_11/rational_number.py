import math
class Rational:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self.__normalize()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f'{self.__numerator} / {self.__denominator}'

    def __mul__(self, other: 'Rational'):
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __floordiv__(self, other: 'Rational'):
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __add__(self, other):
        newnum = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        newden = self.__denominator * other.__denominator
        return Rational(newnum, newden)

    def __sub__(self, other):
        newnum = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        newden = self.__denominator * other.__denominator
        return Rational(newnum, newden)

    def __ge__(self, other: 'Rational'):
        return self.__numerator / self.__denominator >= other.__numerator / other.__denominator

    def __le__(self, other: 'Rational'):
        return self.__numerator / self.__denominator <= other.__numerator / other.__denominator

    def __eq__(self, other: 'Rational'):
        return self.__numerator / self.__denominator == other.__numerator / other.__denominator

    def __ne__(self, other: 'Rational'):
        return self.__numerator / self.__denominator != other.__numerator / other.__denominator

    def __gt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator > other.__numerator / other.__denominator

    def __lt__(self, other: 'Rational'):
        return self.__numerator / self.__denominator < other.__numerator / other.__denominator

    def __normalize(self):
        if self.__denominator < 0 and self.__numerator < 0 or self.__denominator < 0:
            self.__numerator *= -1
            self.__denominator *= -1

        gcd = math.gcd(self.__numerator, self.__denominator)
        if gcd > 1:
            self.__numerator //= gcd
            self.__denominator //= gcd


if __name__ == '__main__':
    num = Rational(7, 10)
    num2 = Rational(1, 10)
    assert num.numerator == 7
    assert num.denominator == 10
    assert num2.denominator == 10
    assert str(num) == '7 / 10'
    assert str(num2) == '1 / 10'
    assert Rational(2, 3) > Rational(1, 3)
    assert Rational(2, 10) < Rational(4, 5)
    assert Rational(1, 10) >= Rational(1, 100)
    assert Rational(2, 3) >= Rational(2, 3)
    assert Rational(1, 55) <= Rational(1, 55)
    assert Rational(1, 3) <= Rational(1, 2)
    assert Rational(1, 6) == Rational(1, 6)
    assert Rational(1, 8) + Rational(1, 8) == Rational(1, 4)
    assert Rational(3, 2) - Rational(1, 2) == Rational(1, 1)
    assert Rational(4, 9) * Rational(6, 12) == Rational(2, 9)
    assert Rational(7, 17) // Rational(49, 34) == Rational(2, 7)
    assert Rational(1, 3) != Rational(1, 4)
    print(Rational(-4, 7))
    print(Rational(-1, -2))
    print(Rational(1, -5))
    print(Rational(1, 5) + (Rational(3, 4) + Rational(1, 8)) * Rational(4, 5))