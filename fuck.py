from tkinter import ttk, messagebox
from tkinter import *
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if firstnum == "" and secondnum == ".":
            self.current = "0."
            self.display(self.current)
            return
        try:
            float(secondnum)
            if self.input_value:
                self.current = secondnum
                self.input_value = False
            else:
                if len(self.current) == 0 and secondnum == '.':
                    self.current = "0."
                    self.display(self.current)
                    return


                ####
                elif secondnum == '.' and '.' not in self.current:
                    if firstnum == "" and secondnum == ".":
                        self.current = "0."
                    else:
                        self.current += "."
                    self.display(self.current)
                    return





                else:
                    if self.op == "squared" and float(firstnum) < 0:
                        self.display("Error")
                        return
                    self.current = firstnum + secondnum
            self.display(self.current)
        except ValueError:
            self.display("Error")

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            try:
                self.valid_function()
            except ZeroDivisionError:
                self.display("Error")
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "sub":
            self.total -= self.current
        elif self.op == "multi":
            self.total *= self.current
        elif self.op == "divide":
            if self.current != 0:
                self.total /= self.current
            else:
                self.display("Error")
                return
        elif self.op == "mod":
            if self.current != 0:
                self.total %= self.current
            else:
                self.display("Error")
                return
        elif self.op == "pow":
            self.total **= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(self.current)
        self.input_value = True

    def All_Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(self.current)
        self.input_value = True
        self.total = 0
        self.op = ''

    def mathPM(self):
        try:
            self.result = False
            self.current = -(float(txtDisplay.get()))
            self.display(self.current)
        except ValueError:
            self.display("Error")

    def squared(self):
        self.result = False
        try:
            num = float(txtDisplay.get())
            if num >= 0:
                self.current = math.sqrt(num)
                self.display(self.current)
            else:
                self.display("Error")
        except ValueError:
            self.display("Error")

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        try:
            angle = float(txtDisplay.get())
            if angle % 180 == 90:
                self.display("Error")
            else:
                self.current = math.tan(math.radians(angle))
                self.display(self.current)
        except ValueError:
            self.display("Error")

    def sin(self):
        self.result = False
        try:
            angle = float(txtDisplay.get())
            if angle % 180 == 90:
                self.display("Error")
            else:
                self.current = math.sin(math.radians(angle))
                self.display(self.current)
        except ValueError:
            self.display("Error")

    def factorial(self):
        self.result = False
        try:
            num = int(txtDisplay.get())
            if num < 0:
                self.display("Error")
            else:
                self.current = math.factorial(num)
                self.display(self.current)
        except ValueError:
            self.display("Error")

    def percent(self):
        self.result = False
        try:
            input_value = float(txtDisplay.get())
            self.current = (input_value / 100.0)
            self.display(self.current)
        except ValueError:
            self.display("Error")

    def power(self):
        self.result = False
        try:
            if self.check_sum:
                self.valid_function()
            else:
                self.total = float(txtDisplay.get())
            self.input_value = True
            self.check_sum = True
            self.op = "pow"
            self.result = False
        except ValueError:
            self.display("Error")

    def to_binary(self):
        self.result = False
        try:
            num = int(txtDisplay.get())
            result = bin(num).replace("0b", "")
            self.display(result)
        except ValueError:
            self.display("Error")

    def to_octal(self):
        self.result = False
        try:
            num = int(txtDisplay.get())
            result = oct(num).replace("0o", "")
            self.display(result)
        except ValueError:
            self.display("Error")

    def to_hexadecimal(self):
        self.result = False
        try:
            num = int(txtDisplay.get())
            result = hex(num).replace("0x", "").upper()
            self.display(result)
        except ValueError:
            self.display("Error")

    def delete_last_char(self):
        self.result = False
        current_value = txtDisplay.get()
        if current_value:
            self.current = current_value[:-1]
            self.display(self.current)
        else:
            self.display("Error")

    def add_binary(self, num1, num2):
        try:
            decimal_sum = int(num1, 2) + int(num2, 2)
            binary_sum = bin(decimal_sum).replace("0b", "")
            return binary_sum
        except ValueError:
            return "Error: Invalid binary numbers"


