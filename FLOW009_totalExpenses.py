for _ in range(int(input())):
    quality, price = map(float, input().split())
    total_expenses = quality * price
    if quality > 1000:
        discount = total_expenses * 0.1
        result = total_expenses - discount
        print(format(float(result), '.6f'))
    else:
        print(format(float(total_expenses), '.6f'))
