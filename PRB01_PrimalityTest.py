for _ in range(int(input())):
    number = int(input())
    lst = []
    if number <= 1:
        print('no')
    else:
        for i in range(2, number+1):
            if number % i == 0:
                lst.append(i)
                if len(lst) >= 2:
                    print('no')
                    break
        else:
            print('yes')