added_value = Calc()

root = Tk()
root.title("Calculator")

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tab for decimal numbers
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Calc')

# Tab for binary/octal/hex numbers
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Binary/Octal/Hex')

# Tab for Complex numbers
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Complex')

tab4 = ttk.Frame(notebook)
notebook.add(tab4, text='Graph')


tab5 = ttk.Frame(notebook)
notebook.add(tab5, text='Matrix')

# Entry widget
txtDisplay = Entry(tab1, font=('Helvetica', 20, 'bold'), bg='black', fg='green', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=1, columnspan=4, pady=1)
txtDisplay.insert(0, "0")


# Number buttons
numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(tab1, width=6, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

btnClear = Button(tab1, text=chr(67), width=6,
                  height=2, bg='powder blue',
                  font=('Helvetica', 20, 'bold')
                  , bd=4, command=added_value.Clear_Entry
                  ).grid(row=1, column=0, pady=1)

btnAllClear = Button(tab1, text=chr(67) + chr(69),
                     width=6, height=2,
                     bg='powder blue',
                     font=('Helvetica', 20, 'bold'),
                     bd=4,
                     command=added_value.All_Clear_Entry
                     ).grid(row=1, column=1, pady=1)

btnsq = Button(tab1, text="\u221A", width=6, height=2,
               bg='powder blue', font=('Helvetica',
                                       20, 'bold'),
               bd=4, command=added_value.squared
               ).grid(row=2, column=5, pady=1)

btnAdd = Button(tab1, text="+", width=6, height=2,
                bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("add")
                ).grid(row=1, column=3, pady=1)

btnSub = Button(tab1, text="-", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("sub")
                ).grid(row=2, column=3, pady=1)

btnMul = Button(tab1, text="x", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("multi")
                ).grid(row=3, column=3, pady=1)

btnDiv = Button(tab1, text="/", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("divide")
                ).grid(row=4, column=3, pady=1)

btnZero = Button(tab1, text="0", width=6,
                 height=2, bg='powder blue', fg='black',
                 font=('Helvetica', 20, 'bold'),
                 bd=4, command=lambda: added_value.numberEnter(0)
                 ).grid(row=5, column=0, pady=1)

btnDot = Button(tab1, text=".", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.numberEnter(".")
                ).grid(row=5, column=1, pady=1)
btnPM = Button(tab1, text=chr(177), width=6,
               height=2, bg='powder blue', font=('Helvetica', 20, 'bold'),
               bd=4, command=added_value.mathPM
               ).grid(row=5, column=2, pady=1)

btnEquals = Button(tab1, text="=", width=6,
                   height=2, bg='powder blue',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.sum_of_total
                   ).grid(row=5, column=3, pady=1)


btnCos = Button(tab1, text="Cos", width=6,
                height=2, bg='powder blue', fg='black',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.cos
                ).grid(row=4, column=4, pady=1)

btntan = Button(tab1, text="tan", width=6,
                height=2, bg='powder blue', fg='black',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.tan
                ).grid(row=5, column=4, pady=1)

btnsin = Button(tab1, text="sin", width=6,
                height=2, bg='powder blue', fg='black',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.sin
                ).grid(row=3, column=4, pady=1)


btnFactorial = Button(tab1, text="!", width=6, height=2,
                     bg='powder blue', font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.factorial
                     ).grid(row=2, column=4, pady=1)

btnPow = Button(tab1, text="^", width=6,
                height=2, bg='powder blue',
                font=('Helvetica', 20, 'bold'),
                bd=4, command=lambda: added_value.operation("pow")
                ).grid(row=1, column=5, pady=1)

btnPercent = Button(tab1, text="%", width=6,
                   height=2, bg='powder blue',
                   font=('Helvetica', 20, 'bold'),
                   bd=4, command=added_value.percent
                   ).grid(row=1, column=4, pady=1)

btnToBinary = Button(tab1, text="2", width=6,
                     height=2, bg='powder blue',
                     font=('Helvetica', 20, 'bold'),
                     bd=4, command=added_value.to_binary
                     ).grid(row=3, column=5, pady=1)

btnToOctal = Button(tab1, text="8", width=6,
                    height=2, bg='powder blue',
                    font=('Helvetica', 20, 'bold'),
                    bd=4, command=added_value.to_octal
                    ).grid(row=4, column=5, pady=1)

btnToHexadecimal = Button(tab1, text="16", width=6,
                          height=2, bg='powder blue',
                          font=('Helvetica', 20, 'bold'),
                          bd=4, command=added_value.to_hexadecimal
                          ).grid(row=5, column=5, pady=1)

btnDel = Button(tab1, text="←", width=6, height=2,
                bg='powder blue', font=('Helvetica', 20, 'bold'),
                bd=4, command=added_value.delete_last_char
                ).grid(row=1, column=2, pady=1)


###################################################################
###################################################################
###################################################################


import tkinter as tk
from tkinter import ttk

class BinOctHex():
    def __init__(self, tab2):

        self.num1_label = ttk.Label(tab2, text="Число 1:")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry = ttk.Entry(tab2)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)

        self.num2_label = ttk.Label(tab2, text="Число 2:")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry = ttk.Entry(tab2)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)

        self.system_label = ttk.Label(tab2, text="Система счисления:")
        self.system_label.grid(row=2, column=0, padx=5, pady=5)
        self.system_var = tk.StringVar()
        self.system_combobox = ttk.Combobox(tab2, textvariable=self.system_var, values=["BIN", "OCT", "HEX"])
        self.system_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.system_combobox.current(0)

        self.operation_label = ttk.Label(tab2, text="Операция:")
        self.operation_label.grid(row=3, column=0, padx=5, pady=5)
        self.operation_var = tk.StringVar()
        self.operation_combobox = ttk.Combobox(tab2, textvariable=self.operation_var, values=["+", "-", "*", "/"])
        self.operation_combobox.grid(row=3, column=1, padx=5, pady=5)
        self.operation_combobox.current(0)

        self.calculate_button = ttk.Button(tab2, text="Посчитать", command=self.calculate)
        self.calculate_button.grid(row=4, columnspan=2, padx=5, pady=5)

        self.result_label = ttk.Label(tab2, text="Результат:")
        self.result_label.grid(row=5, column=0, padx=5, pady=5)
        self.result_entry = ttk.Entry(tab2, state="readonly")
        self.result_entry.grid(row=5, column=1, padx=5, pady=5)

    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        system = self.system_var.get()
        operation = self.operation_var.get()

        try:
            num1_dec = int(num1, 2) if system == "BIN" else int(num1, 8) if system == "OCT" else int(num1, 16)
            num2_dec = int(num2, 2) if system == "BIN" else int(num2, 8) if system == "OCT" else int(num2, 16)

            if operation == "+":
                result = num1_dec + num2_dec
            elif operation == "-":
                result = num1_dec - num2_dec
            elif operation == "*":
                result = num1_dec * num2_dec
            elif operation == "/":
                if num2_dec == 0:
                    result = "Ошибка: деление на ноль!"
                else:
                    result = num1_dec / num2_dec
            else:
                result = "Ошибка: недопустимая операция!"

            # Преобразуем результат в нужную систему счисления
            if system == "BIN":
                result_str = bin(result)[2:]
            elif system == "OCT":
                result_str = oct(result)[2:]
            elif system == "HEX":
                result_str = hex(result)[2:].upper()
            else:
                result_str = str(result)
        except ValueError:
            result_str = "Ошибка: недопустимое значение!"

        self.result_entry.config(state="normal")
        self.result_entry.delete(0, "end")
        self.result_entry.insert(0, result_str)
        self.result_entry.config(state="readonly")


