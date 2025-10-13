list_of_num = list(map(int, input("Введите числа через пробел: ").split()))

flag_to_count = False #Флаг, обозначающий, что идет подсчет последовательности
list_counter = []
max_list_counter = []
for i in range(len(list_of_num)): #Проходимся по каждому числу в списке
    if list_of_num[i] % 2 != 0: #Если число нечетное
        if flag_to_count == False: #Если это первый эл. последовательности
            list_counter.append(list_of_num[i]) 
            flag_to_count = True
        else: #Если до этого уже идет последовательность
            if list_of_num[i-1] * list_of_num[i] < 0: #Если текущее и прошлое число разных знаков
                list_counter.append(list_of_num[i])
            else: #Если знак повторился
                if len(list_counter) > len(max_list_counter): #Если длина последовательности больше чем все предыдущие
                    max_list_counter = list_counter.copy() #Обновляем максимум
                list_counter = [] #Сбрасываем счётчик
                flag_to_count = False #Заканчиваем последовательность
    else: #Если число четное
        if flag_to_count == True: 
            if len(list_counter) > len(max_list_counter):
                max_list_counter = list_counter.copy()
            list_counter = []
            flag_to_count = False
        else: 
            continue
if len(max_list_counter) > 1:
    print(f"Максимальная знакочередующаяся последовательность нечётных чисел: {max_list_counter}")
else: 
    print("В списке нет знакочередующихся нечётных чисел")