import unittest
import tkinter as tk
from tkinter import ttk
from calt import ComplexNumbers

class TestComplexNumbers(unittest.TestCase):

    def setUp(self):
        # Настройка окружения для тестов
        self.root = tk.Tk()  # Создание основного окна Tkinter
        self.tab3 = ttk.Frame(self.root)  # Создание вкладки для виджетов
        self.complex_numbers = ComplexNumbers(self.tab3)  # Создание экземпляра класса ComplexNumbers

    def test_addition(self):
        # Тестирование операции сложения
        self.complex_numbers.num1_entry_real.delete(0, tk.END)  # Очистка поля ввода для реальной части первого числа
        self.complex_numbers.num1_entry_real.insert(0, "2")  # Вставка значения в поле ввода для реальной части первого числа
        self.complex_numbers.num1_entry_imaginary.delete(0, tk.END)  # Очистка поля ввода для мнимой части первого числа
        self.complex_numbers.num1_entry_imaginary.insert(0, "3")  # Вставка значения в поле ввода для мнимой части первого числа
        self.complex_numbers.num2_entry_real.delete(0, tk.END)  # Очистка поля ввода для реальной части второго числа
        self.complex_numbers.num2_entry_real.insert(0, "1")  # Вставка значения в поле ввода для реальной части второго числа
        self.complex_numbers.num2_entry_imaginary.delete(0, tk.END)  # Очистка поля ввода для мнимой части второго числа
        self.complex_numbers.num2_entry_imaginary.insert(0, "4")  # Вставка значения в поле ввода для мнимой части второго числа
        self.complex_numbers.operation_var.set("+")  # Установка операции сложения
        self.complex_numbers.calculate()  # Выполнение расчета
        # Проверка, что результат сложения верен
        self.assertEqual(self.complex_numbers.result_entry_real.get(), "3.0")
        self.assertEqual(self.complex_numbers.result_entry_imaginary.get(), "7.0")

    # Добавлены тесты для операций вычитания, умножения, деления и извлечения квадратного корня
    def test_subtraction(self):
        # Тестирование операции вычитания
        self.complex_numbers.num1_entry_real.delete(0, tk.END)
        self.complex_numbers.num1_entry_real.insert(0, "5")
        self.complex_numbers.num1_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num1_entry_imaginary.insert(0, "2")
        self.complex_numbers.num2_entry_real.delete(0, tk.END)
        self.complex_numbers.num2_entry_real.insert(0, "3")
        self.complex_numbers.num2_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num2_entry_imaginary.insert(0, "1")
        self.complex_numbers.operation_var.set("-")
        self.complex_numbers.calculate()
        self.assertEqual(self.complex_numbers.result_entry_real.get(), "2.0")
        self.assertEqual(self.complex_numbers.result_entry_imaginary.get(), "1.0")

    def test_multiplication(self):
        # Тестирование операции умножения
        self.complex_numbers.num1_entry_real.delete(0, tk.END)
        self.complex_numbers.num1_entry_real.insert(0, "2")
        self.complex_numbers.num1_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num1_entry_imaginary.insert(0, "1")
        self.complex_numbers.num2_entry_real.delete(0, tk.END)
        self.complex_numbers.num2_entry_real.insert(0, "3")
        self.complex_numbers.num2_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num2_entry_imaginary.insert(0, "2")
        self.complex_numbers.operation_var.set("*")
        self.complex_numbers.calculate()
        self.assertEqual(self.complex_numbers.result_entry_real.get(), "4.0")
        self.assertEqual(self.complex_numbers.result_entry_imaginary.get(), "7.0")

    def test_division_by_zero(self):
        # Тестирование деления на ноль
        self.complex_numbers.num1_entry_real.delete(0, tk.END)
        self.complex_numbers.num1_entry_real.insert(0, "4")
        self.complex_numbers.num1_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num1_entry_imaginary.insert(0, "3")
        self.complex_numbers.num2_entry_real.delete(0, tk.END)
        self.complex_numbers.num2_entry_real.insert(0, "0")
        self.complex_numbers.num2_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num2_entry_imaginary.insert(0, "0")
        self.complex_numbers.operation_var.set("/")
        self.complex_numbers.calculate()
        self.assertEqual(self.complex_numbers.result_entry_real.get(), "Ошибка: деление на ноль!")
        self.assertEqual(self.complex_numbers.result_entry_imaginary.get(), "")

    def test_square_root(self):
        # Тестирование операции извлечения квадратного корня
        self.complex_numbers.num1_entry_real.delete(0, tk.END)
        self.complex_numbers.num1_entry_real.insert(0, "4")
        self.complex_numbers.num1_entry_imaginary.delete(0, tk.END)
        self.complex_numbers.num1_entry_imaginary.insert(0, "0")
        self.complex_numbers.operation_var.set("√")
        self.complex_numbers.calculate()
        self.assertEqual(self.complex_numbers.result_entry_real.get(), "2.0")
        self.assertEqual(self.complex_numbers.result_entry_imaginary.get(), "0.0")

    def tearDown(self):
        # Завершение работы окружения для тестов
        self.root.destroy()  # Уничтожение основного окна Tkinter

if __name__ == '__main__':
    unittest.main()
