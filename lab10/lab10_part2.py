import time
import sys
from lab10_func import generate_test_data,check

def insertion_sort_with_sentinel(arr):
    n = len(arr)
    
    iterations = 0
    swaps = 0
    
    sentinel = min(arr) - 1  # Барьер, значение гарантированно меньше всех элементов
    arr.insert(0, sentinel)
    
    # Сортируем массив с барьером
    for i in range(2, n + 1):
        iterations += 1
        key = arr[i]
        j = i - 1
        
        while True:
            iterations += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        if j+1 != i: 
            arr[j + 1] = key
            swaps += 1
    arr.pop(0) #Удаляем барьер
    return arr, iterations, swaps

while True:
    N1 = input("Введите размерность N1: ")
    if check(N1) is not False:
        N1 = int(N1)
        break
    else:
        print(f"{N1} не подходящее значение")

while True:
    N2 = input("Введите размерность N2: ")
    if check(N2) is not False:
        N2 = int(N2)
        break
    else:
        print(f"{N2} не подходящее значение")
if N2 < N1:
    print("N2 должен быть больше чем N1")
    sys.exit()
else:
    if N2 - N1 < 9:
        print("Ошибка, N2 должен быть больше N1 хотя бы на 9") 
        sys.exit()

ticks = 10
offset = 5 #Отступ от начала строки для всех засечек
width = 150 - offset 
tick_step = (N2 - N1) / (ticks - 1)
dimension_vals = []
j = 0
while j < ticks:
    tick_value = int(N1 + j * tick_step)
    dimension_vals.append(int(tick_value))
    j += 1

x_ticks_vals = [[],[],[]]
data = generate_test_data(dimension_vals)
for arr_types in range(len(data)):
    for arr in data[arr_types]:
        arr_copy = arr.copy()
        start = time.time()
        insertion_sort_with_sentinel(arr_copy)
        end = time.time()
        x_ticks_vals[arr_types].append(end-start)
max_time = x_ticks_vals[-1][-1]

ticks = 8
val_per_symbl = (max_time) / width #какое значение соответствует одному символу
tick_step = (max_time) / (ticks - 1) #шаг засечек
tick_positions = [] #позиция засечек
tick_labels = [] #значение засечек
ticks_vals = []
j = 0
pos = 0
while j < ticks:
    tick_value = j * tick_step
    pos = int(round((tick_value) / val_per_symbl)) #Получаем позицию засечки от 0 до 100
    if j > 0 and tick_value * float(tick_labels[-1]) < 0: #добавляем значение засечки для 0, j > 0, чтобы сначала добавилась первая засечка
        tick_labels.append("0")
    tick_positions.append(pos)
    tick_labels.append(f"{tick_value:1f}")
    j += 1

pairs = tuple(zip(tick_positions, tick_labels)) #Кортеж вида: (позиция засечки,наименование засечки)

#Вывод линейки засечек
offset = 5 #Отступ от начала строки для всех засечек

line = [" "] * (width + offset) #Создание пустой линии

for k in range(len(tick_positions)):
    pos = tick_positions[k] + offset #Определение позиции засечки + отступ от начала строки
    label = tick_labels[k] #"Название" засечки
    start = pos
    if start + len(label) > len(line): #Вывод последней засечки
        start = len(line) - len(label)
    for c in range(len(label)): #Заполняем нужное место строки символами числа
        line[start + c] = label[c]
print("".join(line)) #Вывод засечек


#Построение графика
for i in range(len(x_ticks_vals[0])):
    row = [" "] * (width + offset)
    for j in range(len(x_ticks_vals)):
        y = x_ticks_vals[j][i]
        pos = int(round((y) / val_per_symbl)) #Позиция звездочки
        
        if j == 0:
            row[pos] = "*" #sorted
        elif j == 1:
            row[pos] = "-" #random
        else:
            row[pos] = "+" #reversed


    print(f"{dimension_vals[i]}| {''.join(row)}")