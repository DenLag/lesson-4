from collections import Counter

lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
count = Counter(lst)
unique = list(count)
single = [el for el, n in count.items() if n == 1]
print(single)
