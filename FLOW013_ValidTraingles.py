for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a+b+c > 180 or a+b+c < 180:
        print('NO')
    else:
        print('YES')

