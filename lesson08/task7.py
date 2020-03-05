class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        real_sum = self.real_part + other.real_part
        imaginary_sum = self.imaginary_part + other.imaginary_part
        return Complex(real_sum, imaginary_sum)

    def __mul__(self, other):
        real_mul = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        imaginary_mul = (self.real_part * other.imaginary_part) + (other.real_part * self.imaginary_part)
        return Complex(real_mul, imaginary_mul)

    def __str__(self):

        if self.imaginary_part == 0:
            return f'{self.real_part}'
        elif self.imaginary_part == 1:
            return f'{self.real_part} + i'
        elif self.imaginary_part == -1:
            return f'{self.real_part} - i'
        elif self.imaginary_part < 0:
            return f'{self.real_part} - {abs(self.imaginary_part)}i'
        elif self.imaginary_part > 0:
            return f'{self.real_part} + {self.imaginary_part}i'


x1 = Complex(3, -2)
y1 = Complex(1, 3)
x2 = Complex(5, -8)
y2 = Complex(3, 5)

print(x1 + y1)
print(x1 * y1)
print(x2 + y2)
print(x2 * y2)

