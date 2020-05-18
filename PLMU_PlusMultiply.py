for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i] + a[j] == a[i] * a[j]:
                count += 1
    print(count)

