for _ in range(int(input())):
    lst = []
    for i in range(10):
        n = list(map(int,input().split()))
        count = 0
        lst.append(n)
        for i in lst:
            for j in i:
                if j <= 30:
                    count += 1
    if count >= 60:
        print('yes')
    else:
        print('no')