added_value = BinOctHex(tab2)


#pls fix " . " and " , "

#########################################################
#########################################################
#########################################################


import cmath

class ComplexNumbers():
    def __init__(self, tab3):
        self.num1_label = ttk.Label(tab3, text="Число 1 (a + bi):")
        self.num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry_real = ttk.Entry(tab3)
        self.num1_entry_real.grid(row=0, column=1, padx=5, pady=5)
        self.num1_entry_real.insert(0, "0")
        self.num1_entry_real.config(validate="key", validatecommand=(self.num1_entry_real.register(self.validate_input), '%P'))
        self.num1_label_i = ttk.Label(tab3, text="+")
        self.num1_label_i.grid(row=0, column=2, padx=5, pady=5)
        self.num1_entry_imaginary = ttk.Entry(tab3)
        self.num1_entry_imaginary.grid(row=0, column=3, padx=5, pady=5)
        self.num1_entry_imaginary.insert(0, "0")
        self.num1_entry_imaginary.config(validate="key", validatecommand=(self.num1_entry_imaginary.register(self.validate_input), '%P'))
        self.num1_label_i = ttk.Label(tab3, text="i")
        self.num1_label_i.grid(row=0, column=4, padx=5, pady=5)

        self.num2_label = ttk.Label(tab3, text="Число 2 (c + di):")
        self.num2_label.grid(row=1, column=0, padx=5, pady=5)
        self.num2_entry_real = ttk.Entry(tab3)
        self.num2_entry_real.grid(row=1, column=1, padx=5, pady=5)
        self.num2_entry_real.insert(0, "0")
        self.num2_entry_real.config(validate="key", validatecommand=(self.num2_entry_real.register(self.validate_input), '%P'))
        self.num2_label_i = ttk.Label(tab3, text="+")
        self.num2_label_i.grid(row=1, column=2, padx=5, pady=5)
        self.num2_entry_imaginary = ttk.Entry(tab3)
        self.num2_entry_imaginary.grid(row=1, column=3, padx=5, pady=5)
        self.num2_entry_imaginary.insert(0, "0")
        self.num2_entry_imaginary.config(validate="key", validatecommand=(self.num2_entry_imaginary.register(self.validate_input), '%P'))
        self.num2_label_i = ttk.Label(tab3, text="i")
        self.num2_label_i.grid(row=1, column=4, padx=5, pady=5)

        self.operation_label = ttk.Label(tab3, text="Операция:")
        self.operation_label.grid(row=2, column=0, padx=5, pady=5)
        self.operation_var = tk.StringVar()
        self.operation_combobox = ttk.Combobox(tab3, textvariable=self.operation_var, values=["+", "-", "*", "/", "^", "√"], state="readonly")
        self.operation_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.operation_combobox.current(0)

        self.calculate_button = ttk.Button(tab3, text="Посчитать", command=self.calculate)
        self.calculate_button.grid(row=3, columnspan=5, padx=5, pady=5)

        self.result_label = ttk.Label(tab3, text="Результат (x + yi):")
        self.result_label.grid(row=4, column=0, padx=5, pady=5)
        self.result_entry_real = ttk.Entry(tab3, state="readonly",width=40)
        self.result_entry_real.grid(row=4, column=1, padx=5, pady=5)
        self.result_entry_imaginary = ttk.Entry(tab3, state="readonly", width=40)
        self.result_entry_imaginary.grid(row=4, column=3, padx=5, pady=5)
        self.result_entry_imaginary.insert(0, "0")
        self.result_label_i = ttk.Label(tab3, text="i")
        self.result_label_i.grid(row=4, column=4, padx=5, pady=5)

    def calculate(self):
        num1_real_str = self.num1_entry_real.get()
        num1_imaginary_str = self.num1_entry_imaginary.get()
        num2_real_str = self.num2_entry_real.get()
        num2_imaginary_str = self.num2_entry_imaginary.get()
        operation = self.operation_var.get()

        try:
            num1_real = float(num1_real_str)
            num1_imaginary = float(num1_imaginary_str)
            num2_real = float(num2_real_str)
            num2_imaginary = float(num2_imaginary_str)
        except ValueError:
            self.show_error("Ошибка: Недопустимое значение!")
            return

        num1 = complex(num1_real, num1_imaginary)
        num2 = complex(num2_real, num2_imaginary)

        if operation == "√":
            if num1_real > 0 or (num1_real == 0 and num1_imaginary != 0):
                result = cmath.sqrt(num1)
            else:
                self.show_error("Ошибка: Извлечение корня из этого числа невозможно!")
                return
        else:
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    result = "Ошибка: деление на ноль!"
                else:
                    result = num1 / num2
            elif operation == "^":
                result = num1 ** num2
            else:
                self.show_error("Ошибка: Недопустимая операция!")
                return

        if isinstance(result, complex):
            result_real = result.real
            result_imaginary = result.imag
        else:
            result_real = result
            result_imaginary = 0

        self.result_entry_real.config(state="normal")
        self.result_entry_imaginary.config(state="normal")
        self.result_entry_real.delete(0, "end")
        self.result_entry_real.insert(0, result_real)
        self.result_entry_imaginary.delete(0, "end")
        self.result_entry_imaginary.insert(0, result_imaginary)
        self.result_entry_real.config(state="readonly")
        self.result_entry_imaginary.config(state="readonly")

    def show_error(self, message):
        self.result_entry_real.config(state="normal")
        self.result_entry_imaginary.config(state="normal")
        self.result_entry_real.delete(0, "end")
        self.result_entry_imaginary.delete(0, "end")
        self.result_entry_real.insert(0, message)
        self.result_entry_imaginary.insert(0, "")
        self.result_entry_real.config(state="readonly")
        self.result_entry_imaginary.config(state="readonly")

    def validate_input(self, value):
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

