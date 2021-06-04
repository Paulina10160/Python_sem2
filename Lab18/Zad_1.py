with open('pantadeusz.txt', 'r', encoding="utf-8") as readfile:
    for lines in readfile:
        print(lines.rsplit("\n"))