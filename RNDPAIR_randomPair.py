for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    fav_outcomes = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] + a[j] > max:
                max = a[i] + a[j]
                fav_outcomes =1
            elif a[i] + a[j] == max:
                fav_outcomes += 1
                
    total_occurences = n*(n-1)//2
    print(fav_outcomes/total_occurences)
