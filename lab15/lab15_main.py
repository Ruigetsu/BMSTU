import os
from lab15_1 import lab15_1
from lab15_2 import lab15_2
from lab15_3 import lab15_3

menu_text = "\n1) Удалить все отрицательные числа\n\
2) После каждого нечетного добавить его удвоенное значение\n\
3) Сортировка методом Шелла\n\
0) Выйти из программы"

def main():      
    while True:
        print(menu_text)
        
        inp = input("\nВведите номер команды: ").strip()
        
        match inp:
            case "1": 
                lab15_1()
            case "2":
                lab15_2()
            case "3": 
                lab15_3()

            case "0":
                print("\nПрограмма завершена")
                break
            
            case _:
                print("Ошибка: некорректная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()