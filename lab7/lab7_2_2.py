list_of_num = list(map(int,input("Введите числа через пробел:").split()))
counter_even = 0
indx_origin_list = len(list_of_num) - 1 #Индекс последнего эл. изначального списка
for i in list_of_num:
    if i % 2 == 0:
        counter_even += 1

list_of_num += [None] * counter_even
indx_new_list = len(list_of_num) - 1 #Последний индекс нового списка (с пустыми элементами)
while indx_origin_list >= 0: #Проходимся по каждому элементу начального списка
    cur_num = list_of_num[indx_origin_list]

    if cur_num % 2 == 0: 
        list_of_num[indx_new_list] = cur_num * 2 
        indx_new_list -= 1
    
    list_of_num[indx_new_list] = cur_num
    indx_new_list -= 1
    indx_origin_list -= 1

print(f'Новый список: {list_of_num}')
