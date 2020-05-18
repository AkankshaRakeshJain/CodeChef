for _ in range(int(input())):
    classID = input()
    if classID == 'B' or classID == 'b':
        print('BattleShip')
    elif classID == 'C' or classID == 'c':
        print('Cruiser')
    elif classID == 'D' or classID == 'd':
        print('Destroyer')
    elif classID == 'F' or classID == 'f':
        print('Frigate')

