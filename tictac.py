'''The main tictactoe doc'''
# 0 = Blank, 1 = X and 2 = O
board = {
    0: [0, 0, 0],
    1: [0, 0, 0],
    2: [0, 0, 0]
}


def lawyer():
    '''Checks for a win state'''
    if (board[0][0] != 0 and (board[0][0] == board[1][1] and board[2][2] == board[1][1])):
        return True
    if (board[0][2] != 0 and (board[0][2] == board[1][1] and board[2][0] == board[1][1])):
        return True
    for i_en in enumerate(board):
        i_num = i_en[0]
        if (board[i_num][0] != 0 and (board[i_num][0] == board[i_num][1] and board[i_num][2] == board[i_num][1])):
            return True
        if (board[0][i_num] != 0 and (board[0][i_num] == board[1][i_num] and board[2][i_num] == board[1][i_num])):
            return True
    return False


def paint():
    '''Paints the board'''
    out = ""
    for y_en in enumerate(board):
        y_num = y_en[0]
        out += "\n -------------\n | "
        for x_en in enumerate(board[y_num]):
            x_num = y_en[0]
            match board[y_num][x_num]:
                case 0: out += " "
                case 1: out += "X"
                case 2: out += "O"
            out += " | "
    out += "\n ------------- "
    print(out)


def gameloop():
    '''The main game loop'''
    c_piece = 1

    while True:
        paint()
        y_num = 0
        x_num = 0

        print("Your move "+("X" if c_piece == 1 else "O"))
        y_str = input("Please give the y cord: ")
        x_str = input("Please give the x cord: ")

        try:
            y_num = int(y_str)-1
            x_num = int(x_str)-1
            if x_num < 0 or x_num > 2 or y_num < 0 or y_num > 2:
                continue
        except TypeError:
            continue
        if board[y_num][x_num] != 0:
            continue
        board[y_num][x_num] = c_piece
        if lawyer():
            paint()
            print("Player "+("X" if c_piece == 1 else "O")+" won")
            return
        c_piece = 2 if c_piece == 1 else 1


gameloop()
