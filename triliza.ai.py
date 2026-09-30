from random import randrange



board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

def check_win():
    # first player
    if board[0] == [player1, player1, player1]:
        print("player1 win")
        return False
    elif board[1] == [player1, player1, player1]:
        print("player1 win")
        return False
    elif board[2] == [player1, player1, player1]:
        print("player1 win")
        return False
    elif board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1:
        print("player1 win")
        return False
    elif board[0][0] == player1 and board[1][0] == player1 and board[2][0] == player1:
        print("player1 win")
        return False
    elif board[0][1] == player1 and board[1][1] == player1 and board[2][1] == player1:
        print("player1 win")
        return False
    elif board[0][2] == player1 and board[1][2] == player1 and board[2][2] == player1:
        print("player1 win")
        return False
    elif board[2][0] == player1 and board[1][1] == player1 and board[0][2] == player1:
        print("player1 win")
        return False
    # second player
    if board[0] == [player2, player2, player2]:
        print("player2 win")
        return False
    elif board[1] == [player2, player2, player2]:
        print("player2 win")
        return False
    elif board[2] == [player2, player2, player2]:
        print("player2 win")
        return False
    elif board[0][0] == player2 and board[1][1] == player2 and board[2][2] == player2:
        print("player2 win")
        return False
    elif board[0][0] == player2 and board[1][0] == player2 and board[2][0] == player2:
        print("player2 win")
        return False
    elif board[0][1] == player2 and board[1][1] == player2 and board[2][1] == player2:
        print("player2 win")
        return False
    elif board[0][2] == player2 and board[1][2] == player2 and board[2][2] == player2:
        print("player2 win")
        return False
    elif board[2][0] == player2 and board[1][1] == player2 and board[0][2] == player2:
        print("player2 win")
        return False
    else:
        return True

def check_cols():
    for j in range(3):
        danger = 0
        open_block = None
        for i in range(3):
            if board[j][i] == player1:
                danger += 1
            elif board[j][i] == " ":
                open_block = i
        if danger == 2 and open_block != None:
            return [j,open_block]
    else:
        return 0

def check_rows():
    for j in range(3):
        danger = 0
        open_block = None
        for i in range(3):
            if board[i][j] == player1:
                danger += 1
            elif board[i][j] == " ":
                open_block = i
        if danger == 2 and open_block != None:
            return [open_block,j]
    else:
        return 0

def check_diag():
    if board[0][0] == player1 and board[1][1] == player1:
        return [2, 2]
    elif board[2][2] == player1 and board[1][1] == player1:
        return [0, 0]
    elif board[0][0] == player1 and board[2][2] == player1:
        return [1, 1]
    elif board[0][2] == player1 and board[1][1] == player1:
        return [2, 0]
    elif board[0][2] == player1 and board[2][0] == player1:
        return [1, 1]
    elif board[1][1] == player1 and board[2][0] == player1:
        return [0, 2]
    else:
        return 0

def check_rows_win():
    for j in range(3):
        danger = 0
        open_block = None
        for i in range(3):
            if board[i][j] == player2:
                danger += 1
            elif board[i][j] == " ":
                open_block = i
        if danger == 2 and open_block != None:
            return [open_block,j]
    else:
        return 0

def check_diag_win():
    if board[0][0] == player2 and board[1][1] == player2:
        return [2, 2]
    elif board[2][2] == player2 and board[1][1] == player2:
        return [0, 0]
    elif board[0][0] == player2 and board[2][2] == player2:
        return [1, 1]
    elif board[0][2] == player2 and board[1][1] == player2:
        return [2, 0]
    elif board[0][2] == player2 and board[2][0] == player2:
        return [1, 1]
    elif board[1][1] == player2 and board[2][0] == player2:
        return [0, 2]
    else:
        return 0

def check_cols_win():
    for j in range(3):
        danger = 0
        open_block = None
        for i in range(3):
            if board[j][i] == player2:
                danger += 1
            elif board[j][i] == " ":
                open_block = i
        if danger == 2 and open_block != None:
            return [j,open_block]
    else:
        return 0

def print_board():
    for i in range(3):
        print("+" + 3 * "-",end="")
    print("+")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} |")
    for i in range(3):
        print("+" + 3 * "-", end="")
    print("+")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} |")
    for i in range(3):
        print("+" + 3 * "-", end="")
    print("+")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} |")
    for i in range(3):
        print("+" + 3 * "-", end="")
    print("+")

def computer_play_easy():
    sq = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                sq.append([i,j])
    return sq[randrange(len(sq))]

def computer_play_medium():
    checked1 = check_rows()
    if checked1 == 0:
        pass
    else:
        return checked1

    checked3 = check_diag()
    if checked3 == 0:
        pass
    else:
        return checked3

    checked2 = check_cols()
    if checked2 == 0:
        sq = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    sq.append([i, j])
        return sq[randrange(len(sq))]
    else:
        return checked2

def computer_play_hard():
    checked1 = check_rows()
    checked5 = check_rows_win()

    if checked5 == 0:
        pass
    else:
        return checked5

    if checked1 == 0:
        pass
    else:
        return checked1

    checked3 = check_diag()
    checked6 = check_diag_win()

    if checked6 == 0:
        pass
    else:
        return checked6

    if checked3 == 0:
        pass
    else:
        return checked3


    checked2 = check_cols()
    checked7 = check_cols_win()
    if checked7 == 0:
        pass
    else:
        return checked7

    if checked2 == 0:
        sq = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    sq.append([i, j])
        return sq[randrange(len(sq))]
    else:
        return checked2

print_board()
level = input("choose difficulty (0-easy, 1-medium, 2-hard): ")
player1 = input("choose player1 (X or O): ")
if player1 == "X":
    player1 = "X"
    player2 = "O"
elif player1 == "O":
    player1 = "O"
    player2 = "X"

def plays():
    # first player
    player1_col = int(input("player1 choose column: "))
    player1_row = int(input("player1 choose row: "))
    while board[player1_col][player1_row] == "X" or board[player1_col][player1_row] == "O":
        print("yparxei hdh ekei")
        player1_col = int(input("player1 choose column: "))
        player1_row = int(input("player1 choose row: "))

    board[player1_col][player1_row] = player1
    print_board()

    if check_win() == False:
        return

    #second play
    if level == "0":
        numbers = computer_play_easy()
        board[numbers[0]][numbers[1]] = player2
    elif level =="1":
        numbers = computer_play_medium()
        if board[numbers[0]][numbers[1]] != " ":
            numbers = computer_play_easy()
            board[numbers[0]][numbers[1]] = player2
        else:
            board[numbers[0]][numbers[1]] = player2
    else:
        numbers = computer_play_hard()
        if board[numbers[0]][numbers[1]] != " ":
            numbers = computer_play_easy()
            board[numbers[0]][numbers[1]] = player2
        else:
            board[numbers[0]][numbers[1]] = player2

    print_board()
    if check_win() == False:
        return


while True:
    plays()
    if check_win() == False:
        break