added_complex = ComplexNumbers(tab3)

###################################################################
###################################################################
###################################################################

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class GraphingCalculator:
    def __init__(self, tab):
        self.tab = tab

        self.expression_label = ttk.Label(tab, text="Введите функцию для построения графика:")
        self.expression_label.grid(row=0, column=0, padx=5, pady=5)
        self.expression_entry = ttk.Entry(tab, width=50)
        self.expression_entry.grid(row=0, column=1, padx=5, pady=5)

        self.calculate_button = ttk.Button(tab, text="Построить график", command=self.plot_function)
        self.calculate_button.grid(row=1, columnspan=2, padx=5, pady=5)

        self.error_label = ttk.Label(tab, text="", foreground="red")
        self.error_label.grid(row=2, columnspan=2, padx=5, pady=5)

    def plot_function(self):
        expression = self.expression_entry.get()
        x = sp.symbols('x')
        try:
            expression = sp.sympify(expression)
            y = sp.lambdify(x, expression, 'numpy')

            x_vals = np.linspace(-100, 100, 100000)
            y_vals = y(x_vals)

            plt.plot(x_vals, y_vals)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Graph of the function')

            # Установка границ для осей x и y
            plt.xlim(-10, 10)  # Настройка границ для оси x
            plt.ylim(-50, 50)  # Настройка границ для оси y

            plt.axhline(0, color='black', linewidth=2, linestyle='-')  # Горизонтальная линия через 0
            plt.axvline(0, color='black', linewidth=2, linestyle='-')  # Вертикальная линия через 0

            plt.grid(True)
            plt.show()

            self.error_label.config(text="")
        except Exception as e:
            self.error_label.config(text=str(e))

