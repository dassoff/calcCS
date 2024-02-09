import unittest
import tkinter as tk
from tkinter import ttk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from calt import GraphingCalculator

class TestGraphingCalculator(unittest.TestCase):

    def setUp(self):
        # Настройка окружения для тестов
        self.root = tk.Tk()  # Создание основного окна Tkinter
        self.tab = ttk.Frame(self.root)  # Создание вкладки для виджетов
        self.graphing_calculator = GraphingCalculator(self.tab)  # Создание экземпляра класса GraphingCalculator

    def test_plot_valid_function(self):
        # Тестирование построения графика для правильной функции
        self.graphing_calculator.expression_entry.delete(0, tk.END)  # Очистка поля ввода функции
        self.graphing_calculator.expression_entry.insert(0, "x**2")  # Ввод правильной функции x^2
        self.graphing_calculator.plot_function()  # Построение графика
        # Ожидается, что нет ошибок и график успешно построен

    def test_plot_invalid_function(self):
        # Тестирование построения графика для неправильной функции
        self.graphing_calculator.expression_entry.delete(0, tk.END)  # Очистка поля ввода функции
        self.graphing_calculator.expression_entry.insert(0, "x**")  # Ввод неправильной функции x^
        self.graphing_calculator.plot_function()  # Построение графика
        # Ожидается, что будет выведена ошибка

    def test_plot_empty_function(self):
        # Тестирование построения графика для пустой функции
        self.graphing_calculator.expression_entry.delete(0, tk.END)  # Очистка поля ввода функции
        self.graphing_calculator.plot_function()  # Построение графика
        # Ожидается, что будет выведена ошибка

    def test_plot_unknown_function(self):
        # Тестирование построения графика для неизвестной функции
        self.graphing_calculator.expression_entry.delete(0, tk.END)  # Очистка поля ввода функции
        self.graphing_calculator.expression_entry.insert(0, "log(x)")  # Ввод неизвестной функции log(x)
        self.graphing_calculator.plot_function()  # Построение графика
        # Ожидается, что будет выведена ошибка

    def tearDown(self):
        # Завершение работы окружения для тестов
        self.root.destroy()  # Уничтожение основного окна Tkinter

if __name__ == '__main__':
    unittest.main()
