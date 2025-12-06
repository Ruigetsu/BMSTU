import os

def print_db(path):
    with open(path,"r", encoding="utf-8-sig") as file:
        count = 0
        for line in file:
            row = line.strip().split(";")
            if count == 0:
                print(f"{" ":^5}|{row[0]:^10}|{row[1]:^7}|{row[2]:^4}|{row[3]:^20}")
                print("-"*50)
                count += 1
            else:
                print(f"{count:^4})|{row[0]:^10}|{row[1]:^7}|{row[2]:^4}|{row[3]:^20}")
                count += 1
