print("Введите номер задания или 0 для выхода:\n\
      Для задания 1a введите: 1a\n\
      Для задания 1b введите: 1b\n\
      Для задания 2a введите: 2a\n\
      Для задания 2b введите: 2b\n\
      Для задания 3 введите : 3\n\
      Для задания 4 введите : 4\n\
      Для задания 5 введите : 5\n\
      Для завершения введите: 0\n")

while True: 
      exercise = input("Введите номер задания: ")
      match exercise:
            case "1a":
                  f = open("lab6_1a.py").read()
                  exec(f)
                  print("\n")
            case "1b":
                  f = open("lab6_1b.py").read()
                  exec(f)
                  print("\n")
            case "2a":
                  f = open("lab6_2a.py").read()
                  exec(f)
                  print("\n")
            case "2b":
                  f = open("lab6_2b.py").read()
                  exec(f)
                  print("\n")
            case "3":
                  f = open("lab6_3.py").read()
                  exec(f)
                  print("\n")
            case "4":
                  f = open("lab6_4_7.py").read()
                  exec(f)
                  print("\n")
            case "5":
                  f = open("lab6_5_2.py").read()
                  exec(f)
                  print("\n")
            case "0":
                  print("Завершение работы")
                  break
            case _:
                  print("Вы ввели неправильное число")