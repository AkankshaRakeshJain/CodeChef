for _ in range(int(input())):
    char = input()
    if len(char) == 1:
        print('YES')
    else:
        lv = char[1:] + char[0]                 # L(V)
        rv = char[-1:] + char[0:len(char)-1]    # R(V)
        if lv == rv:
            print('YES')
        else:
            print('NO')
