for _ in range(int(input())):
    number = input()
    if number == number[::-1]:
        print('wins')
    else:
        print('losses')
