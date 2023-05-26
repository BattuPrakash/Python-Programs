from collections import Counter
def count_letters_digits_symbols(s):
    chars=0
    digits=0
    symbols=0
    for i in s:
        if i.islower() or i.isupper():
            chars+=1
        elif i.isdigit():
            digits+=1
        else:
            symbols+=1
    print("chars",chars)
    print("digits",digits)
    print("symbols",symbols)
s=input()
count_letters_digits_symbols(s)
