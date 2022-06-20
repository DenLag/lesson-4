from itertools import count

begin = int(input('Enter a number for begin:'))
for el in count(begin):
    if el > 15:
        break
    else:
        print(el, end=' ')
