user, initial = map(float, input().split())
user = int(user)
if user > initial or user % 5 != 0:
    print(initial)
elif user % 5 == 0:
    charges = 0.5
    if (user + charges) < initial:
        print(initial - user - charges)
    else:
        print(initial)
