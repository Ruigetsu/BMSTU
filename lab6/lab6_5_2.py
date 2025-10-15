list_of_num = list(map(int, input("Введите числа через пробел: ").split()))
indx_min_positive = 0
indx_max_negative = 0
min_positive = None
max_negative = None
for i in range(len(list_of_num)): 
    if list_of_num[i] > 0:
        if min_positive == None: 
            min_positive = list_of_num[i]
            indx_min_positive = i
        else:
            if list_of_num[i] < min_positive: 
                min_positive = list_of_num[i]
                indx_min_positive = i
    elif list_of_num[i] < 0:
        if max_negative == None: 
            max_negative = list_of_num[i]
            indx_max_negative = i
        else:
            if list_of_num[i] > max_negative:
                max_negative  = list_of_num[i]
                indx_max_negative = i
list_of_num[indx_min_positive], list_of_num[indx_max_negative] = list_of_num[indx_max_negative], list_of_num[indx_min_positive]
print(f"Изменённый список: {list_of_num}")

