# Method-1
for _ in range(int(input())):
    ap = list(map(int,input().split()))
    total = sum(ap[:-1]) * ap[-1]
    if total > (24*5):
        print('Yes')
    else:
        print('No')


#Method -2

for _ in range(int(input())):
    ap = list(map(int,input().split()))
    count = 0
    p = ap[-1]
    ap.pop(-1)
    for i in ap:
        count += (i*p)
    if count > 120:
        print('Yes')
    else:
        print('No')
