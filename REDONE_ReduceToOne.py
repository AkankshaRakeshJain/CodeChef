def product(lst):
    product = 1
    for i in lst:
        product *= i
    return product

for _ in range(int(input())):
    m=10**9+7
    lst = []
    lst1 = []
    summ = 0
    n = int(input())
    for i in range(1,n+1):
        lst.append(i)
    while len(lst)!=1:
        lst1.append(lst.pop(0))
        lst1.append(lst.pop(-1))
        x = sum(lst1)
        y = product(lst1)
        z = (x+y) %m
        lst.append(z)
        lst1 = []
        
    for i in lst:
        print(i)

