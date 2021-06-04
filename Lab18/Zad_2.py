with open("pantadeusz.txt", "r", encoding="utf-8") as readfile:
    count = -1
    for i, lines in enumerate(readfile):
        count += 1
        if i == 8 or i == 12 or i == 60 or i == 98 or i == 104:
            print(lines)
            count += 1
    print("Ilość wierszy w inwokacji: ", count)