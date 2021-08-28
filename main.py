player1 = [1, 1]
player2 = [1, 1]
count = 0
def attack(h1, h2, player1, player2):

    if h1 == 'L':
        if h2 == 'L':
            player2[0] += player1[0]
        else:
            player2[1] += player1[0]
    elif h1 == 'R':
        if h2 == 'L':
            player2[0] += player1[1]
        else:
            player2[1] += player1[1]
def attack1(h1, h2, player1, player2):
    if h1 == 'L':
        if player1[0] != 0:
            if h2 == 'R':
                player2[1] += player1[0]
            else:
                player2[0] += player1[0]
    elif h1 == 'R':
        if player1[1] != 0:
            if h2 == 'L':
                player2[0] += player1[1]
            else:
                player2[1] += player1[1]

    elif player1[0] == 0 and player1[1] == 0:
        return
def sp(hand, x, y):

    if hand[0]+hand[1] == x+y:
        hand[0] = x
        hand[1] = y
    else:
        print("Invalid Move")
while(True):
    print("Enter move for the "+"Player"+str(count+1))
    move = input()
    if move == "A":
        A1, A2 = input("Enter Move Combination ").split()
        if player1[0]*player1[1]*player2[0]*player2[1] != 0:

            if count == 0:
                attack(A1, A2, player1, player2)
            else:
                attack(A1, A2, player2, player1)
        else:
            if count == 0:
                attack1(A1, A2, player1, player2)
            else:
                attack1(A1, A2, player2, player1)
    elif move == 'S':
        key, x, y = input("Enter the split Combination ").split()
        if count == 0:
            sp(player1, int(x), int(y))
        else:
            sp(player2, int(x), int(y))
    if player1[0] >= 5:
        player1[0] = 0
    if player1[1] >= 5:
        player1[1] = 0
    if player2[0] >= 5:
        player2[0] = 0
    if player2[1] >= 5:
        player2[1] = 0
    print("Current Status")
    print("Player:1 " +str(player1), "Player:2 "+ str(player2))
    if player1[0]==0 and player1[1]==0:
        print("Player 2 won")
        break
    elif player2[0]==0 and player2[1]==0:
        print("Player 1 won")
        break
    count = 1-count