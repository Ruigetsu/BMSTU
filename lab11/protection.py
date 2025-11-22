#начало и конец, кол-во разбиений 1, площадь и из эталонной отнимаем эту метод 3/8
from math import sin,cos,pi
start = float(input("Введите начало отрезка: "))
end = float(input("Введите конец отрезка: "))
while True:
    N = int(input("Введите кол-во разбиений: "))
    if N % 3 != 0: 
        print("Кол-во разбиений должно быть кратно 3, введите их заного")
    else: 
        break

def f(x): 
    return x**2 - 1

def g(x): 
    return x**3 / 3 - x

true_value = g(end) - g(start)

def metod_3_8(f,start,end,n): 
    step = (end - start)/n
    s = f(start) + f(end)

    for i in range(1,n): 
        x = start + i * step
        if i % 3 == 0: 
            s += 2 * f(x)
        else: 
            s += 3 * f(x)
    
    s *= (3*step/8)
    return s

val = metod_3_8(f,start,end,N)
EPS = 1e-7
if abs(true_value - val) < EPS:
    error = 0
else: 
    error = abs(true_value - val)
print(f"Площадь методом 3/8 при {N} разбиениях = {val}\n\
Разница между эталоном = {error:g}")