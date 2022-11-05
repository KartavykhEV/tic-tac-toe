size = 3
board = []
# player
cPlayer = 'X'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# print board to screen
def printBoard():
    print('    1   2   3 ')
    for i in range(0, size):
        row = chr(ord('a') + i) + ' |'
        for j in range(0, size):
            row += ' ' + board[i][j] + ' |'
        print(row)

# check if game is done?
def isDone():
    for winner in ['0', 'X']:
        doneD1 = True
        doneD2 = True
        for i in range(0, size):
            doneH = True
            doneV = True
            for j in range(0, size):
                doneH &= board[i][j] == winner
                doneV &= board[j][i] == winner
            if doneH or doneV:
                return winner
            doneD1 &= board[i][i] == winner
            doneD2 &= board[size - i - 1][i] == winner
        if doneD1 or doneD2:
            return winner
    return '-'

# make a next move for player
def makeAMove(player):
    choise = input(f"Enter choise for player {player}: ").lower()
    i = ord(choise[0]) - ord('a')
    j = int(choise[1]) - 1
    if i < 0 or j < 0 or i > 2 or j > 2:
        print(f'{bcolors.FAIL}! WRONG index !{bcolors.ENDC}')
        return player
    if(board[i][j] != ' '):
        print(f'{bcolors.FAIL}! Field {choise} isn\'t empty !{bcolors.ENDC}')
        return player
    board[i][j] = player
    return '0' if player == 'X' else 'X'



# init game board
for i in range(0, size):
    board.append([' '] * size)

# set winner to none
winner = '-'
while winner == '-':  # routine until someone win
    printBoard()
    cPlayer = makeAMove(cPlayer)
    winner = isDone()



# game is done
printBoard() # print result board
print(f'Winner is: {bcolors.OKBLUE}{bcolors.BOLD}{winner}{bcolors.ENDC}') # print winner!
