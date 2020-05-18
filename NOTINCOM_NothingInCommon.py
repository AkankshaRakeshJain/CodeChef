for _ in range(int(input())):
    a, b = map(int, input().split())
    alice = set(map(int, input().split()))
    berta = set(map(int, input().split()))
    print(len(alice.intersection(berta)))


