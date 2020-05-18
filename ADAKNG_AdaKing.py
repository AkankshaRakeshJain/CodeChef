# Cells that king can visit will form a square/rectangle 

for _ in range(int(input())):
    r,c,k = map(int,input().split())
    #x --> horizontal and y --> vertical
    x = min(c+k,8) - max(c-k,1) + 1  # +1 is row/column the king is standing
    y = min(r+k,8) - max (r-k,1) +1  
    print(x*y)   #area