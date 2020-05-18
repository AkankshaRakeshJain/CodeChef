for _ in range(int(input())):
    n,k = map(int,input().split())
    a = list(map(float,input().split()))
    x = sorted(a)
    if k != 0:
        x = x[k:-k]
    print(format(sum(x)/len(x),'.6f'))
        
