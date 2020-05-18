def fact(number):
    if number == 1:
        return number
    else:
        return number * fact(number - 1)

user = int(input())
for i in range(0, user):
    factNumber = int(input())
    print(fact(factNumber))


