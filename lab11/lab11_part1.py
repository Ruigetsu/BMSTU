import sys
from math import *
from lab11_func import input_num_func, input_int_func, trapezoid_method, median_rectangle_method

def f(x):
    return x**2

def func_perv(x): #первообразная функции f(x)
    return x**3 / 3

while True:
    start = input_num_func("Введите начало отрезка интегрирования: ")
    end = input_num_func("Введите конец отрезка интегрирования: ")
    if start < end:
        try: 
            f(start)
            f(end)
            break 
        except: 
            print("Метод трапеций нельзя использовать, т.к. функция неопределена на концах отрезка интегрирования, введите начало и конец заного")
    else: 
        print("Конец отрезка должен быть больше начала, введите их заного")
N1 = input_int_func("Введите кол-во участков разбиения N1: ")
N2 = input_int_func("Введите кол-во участков разбиения N2: ")

try:
    true_value = func_perv(end) - func_perv(start)
except (ArithmeticError, ValueError) as e: 
    print("Нельзя вычислить реальное значение интеграла через формулу ньютона-лейбница,\
т.к. первообразная неопределена в крайних точках отрезка", f"\n{e}")
    sys.exit()

errors = [] #погрешности 4 измерений

"""for N in [N1,N2]: 
    if median_rectangle_method(f,start,end,N) is False or trapezoid_method(f,start,end,N) is False:
        print("функция неопределена на отрезке")
        sys.exit()"""

print(f"\n{" "*24}|{"N1":^14}|{"N2":^14}|\n\
{"-"*55}")
for method in range(1,3): 
    if method == 1: 
        str_to_print = f"{"Срединные прямоугольники":^24}|"
    else:
        str_to_print += f"\n{"Трапециями":^24}|"
    for N in [N1,N2]: 
        if method == 1:
            val = median_rectangle_method(f,start,end,N)
            str_to_print += f"{val:^14g}|"
            if true_value != 0:
                errors.append((abs(val-true_value), abs((val-true_value)/true_value)*100))
            else: 
                errors.append((abs(val-true_value), None))
        else:
            val = trapezoid_method(f,start,end,N)
            str_to_print += f"{val:^14f}|"
            if true_value != 0:
                errors.append((abs(val-true_value), abs((val-true_value)/true_value)*100))
            else: 
                errors.append((abs(val-true_value), None))
print(str_to_print)

print(f"\n\nПогрешности\n\
{" "*24}|{"N1":^26}|{"N2":^26}|\n\
{" "*24}|{"Абсолютная":^12}{"Относительная%":13}|{"Абсолютная":^12}{"Относительная%":13}|\n\
{"-"*79}")

indx_of_method = 0
max_error = float("inf")
is_true_val_equal_zero = False
if true_value == 0:
    is_true_val_equal_zero = True
for i in range(len(errors)): 
    if i == 0:
        if errors[i][0] > max_error: 
            max_error = errors[i][0]
            indx_of_method = i//2 + 1
        if not is_true_val_equal_zero:
            str_to_print = f"{"Срединные прямоугольники":^24}|{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
        else: 
            str_to_print = f"{"Срединные прямоугольники":^24}|{errors[i][0]:^13g}{"-":^13}|"
    elif i == 2:
        if errors[i][0] < max_error: 
            max_error = errors[i][0]
            indx_of_method = i//2 + 1

        print(str_to_print)
        if not is_true_val_equal_zero:
            str_to_print = f"{"Трапециями":^24}|{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
        else: 
            str_to_print = f"{"Трапециями":^24}|{errors[i][0]:^13g}{"-":^13}|"
    else:
        if not is_true_val_equal_zero:
            str_to_print += f"{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
        else: 
            str_to_print += f"{errors[i][0]:^13g}{"-":^13}|"
print(str_to_print)

EPS = input_num_func("Введите точность (EPS): ")
N = 1
if indx_of_method == 1: 
    print("Наиболее точный метод - Трапеции") 
    while abs(median_rectangle_method(f,start,end,N) - median_rectangle_method(f,start,end,2*N)) >= EPS:
        N += 1
    print(f"Кол-во необходимых участков разбиения для метода срединных прямоугольников = {N},\
приближенное значение интеграла при данном N = {trapezoid_method(f,start,end,N)}")
else:
    print("Наиболее точный метод - Срединные прямоугольник") 
    while abs(trapezoid_method(f,start,end,N) - trapezoid_method(f,start,end,2*N)) >= EPS:
        N += 1
    print(f"Кол-во необходимых участков разбиения для метода трапеций = {N},\
приближенное значение интеграла при данном N = {median_rectangle_method(f,start,end,N)}")
