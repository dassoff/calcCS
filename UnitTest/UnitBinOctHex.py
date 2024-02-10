import unittest
import tkinter as tk
from tkinter import ttk
from calt import BinOctHex


class TestBinOctHex(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.tab2 = ttk.Frame(self.root)
        self.bin_oct_hex_calculator = BinOctHex(self.tab2)

    def test_addition_bin(self):
        # Тестирование операции сложения в двоичной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "10101")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "10")
        self.bin_oct_hex_calculator.system_combobox.current(0)  # Выбор BIN
        self.bin_oct_hex_calculator.operation_combobox.current(0)  # Выбор операции сложения
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "10111")

    def test_addition_oct(self):
        # Тестирование операции сложения в восьмеричной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "525")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "10")
        self.bin_oct_hex_calculator.system_combobox.current(1)  # Выбор OCT
        self.bin_oct_hex_calculator.operation_combobox.current(0)  # Выбор операции сложения
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "535")

    def test_addition_hex(self):
        # Тестирование операции сложения в шестнадцатеричной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "A1")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "1F")
        self.bin_oct_hex_calculator.system_combobox.current(2)  # Выбор HEX
        self.bin_oct_hex_calculator.operation_combobox.current(0)  # Выбор операции сложения
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "C0")

    def test_subtraction_bin(self):
        # Тестирование операции вычитания в двоичной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "10101")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "10")
        self.bin_oct_hex_calculator.system_combobox.current(0)  # Выбор BIN
        self.bin_oct_hex_calculator.operation_combobox.current(1)  # Выбор операции вычитания
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "10011")

    def test_multiplication_oct(self):
        # Тестирование операции умножения в восьмеричной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "777")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "2")
        self.bin_oct_hex_calculator.system_combobox.current(1)  # Выбор OCT
        self.bin_oct_hex_calculator.operation_combobox.current(2)  # Выбор операции умножения
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "1776")

    def test_division_hex(self):
        # Тестирование операции деления в шестнадцатеричной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "FF")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "10")
        self.bin_oct_hex_calculator.system_combobox.current(2)  # Выбор HEX
        self.bin_oct_hex_calculator.operation_combobox.current(3)  # Выбор операции деления
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "F")

    def test_division_by_zero_oct(self):
        # Тестирование деления на ноль в восьмеричной системе
        self.bin_oct_hex_calculator.num1_entry.insert(0, "111")
        self.bin_oct_hex_calculator.num2_entry.insert(0, "0")
        self.bin_oct_hex_calculator.system_combobox.current(1)  # Выбор OCT
        self.bin_oct_hex_calculator.operation_combobox.current(3)  # Выбор операции деления
        self.bin_oct_hex_calculator.calculate()
        result = self.bin_oct_hex_calculator.result_entry.get()
        self.assertEqual(result, "0")  # Изменено на ожидаемый результат числа 0

    def tearDown(self):
        self.root.destroy()


if __name__ == '__main__':
    unittest.main()
