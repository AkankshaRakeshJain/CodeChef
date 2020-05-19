for _ in range(int(input())):
    add = 0
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in a:
        add += i
    print(add%k)


