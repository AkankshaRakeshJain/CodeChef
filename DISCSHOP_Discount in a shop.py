def merge(lst):
    check = [str(i) for i in lst]
    join = ''.join(check)
    return int(join)


for _ in range(int(input())):
    lst,lst1 = [],[]
    n = int(input())
    while n>0:
        lst.insert(0,n%10)
        n //=10
    for i in range(len(lst)):
        x = lst.pop(i) 
        lst1.append(merge(lst))
        lst.insert(i,x)
    
    minimum = min(lst1)
    print(minimum)