def is_palindrome(pal):
    palindromic_string = ''.join(reversed(list(pal)))
    if pal == palindromic_string:
        print(f'słowo {pal} jest palindromem')
    else:
        print(f'słowo {pal} nie jest palindromem')

if __name__ == '__main__':
    word = str(input("Podaj słowo do zbadania\n"))
    is_palindrome(word)