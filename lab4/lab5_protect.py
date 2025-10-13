from math import sin
# f(x) = sin(x) - x
first_arg = float(input("Введите начальное значение аргумента: "))
last_arg = float(input("Введите конечное значение аргумента: "))
step = float(input("Введите шаг: "))

y_min = sin(first_arg) - first_arg
y_max = sin(first_arg) - first_arg

x_start = first_arg
x_last = last_arg
while x_start <= x_last: 
    y = sin(x_start) - x_start
    y_min = min(y_min,y)
    y_max = max(y_max,y)
    x_start = round(x_start+step)

width = 100

offset = 5
row_of_ticks = " "*offset

val_per_symbol = (y_max - y_min)/width

pos_min_tick = offset + 1
pos_max_tick = width - len(str(y_max))
row_of_ticks += f'{" "*pos_min_tick}{y_min:^6.2g}'
row_of_ticks += f'{" "*pos_max_tick}{y_max:^6.2g}'

print(row_of_ticks)

pos_zero = 0
if y_min < 0 < y_max: 
    pos_zero = int((0 - y_min)/val_per_symbol)


x = first_arg
x_last = last_arg
for _ in range((x_last-x)//step): 
    y = sin(x) - x
    pos_point = int((y - y_min)//val_per_symbol)
    if pos_zero:
        if pos_point < pos_zero: 
            print(f"{x:^{offset}.2g}|{" "*pos_point}*{" "*(pos_zero-pos_point)}|{" "*(width-pos_zero)}")
        elif pos_point > pos_zero: 
            print(f"{x:^{offset}.2g}|{" "*pos_zero}|{" "*(pos_point-pos_zero)}*{" "*(width-pos_point)}")
        else: 
            print(f"{x:^{offset}.2g}|{" "*pos_point}+{" "*(width-pos_point)}")
    else: 
        print(f"{x:^{offset}.2g}|{" "*pos_point}*{" "*(width-pos_point)}     |")    
