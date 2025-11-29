from lab12_functions import print_array, input_with_check
from lab12_1 import lab12_1
from lab12_2 import lab12_2
from lab12_3 import lab12_3
from lab12_4 import lab12_4
from lab12_5 import lab12_5
from lab12_6 import lab12_6
from lab12_7 import lab12_7

array = ["  В начале 180600/5/20/*-го года Николай Ростов вернулся",
         "в отпуск. Денисов ехал тоже домой",
         "в Воронеж. Ростов уговорил его ехать с собой до Москвы и остановиться     ",
         "у них в доме. На предпоследней станции, встретив товарища,  ",
         "   Денисов выпил с ним 6/2*2/2*1+1 бутылки вина. Подъезжая к Москве, несмотря на ухабы дороги,он не просыпался,    ",
         "лежа на дне перекладных",
         " саней, подле Ростова. Ростов по мере приближения к Москве       ",
         "      приходил все более и более в нетерпение."]

while True:
    print("") 
    inp = input("Введите номер задания: ")
    print("")
    match inp: 
        case "1": 
            array = lab12_1(array)
            print_array(array)
        
        case "2": 
            array = lab12_2(array)
            print_array(array)
        
        case "3":
            array = lab12_3(array) 
            print_array(array)
        
        case "4": 
            word = input_with_check("Введите слово: ")
            array,count = lab12_4(array,word)
            print_array(array)
            print(f"\nВ списке нашлось {count} слов, содержащих '{word}'.")
        
        case "5": 
            word_to_replace = input_with_check("Введите слово, которое надо заменить: ")
            word = input_with_check("Введите слово, которым надо заменить: ")
            array,count = lab12_5(array,word_to_replace,word)
            print_array(array)
            print(f"\nКоличество замен = {count}")
        
        case "6": 
            array = lab12_6(array)
            print_array(array)
        
        case "7":
            letter = input_with_check("Введите букву: ")
            sentence, array = lab12_7(array,letter) 
            print(sentence,"\n")
            print_array(array)
        
        case "0":
            print("Вы завершили программу!") 
            break
        case _:
            print("Вы ввели неправильный номер задания")