added_graphics = GraphingCalculator(tab4)

import tkinter as tk
from tkinter import ttk

class Matrix:
    def __init__(self, tab):
        self.tab = tab

        # Создание элементов управления
        self.dimension_label = ttk.Label(tab, text="Размерность матрицы:")
        self.dimension_label.grid(row=0, column=0, padx=5, pady=5)
        self.dimension_entry = ttk.Entry(tab)
        self.dimension_entry.grid(row=0, column=1, padx=5, pady=5)

        self.create_matrix_button = ttk.Button(tab, text="Создать матрицы", command=self.create_matrices)
        self.create_matrix_button.grid(row=1, columnspan=2, padx=5, pady=5)

        self.operation_label = ttk.Label(tab, text="Выберите операцию:")
        self.operation_label.grid(row=2, column=0, padx=5, pady=5)
        self.operation_combobox = ttk.Combobox(tab, values=["Сложение", "Вычитание", "Умножение", "Деление"])
        self.operation_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.operation_combobox.current(0)

        self.calculate_button = ttk.Button(tab, text="Подсчитать", command=self.calculate)
        self.calculate_button.grid(row=3, columnspan=2, padx=5, pady=5)

        self.result_label = ttk.Label(tab, text="Результат:")
        self.result_label.grid(row=4, column=0, padx=5, pady=5)
        self.result_text = tk.Text(tab, width=40, height=10)
        self.result_text.grid(row=4, column=1, padx=5, pady=5)

    def create_matrices(self):
        try:
            dimension = int(self.dimension_entry.get())
            self.matrix1 = self.input_matrix("Матрица 1", dimension)
            if self.operation_combobox.get() != "Деление":
                self.matrix2 = self.input_matrix("Матрица 2", dimension)
            elif self.operation_combobox.get() == "Деление":
                self.matrix2 = self.input_divisor_matrix("Делитель", dimension)
        except ValueError:
            self.show_error("Ошибка: Некорректная размерность матрицы!")

    def input_matrix(self, name, dimension):
        matrix = []
        matrix_window = tk.Toplevel(self.tab)
        matrix_window.title(name)
        matrix_window.geometry("300x200")

        for i in range(dimension):
            row = []
            for j in range(dimension):
                entry = ttk.Entry(matrix_window, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row.append(entry)
            matrix.append(row)

        return matrix

    def input_divisor_matrix(self, name, dimension):
        matrix = []
        matrix_window = tk.Toplevel(self.tab)
        matrix_window.title(name)
        matrix_window.geometry("300x200")

        for i in range(dimension):
            row = []
            for j in range(dimension):
                entry = ttk.Entry(matrix_window, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row.append(entry)
            matrix.append(row)

        return matrix

    def calculate(self):
        operation = self.operation_combobox.get()
        if operation == "Сложение":
            result = self.add_matrices()
        elif operation == "Вычитание":
            result = self.subtract_matrices()
        elif operation == "Умножение":
            result = self.multiply_matrices()
        elif operation == "Деление":
            result = self.divide_matrices()
        else:
            self.show_error("Ошибка: Неверная операция!")
            return

        self.display_result(result)

    def add_matrices(self):
        result = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                entry1 = float(self.matrix1[i][j].get())
                entry2 = float(self.matrix2[i][j].get())
                row.append(entry1 + entry2)
            result.append(row)
        return result

    def subtract_matrices(self):
        result = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                entry1 = float(self.matrix1[i][j].get())
                entry2 = float(self.matrix2[i][j].get())
                row.append(entry1 - entry2)
            result.append(row)
        return result

    def multiply_matrices(self):
        result = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix2[0])):
                total = 0
                for k in range(len(self.matrix2)):
                    entry1 = float(self.matrix1[i][k].get())
                    entry2 = float(self.matrix2[k][j].get())
                    total += entry1 * entry2
                row.append(total)
            result.append(row)
        return result

    def divide_matrices(self):
        # Деление матрицы 1 на матрицу 2
        # Предполагается, что матрица 2 не содержит нулевых значений
        result = []
        for i in range(len(self.matrix1)):
            row = []
            for j in range(len(self.matrix1[0])):
                entry1 = float(self.matrix1[i][j].get())
                entry2 = float(self.matrix2[i][j].get())
                row.append(entry1 / entry2)
            result.append(row)
        return result

    def display_result(self, result):
        self.result_text.config(state="normal")
        self.result_text.delete('1.0', tk.END)
        for row in result:
            self.result_text.insert(tk.END, ' '.join(map(str, row)) + '\n')
        self.result_text.config(state="disabled")

    def show_error(self, message):
        # Вывод сообщения об ошибке
        error_window = tk.Toplevel(self.tab)
        error_window.geometry("250x100")
        error_label = ttk.Label(error_window, text=message, foreground="red")
        error_label.pack(padx=10, pady=10)



matrix_calculator = Matrix(tab5)

root.mainloop()
