num_of_appartament = int(input("Введите номер квартиры: "))
podezd = num_of_appartament // 36 
if podezd > 0: 
    etazh = (num_of_appartament - 36*(podezd))//4 + 1
else: 
    etazh = num_of_appartament//4 + 1
print(f"{podezd+1}, {etazh}")