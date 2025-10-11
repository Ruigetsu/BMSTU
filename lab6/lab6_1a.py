list_of_num = list(map(int,input("Введите элементы списка через пробел: ").split()))
num = int(input("Введите элемент для вставки: "))
indx = int(input("Введите индекс вставки элемента: "))
list_of_num.insert(indx,num)
print(f"Новый список = {list_of_num}")

'''if indx > len(list_of_num) or indx < -len(list_of_num) - 1:
    print("Вы ввели неверный индекс")
elif indx == -1 or indx == len(list_of_num):
    list_of_num.append(num)
    print(list_of_num)
else: 
    list_of_num = list_of_num[:indx] + [num] + list_of_num[indx:]
    print(list_of_num)
'''