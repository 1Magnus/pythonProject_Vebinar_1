# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    # =================================================================================================================

    def __str__(self):
        summers = ''
        new_list_matrix = []
        new_matrix = []
        max_len = max([len(str(e)) for r in self.matrix for e in r]) + 3
        for list_matrix in self.matrix:
            for cir in list_matrix:
                new_cir = str(cir).ljust(max_len)
                new_list_matrix.append(new_cir)
            new_matrix.append(new_list_matrix)
            new_list_matrix = []

        for list_matrix in new_matrix:
            result = ''.join(list_matrix) + '\n'
            summers = summers + result
        return summers

    # =================================================================================================================

    def __add__(self, other):
        line = len(self.matrix)
        column = len(self.matrix[0])
        line_other = len(other.matrix)
        column_other = len(other.matrix[0])
        result_list = []
        result_matrix = []
        if line == line_other and column == column_other:
            for line_matrix in range(line):
                for numb_el_line in range(column):
                    result = self.matrix[line_matrix][numb_el_line] + other.matrix[line_matrix][numb_el_line]
                    result_list.append(result)
                result_matrix.append(result_list)
                result_list = []
        else:
            return 'Матрицы не равны!'
        return Matrix(result_matrix)
    # =================================================================================================================


matrix_1 = Matrix([[9, 8123, 7],
                   [6, 54465464, 4],
                   [3, 2, 1]])

matrix_2 = Matrix([[1, 2, 3],
                   [4, 5, 6]])

matrix_3 = Matrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# =================================================================================================================

print(matrix_1)
print(matrix_2)
print(matrix_3)

print(matrix_1 + matrix_2)
print()
print(matrix_1 + matrix_3 + matrix_1)
