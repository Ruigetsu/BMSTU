def print_db(path):
    with open(path,"r", encoding="utf-8-sig") as file:
        count = 0
        for line in file:
            row = line.strip().split(";")
            if count == 0:
                print(f"{row[0]:^10}|{row[1]:^7}|{row[2]:^4}|{row[3]:^20}")
                print("="*45)
                count += 1
            else:
                print(f"{row[0]:^10}|{row[1]:^7}|{row[2]:^4}|{row[3]:^20}")

