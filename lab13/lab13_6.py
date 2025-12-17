from lab13_functions import parse_line

def find_two_fields(path,fields,values):
    with open(path, 'r', encoding="utf-8-sig") as file:
        head = file.readline().strip().split(";")
        count = 0
        for row in file:
            line = parse_line(row.strip())
            values_in_line = [line[fields[0]-1], line[fields[1]-1]]
            if values[0] == values_in_line[0] and values[1] == values_in_line[1]: 
                if count == 0: 
                    print(f"{head[0]:^10}|{head[1]:^7}|{head[2]:^4}|{head[3]:^20}")
                    print("="*45)
                    count +=1
                    print(f"{line[0]:^10}|{line[1]:^7}|{line[2]:^4}|{line[3]:^20}")
                else:
                    print(f"{line[0]:^10}|{line[1]:^7}|{line[2]:^4}|{line[3]:^20}")
        if count == 0: 
            print("Подходящих строк не найдено")