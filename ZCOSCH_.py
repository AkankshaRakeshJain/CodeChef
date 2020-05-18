for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    x = a[:2]

    sum = 0
    for i in x:
        sum += i
    print(sum)
