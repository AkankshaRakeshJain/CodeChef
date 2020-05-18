for _ in range(int(input())):
    x, y = map(int, input().split())
    z = x+y+1
    while 1:
        count = 0
        for i in range(2, z):
            if z % i == 0:
                count += 1
                break
        if count == 0:
            print(z-(x+y))
            break
        else:
            z += 1
