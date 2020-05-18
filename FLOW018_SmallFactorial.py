def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num-1)


for i in range(int(input())):
    number = int(input())
    print(fact(number))
