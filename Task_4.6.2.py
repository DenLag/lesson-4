from itertools import cycle

ls = input('Enter the elements whith space:')
i = 0
for el in cycle(ls):
    if i > 15:
        break
    else:
        print(el, end='')
    i += 1
