
number_of_rounds = int(input())
value1 = 0
value2 = 0
lst = []
for _ in range(number_of_rounds):
    player1, player2 = map(int, input().split())
    value1 += player1
    value2 += player2
    lst.append(value1-value2)

if max(lst) > -min(lst):
    print(f"1 {max(lst)}")
else:
    print(f"2 {-min(lst)}")
