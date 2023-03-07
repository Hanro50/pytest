
# 0 = Blank, 1 = X and 2 = O
import random


board = {
    0:[0,0,0],
    1:[0,0,0],
    2:[0,0,0]
}
# Checks for a win state
def lawyer():
    if (board[0][0]!=0 and (board[0][0]==board[1][1] and board[2][2]==board[1][1])):
            return True
    if (board[0][2]!=0 and (board[0][2]==board[1][1] and board[2][0]==board[1][1])):
            return True
    for x in range(len(board)):
        if (board[x][0]!=0 and (board[x][0]==board[x][1] and board[x][2]==board[x][1])):
            return True
        if (board[0][x]!=0 and (board[0][x]==board[1][x] and board[2][x]==board[1][x])):
            return True
    return False
    



# Paints the board
def paint():
    out = ""
    for y in range(len(board)):
        out+="\n -------------\n | "
        for x in range(len(board[y])):
            match board[y][x]:
                case 0 : out += " "
                case 1 : out += "X"
                case 2 : out += "O"
            out+=" | "
    out+="\n ------------- "
    print(out)


def gameloop():
    cPiece = 1

             

    while (True):
        paint()
        y = 0
        x = 0

        print("Your move "+("X" if cPiece==1 else "O"))
        yStr = input("Please give the y cord: ")
        xStr = input("Please give the x cord: ")
            
        try:
            y = int(yStr)-1
            x = int(xStr)-1
            if x<0 or x>2 or y<0 or y>2: continue
        except: 
            continue
        if board[y][x] != 0 : continue
        board[y][x] = cPiece
        if (lawyer()): 
            paint()
            print("Player "+("X" if cPiece==1 else "O")+" won")
            return
        cPiece = 2 if cPiece==1 else 1
        
        

gameloop()