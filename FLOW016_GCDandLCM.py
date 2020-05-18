def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    number1, number2 = map(int, input().split())
    set1 = set()
    set2 = set()

    lcm = (number1*number2)//gcd(number1, number2)
    print(gcd(number1, number2), lcm)


