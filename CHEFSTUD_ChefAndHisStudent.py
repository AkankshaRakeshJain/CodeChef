for _ in range(int(input())):
    s = input()
    lst = []
    count = 0
    for i in s:
        lst.append(i)
    for i in range(len(lst)):
        if lst[i] == '<':
            lst[i] = '>'
            continue
        elif lst[i] == '>':
            lst[i] = '<'
            continue
    for i in range(len(lst)-1):
        if lst[i] == '>' and lst[i+1] == '<':
            count += 1
    print(count)
