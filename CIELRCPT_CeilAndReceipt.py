
for i in range(int(input())):
    N = int(input())
    if N < 4096:
        print(str(bin(N)).count("1"))
    else:
        print(N//2048 + str(bin(N % 2048)).count("1"))

