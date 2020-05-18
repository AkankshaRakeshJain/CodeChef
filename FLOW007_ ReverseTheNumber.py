user = int(input())
for _ in range(user):
    number = int(input())
    reverse = 0
    first = 1
    while number > 0:
        first = number % 10
        reverse = reverse*10 + first
        number = number // 10
    number = 0
    print(reverse)
