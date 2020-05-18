user = int(input())

for _ in range(user):
    number = input()
    count = 0
    for values in number:
        if values == '4':
            count += 1
    print(count)
