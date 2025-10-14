list_of_num = list(map(int,input("Введите элементы списка через пробел: ").split()))
num = int(input("Введите элемент для вставки: "))
indx = int(input("Введите индекс вставки элемента: "))
if indx > len(list_of_num) or indx < -len(list_of_num) - 1: #Если индекс > (длина списка) или < -(длина списка) - 1
    print("Вы ввели неверный индекс")
else: 
    list_of_num.insert(indx,num)
    print(f"Новый список = {list_of_num}")
