def sum(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum


for _ in range(int(input())):
    d, n = map(int, input().split())
    x = sum(n)
    for i in range(1, d):
        x = sum(x)
    print(x)
