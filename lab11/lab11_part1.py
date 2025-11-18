from math import *
from lab11_func import input_num_func, input_int_func

start = input_num_func("Введите начало отрезка интегрирования: ")
end = input_num_func("Введите конец отрезка интегрирования: ")
N1 = input_int_func("Введите N1: ")
N2 = input_int_func("Введите N2: ")

def f(x):
    return x**2 - 2*x + 1 

def func_perv(x): #первообразная функции f(x)
    return x**3/3 - x**2 + x

true_value = round(func_perv(end) - func_perv(start),4)

def trapezoid_method(start,end,N): 
    s = 0 #Сумма
    step = (end - start)/N #step = delta(x)
    s += (f(start) + f(end))/2
    for i in range(1,N):
        x = start + i*step
        s += f(x)
    return s * step

def median_rectangle_method(start,end,N):
    s = 0
    step = (end - start)/N
    for i in range(N): 
        x = start + i*step 
        s += f(x + step/2)
    return s * step

errors = [] #погрешности 4 измерений

print(f"\n{" "*9}|{"N1":^14}|{"N2":^14}|\n\
{"-"*40}")
for method in range(1,3): 
    if method == 1: 
        str_to_print = f"{"Метод 1":^9}|"
    else:
        str_to_print = f"{"Метод 2":^9}|"
    for N in [N1,N2]: 
        if method == 1:
            val = trapezoid_method(start,end,N)
            str_to_print += f"{val:^14g}|"
            errors.append((abs(val-true_value), abs((val-true_value)/true_value)*100))
        else:
            val = median_rectangle_method(start,end,N)
            str_to_print += f"{val:^14g}|"
            errors.append((abs(val-true_value), abs((val-true_value)/true_value)*100))
    print(str_to_print)

print(f"\nПогрешности\n\
{" "*9}|{"N1":^26}|{"N2":^26}|\n\
{" "*9}|{"Абсолютная":^12}{"Относительная%":13}|{"Абсолютная":^12}{"Относительная%":13}|\n\
{"-"*64}")

indx_of_method = 0
min_val = float("inf")
for i in range(len(errors)): 
    if i == 0:
        if errors[i][0] < min_val: 
            min_val = errors[i][0]
            indx_of_method = i//2

        str_to_print = f"{"Метод 1":^9}|{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
    elif i == 2:
        if errors[i][0] < min_val: 
            min_val = errors[i][0]
            indx_of_method = i//2

        print(str_to_print)
        str_to_print = f"{"Метод 2":^9}|{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
    else:
        str_to_print += f"{errors[i][0]:^13g}{errors[i][1]:^13.3g}|"
print(str_to_print)

EPS = input_num_func("Введите точность (EPS): ")
N = 1
if indx_of_method == 1: 
    while abs(trapezoid_method(start,end,N) - trapezoid_method(start,end,2*N)) >= EPS:
        N += 1
    print(f"Кол-во необходимых участков разбиения для метода1 = {N}, приближенное значение интеграла при данном N = {trapezoid_method(start,end,N)}")
else: 
    while abs(median_rectangle_method(start,end,N) - median_rectangle_method(start,end,2*N)) >= EPS:
        N += 1
    print(f"Кол-во необходимых участков разбиения для метода2 = {N}, приближенное значение интеграла при данном N = {median_rectangle_method(start,end,N)}")