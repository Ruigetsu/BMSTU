from math import sin
from lab11_func import trapezoid_method, input_num_func

def f(x): 
    return -x**2 + 7

def g(x): 
    return x**2 - 1

def y(x): 
    return abs(f(x) - g(x))

interval = [-20,20]

def find_zeros(f, iterations = 100):    
    global interval
    step = 2
    epsilon = 1e-7

    def bisection(f, a, b, epsilon, iterations):
        if f(a) * f(b) > 0:
            return None
            
        for _ in range(iterations):
            c = (a + b) / 2
            if abs(f(c)) < epsilon:
                return c
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
        return (a + b) / 2
    
    a, b = interval
    zeros = []
    x = a
    
    while x < b:
        if f(x) * f(x + step) <= 0: 
            zero = bisection(f, x, x + step, epsilon, iterations)
            if zero is not None and abs(f(zero)) < 1e-5:
                is_duplicate = False
                for existing_zero in zeros:
                    if abs(zero - existing_zero) < 1e-6:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    zeros.append(round(zero,5))
        x += step
    
    if len(zeros) < 2: 
        return False
    else: 
        return zeros

EPS = input_num_func("Введите точность (EPS): ")
all_zeros = find_zeros(y)
count = 0
if all_zeros:  
    for i in range(len(all_zeros) - 1):
        start = all_zeros[i]
        end = all_zeros[i+1]
        N1 = 1
        while abs(trapezoid_method(f,start,end,N1) - trapezoid_method(f,start,end,2*N1)) >= EPS:
            N1 += 1
        N2 = 1
        while abs(trapezoid_method(g,start,end,N2) - trapezoid_method(g,start,end,2*N2)) >= EPS:
            N2 += 1
        s1 = trapezoid_method(f,start,end,N1)
        s2 = trapezoid_method(g,start,end,N2)
        count += 1
        print(f"Площадь образованной графиками замкнутой фигуры №{count} = {abs(s1-s2)}")
    
    x_start, x_end = [-5,5] #интервал для вывода графика
    steps = 40  # Количество точек (строк) по вертикали
    step_val = (x_end - x_start) / steps

    x_ticks_vals = []
    y1_vals = []
    y2_vals = []


    current_x = x_start
    for _ in range(steps + 1):
        x_ticks_vals.append(current_x)
        y1_vals.append(f(current_x))
        y2_vals.append(g(current_x))
        current_x += step_val

    all_y = y1_vals + y2_vals
    min_y2 = min(all_y)
    max_y2 = max(all_y)
    ticks = 10 #засечки
    offset = 5 
    width = 100 - offset 
    val_per_symbl = (max_y2 - min_y2) / width 
    tick_step = (max_y2 - min_y2) / (ticks - 1) 
    tick_positions = [] 
    tick_labels = [] 
    j = 0
    pos = 0

    while j < ticks:
        tick_value = min_y2 + j * tick_step
        pos = int(round((tick_value - min_y2) / val_per_symbl))
        if pos >= width + offset: 
            pos = width + offset - 1
            
        if j > 0 and tick_labels and tick_value * float(tick_labels[-1]) < 0: 
            pos0 = int(round((0 - min_y2) / val_per_symbl))
            if 0 <= pos0 < width + offset:
                tick_positions.append(pos0)
                tick_labels.append("0")
                
        tick_positions.append(pos)
        tick_labels.append(f"{tick_value:.1f}")
        j += 1

    pairs = tuple(zip(tick_positions, tick_labels)) 

    line = [" "] * (width + offset) 

    for k in range(len(tick_positions)):
        if tick_labels[k] != "0":
            pos = tick_positions[k] + offset 
            label = tick_labels[k] 
            start = pos
            if start + len(label) > len(line): 
                start = len(line) - len(label)
            for c in range(len(label)): 
                if start + c < len(line):
                    line[start + c] = label[c]
        else: 
            continue

    print(" "*(offset-1) + "".join(line))

    for i in range(len(x_ticks_vals)):
        x = x_ticks_vals[i]
        val1 = y1_vals[i]
        val2 = y2_vals[i]

        pos1 = int(round((val1 - min_y2) / val_per_symbl))
        pos2 = int(round((val2 - min_y2) / val_per_symbl))
        row = [" "] * (width + offset)

        for t in pairs:
            p = t[0] 
            if t[1] == "0" and 0 <= p < len(row):
                row[p] = "|"
        if pos1 == pos0:
            row[pos1] = "-"
        else: 
            row[pos1] = "*"
        if pos2 == pos0:
            row[pos2] = "-"
        else: 
            if row[pos2] == "*": #если совпадают
                row[pos2] = "@" 
            else:
                row[pos2] = "+"

        print(f"{x:5.1f} | {''.join(row)}")

else: 
    print("У функций меньше 2 точек пересечения") 
