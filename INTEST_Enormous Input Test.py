loop, divideBy = map(int, input().split())
count = 0
for _ in range(0, loop):
    number = int(input())
    if number % divideBy == 0:
        count += 1
print(count)
