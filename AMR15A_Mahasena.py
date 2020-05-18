number_of_soldiers = int(input())
a = list(map(int, input().split()))  # number of weapons
x1 = 0
x2 = 0
for i in range(0, len(a)):
    if a[i] % 2 == 0:
        x1 += 1  
    else:
        x2 += 1  
        
if x1 > x2:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
