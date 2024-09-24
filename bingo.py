import random

def generateBoard():
    n=random.sample(range(1,101),25)
    board=[['.','.','.','.','.'] for _ in range(5)] 
    for k in range(5):
        for j in range(5):
            board[k][j]=n[k*5+j]
    return board

def displayBoard(board):
    for i in range(5):
        for j in range(5):
            print(board[i][j],end=" ")
        print("\n")
    return None

def markboard(board,number):
    for i in range(5):
        for j in range(5):
            if number==board[i][j]:
                board[i][j]='x'
    return board
# board=generateBoard()
# displayBoard(board)
# number=34
# markboard(board,number)
    
def getUserNumber():
    try:
        n=int(input("Enter the drawn number:"))
        if 1<=n<101:
            return n
        elif n<0 and  n>100:
            print("Invalid input! please enter an integer between 1 and 100")
        else:
            print("Invalid input! please enter an integer between 1 and 100")
    except:
        print("error in try block")

# displayBoard(markboard(board,getUserNumber()))



def horizlines(board):
    l=[]
    for row in range(5):
        l.append(str(board[row][0])+str(board[row][1])+str(board[row][2])+str(board[row][3])+str(board[row][4]))
    return l
def verticle(board):
    l=[]
    for colomn in range(5):
        l.append(str(board[0][colomn])+str(board[1][colomn])+str(board[2][colomn])+str(board[3][colomn])+str(board[4][colomn]))
    return l
def diagLines(board):
    leftdown=str(board[0][0])+str(board[1][1])+str(board[2][2])+str(board[3][3])+str(board[4][4])
    rightdown=str(board[0][4])+str(board[1][3])+str(board[2][2])+str(board[3][1])+str(board[4][0])
    return[leftdown,rightdown]
def isfull(board):
    for row in range(5):
        for colomn in range(5):
            if board[row][colomn]!='x':
                return False
    return True
def checkwin(board):
    if isfull(board):
        return True
    all=horizlines(board) or verticle(board) or diagLines(board)
    for l in all:
        if l=="xxxxx":
            return True
    return False

def playBingoGame(): 
    print("Welcome the player")
    board=generateBoard()
    displayBoard(board)
    k=0
    while True:
        n= getUserNumber()
        markboard(board,n)
        displayBoard(board)
        if checkwin(board) == True:
            break
        k+=1 
    print("You Won")
    print("number of iterartrions?",k)    
playBingoGame()