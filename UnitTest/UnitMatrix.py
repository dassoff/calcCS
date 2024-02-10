import unittest
import tkinter as tk
from tkinter import ttk
from calt import Matrix

class TestMatrix(unittest.TestCase):

    def setUp(self):
        # Настройка окружения для тестов
        self.root = tk.Tk()  # Создание основного окна Tkinter
        self.tab = ttk.Frame(self.root)  # Создание вкладки для виджетов
        self.matrix_calculator = Matrix(self.tab)  # Создание экземпляра класса Matrix

    def test_add_matrices(self):
        self.matrix_calculator.dimension_entry.insert(0, "2")
        self.matrix_calculator.create_matrix()
        self.fill_matrix(self.matrix_calculator.matrix1, [[1, 2], [3, 4]])
        self.fill_matrix(self.matrix_calculator.matrix2, [[5, 6], [7, 8]])
        self.matrix_calculator.operation_combobox.set("Сложение")
        self.matrix_calculator.calculate()
        self.assertEqual(self.get_matrix_values(self.matrix_calculator.result_text), [[6, 8], [10, 12]])

    def test_subtract_matrices(self):
        # Тестирование вычитания матриц
        self.matrix_calculator.dimension_entry.insert(0, "2")  # Ввод размерности матрицы
        self.matrix_calculator.create_matrix()  # Создание матрицы
        # Заполнение матриц
        self.fill_matrix(self.matrix_calculator.matrix1, [[5, 4], [3, 2]])
        self.fill_matrix(self.matrix_calculator.matrix2, [[1, 1], [1, 1]])
        # Выполнение операции вычитания
        self.matrix_calculator.operation_combobox.set("Вычитание")
        self.matrix_calculator.calculate()
        # Ожидается, что результат вычитания будет [[4, 3], [2, 1]]
        self.assertEqual(self.get_matrix_values(self.matrix_calculator.result_text), [[4, 3], [2, 1]])

    def test_multiply_matrices(self):
        # Тестирование умножения матриц
        self.matrix_calculator.dimension_entry.insert(0, "2")  # Ввод размерности матрицы
        self.matrix_calculator.create_matrix()  # Создание матрицы
        # Заполнение матриц
        self.fill_matrix(self.matrix_calculator.matrix1, [[1, 2], [3, 4]])
        self.fill_matrix(self.matrix_calculator.matrix2, [[5, 6], [7, 8]])
        # Выполнение операции умножения
        self.matrix_calculator.operation_combobox.set("Умножение")
        self.matrix_calculator.calculate()
        # Ожидается, что результат умножения будет [[19, 22], [43, 50]]
        self.assertEqual(self.get_matrix_values(self.matrix_calculator.result_text), [[19, 22], [43, 50]])

    def test_transpose_matrix(self):
        # Тестирование транспонирования матрицы
        self.matrix_calculator.dimension_entry.insert(0, "2")  # Ввод размерности матрицы
        self.matrix_calculator.create_matrix()  # Создание матрицы
        # Заполнение матрицы
        self.fill_matrix(self.matrix_calculator.matrix1, [[1, 2], [3, 4]])
        # Выполнение операции транспонирования
        self.matrix_calculator.operation_combobox.set("Транспонирование")
        self.matrix_calculator.calculate()
        # Ожидается, что результат транспонирования будет [[1, 3], [2, 4]]
        self.assertEqual(self.get_matrix_values(self.matrix_calculator.result_text), [[1, 3], [2, 4]])

    def test_inverse_matrix(self):
        # Тестирование нахождения обратной матрицы
        self.matrix_calculator.dimension_entry.insert(0, "2")  # Ввод размерности матрицы
        self.matrix_calculator.create_matrix()  # Создание матрицы
        # Заполнение матрицы
        self.fill_matrix(self.matrix_calculator.matrix1, [[1, 2], [3, 4]])
        # Выполнение операции нахождения обратной матрицы
        self.matrix_calculator.operation_combobox.set("Обратная матрица")
        self.matrix_calculator.calculate()
        # Ожидается, что результат будет [[-2, 1], [1.5, -0.5]]
        self.assertEqual(self.get_matrix_values(self.matrix_calculator.result_text), [[-1.9999999999999996, 0.9999999999999998],
 [1.4999999999999998, -0.4999999999999999]])

    def test_determinant_matrix(self):
        # Тестирование нахождения определителя матрицы
        self.matrix_calculator.dimension_entry.insert(0, "2")  # Ввод размерности матрицы
        self.matrix_calculator.create_matrix()  # Создание матрицы
        # Заполнение матрицы
        self.fill_matrix(self.matrix_calculator.matrix1, [[1, 2], [3, 4]])
        # Выполнение операции нахождения определителя
        self.matrix_calculator.operation_combobox.set("Определитель")
        self.matrix_calculator.calculate()
        # Ожидается, что результат будет 1 * 4 - 2 * 3 = -2
        self.assertEqual(float(self.matrix_calculator.result_text.get("1.0", tk.END)), -2.0000000000000004)

    def fill_matrix(self, matrix, values):
        # Заполнение матрицы значениями из двумерного списка
        for i, row in enumerate(matrix):
            for j, entry in enumerate(row):
                entry.delete(0, tk.END)
                entry.insert(0, str(values[i][j]))

    def get_matrix_values(self, text_widget):
        # Получение значений матрицы из текстового виджета
        lines = text_widget.get('1.0', tk.END).strip().split('\n')
        return [list(map(float, line.split())) for line in lines]

    def tearDown(self):
        # Завершение работы окружения для тестов
        self.root.destroy()  # Уничтожение основного окна Tkinter

if __name__ == '__main__':
    unittest.main()
