for number_of_rows in range(1):
    number_of_rows = int(input())
    lst = []
    for i in range(number_of_rows):
        a = list(map(int, input().split()))
        lst.append(a)
    # print(lst)
    for i in range(number_of_rows-1, 0, -1):
        for j in range(i):
            if lst[i][j] > lst[i][j+1]:
                lst[i-1][j] += + lst[i][j]
            else:
                lst[i-1][j] += lst[i][j+1]
    print(lst[0][0])
