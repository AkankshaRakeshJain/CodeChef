for _ in range(int(input())):
    x = int(input())
    if x % 10 == 0:
        print('0')
    else:
        x = x*2
        if x % 10 == 0:
            print('1')
        else:
            print('-1')
