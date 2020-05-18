for _ in range(int(input())):
    number = int(input())
    lst = [100, 50, 10, 5, 2, 1]
    remainder = 0
    for i in range(len(lst)):
        q = number // lst[i]
        if number % lst[i] == 0:
            remainder += q
            break
        else:
            remainder += q
            number = number % lst[i]

    print(remainder)
