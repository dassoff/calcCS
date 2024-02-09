###
### TEST
###

import unittest
from calt import BinOctHex

class TestBinOctHex(unittest.TestCase):
    def setUp(self):
        self.calculator = BinOctHex(None)  # Создаем экземпляр класса BinOctHex

    def test_addition_bin(self):
        self.calculator.num1_entry.insert(0, "1010")
        self.calculator.num2_entry.insert(0, "110")
        self.calculator.system_combobox.current(0)  # Выбираем BIN
        self.calculator.operation_combobox.current(0)  # Выбираем операцию сложения
        self.calculator.calculate()
        result = self.calculator.result_entry.get()
        self.assertEqual(result, "10000")

    def test_subtraction_oct(self):
        self.calculator.num1_entry.insert(0, "36")
        self.calculator.num2_entry.insert(0, "15")
        self.calculator.system_combobox.current(1)  # Выбираем OCT
        self.calculator.operation_combobox.current(1)  # Выбираем операцию вычитания
        self.calculator.calculate()
        result = self.calculator.result_entry.get()
        self.assertEqual(result, "21")

    def test_multiplication_hex(self):
        self.calculator.num1_entry.insert(0, "8AB")
        self.calculator.num2_entry.insert(0, "B78")
        self.calculator.system_combobox.current(2)  # Выбираем HEX
        self.calculator.operation_combobox.current(0)  # Выбираем операцию сложения
        self.calculator.calculate()
        result = self.calculator.result_entry.get()
        self.assertEqual(result, "1423")

    def test_division_error(self):
        self.calculator.num1_entry.insert(0, "10101")
        self.calculator.num2_entry.insert(0, "10")
        self.calculator.system_combobox.current(0)  # Выбираем BIN
        self.calculator.operation_combobox.current(3)  # Выбираем операцию деления
        self.calculator.calculate()
        result = self.calculator.result_entry.get()
        self.assertEqual(result, "Ошибка: деление на ноль!")

if __name__ == '__main__':
    unittest.main()
