list_of_num = list(map(int,input("Введите целые числа через пробел: ").split()))

print(f"\nНачальынй список: {list_of_num}")

s = 0
n = 0
last_zero = -1
for i in range(len(list_of_num)):
    if list_of_num[i] > 0:
        s += list_of_num[i]
        n += 1
    elif list_of_num[i] == 0: 
        last_zero = i
if last_zero >= 0:
    list_of_num[last_zero] = s/n
    print(f"Ср. арифм. положительных эл. = {s/n:g}, итоговый список: {list_of_num}") 
else:
    print(f"В списке нету нулей и ср. арифм. положительных = {s/n:g}") 

