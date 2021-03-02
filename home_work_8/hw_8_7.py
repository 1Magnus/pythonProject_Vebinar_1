# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, x, j):
        self.x = x
        self.j = j
        self.complex_numb = complex(x, j)

    def __add__(self, other):
        result = self.complex_numb + other.complex_numb
        return ComplexNumbers(result.real, result.imag)

    def __mul__(self, other):
        result = self.complex_numb * other.complex_numb
        return ComplexNumbers(result.real, result.imag)

    def __str__(self):
        return f"Комплексное число - {self.complex_numb}"


complex_1 = ComplexNumbers(1, 2)
complex_2 = ComplexNumbers(2, 3)
complex_3 = ComplexNumbers(3, 4)

print(complex_1 + complex_2 + complex_3)
print(complex_1 * complex_2 * complex_3)
