user = int(input())
for _ in range(0, user):
    lst = []
    number = input()
    for value in number:
        lst.append(int(value))
    print(lst[0] + lst[-1])
