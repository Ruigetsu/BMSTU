import sys
from math import *
from lab11_func import input_num_func, input_int_func, trapezoid_method, median_rectangle_method

def f(x):
    try:
        y = 1/2/x**0.5
        return y
    except ArithmeticError: 
        return False

def func_perv(x): #первообразная функции f(x)
    try:
        y = x**0.5
        return y
    except ArithmeticError: 
        return False

while True:
    start = input_num_func("Введите начало отрезка интегрирования: ")
    end = input_num_func("Введите конец отрезка интегрирования: ")
    if f(start) == False or f(end) == False: 
        print("Метод трапеций нельзя использовать, т.к. функция неопределена на концах отрезка интегрирования, введите начало и конец отрезка заного")
    else: 
        break
N1 = input_int_func("Введите N1: ")
N2 = input_int_func("Введите N2: ")

if func_perv(end) is not False and func_perv(start) is not False:
    true_value = round(func_perv(end) - func_perv(start),4)
else: 
    print("Нельзя вычислить реальное значение интеграла через формулу ньютона-лейбница, т.к. первообразная неопределена в крайних точках отрезка")
    sys.exit()

errors = [] #погрешности 4 измерений

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
            errors.append((abs(val-true_value), abs((val-true_value)/true_value)*100))
        else:
            val = trapezoid_method(f,start,end,N)
            str_to_print += f"{val:^14f}|"
            errors.append((abs(val-true_value), abs((val-true_value)/true_value)*100))
print(str_to_print)

print(f"\nПогрешности\n\
{" "*24}|{"N1":^26}|{"N2":^26}|\n\
{" "*24}|{"Абсолютная":^12}{"Относительная%":13}|{"Абсолютная":^12}{"Относительная%":13}|\n\
{"-"*79}")

indx_of_method = 0
min_val = float("inf")
for i in range(len(errors)): 
    if i == 0:
        if errors[i][0] < min_val: 
            min_val = errors[i][0]
            indx_of_method = i//2

        str_to_print = f"{"Срединные прямоугольники":^24}|{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
    elif i == 2:
        if errors[i][0] < min_val: 
            min_val = errors[i][0]
            indx_of_method = i//2

        print(str_to_print)
        str_to_print = f"{"Трапециями":^24}|{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
    else:
        str_to_print += f"{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
print(str_to_print)

EPS = input_num_func("Введите точность (EPS): ")
N = 1
if indx_of_method == 0: 
    while abs(trapezoid_method(f,start,end,N) - trapezoid_method(f,start,end,2*N)) >= EPS:
        N += 1
    if N > 1:
        print(f"Кол-во необходимых участков разбиения для метода1 = {N}, приближенное значение интеграла при данном N = {trapezoid_method(f,start,end,N)}")
    else: 
        print("Необходимая точность и так достигнута")
else: 
    while abs(median_rectangle_method(f,start,end,N) - median_rectangle_method(f,start,end,2*N)) >= EPS:
        N += 1
    if N > 1:
        print(f"Кол-во необходимых участков разбиения для метода2 = {N}, приближенное значение интеграла при данном N = {median_rectangle_method(f,start,end,N)}")
    else: 
        print("Необходимая точность и так достигнута")