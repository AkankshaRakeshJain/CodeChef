# basic salary< 1500 --> HRA = 10%(basic) --> DA = 90%(basic)
# basic salary>= 1500 --> HRA = 500 --> DA = 98%(basic)
# Gross Salary = Basic Salary + HRA + DA
for _ in range(int(input())):
    salary = int(input())
    if salary < 1500:
        print(salary + (0.1*salary) + (0.9*salary))
    else:
        print(salary + 500 + 0.98*salary)
