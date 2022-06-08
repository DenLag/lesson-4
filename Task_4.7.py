def numbers_range(n):
    for i in range(1,n+1):
        yield i
res = 1
a = numbers_range(int(input('Enter a number')))
for el in a:
    res *= el
print('Result = ',res)
