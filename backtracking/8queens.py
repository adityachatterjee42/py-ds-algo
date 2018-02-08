count = 0
def isSafe(board, row, col):
    for i in range(col):
        if board[row][i]==1:
            return False
    i = row - 1
    j = col - 1
    while(i>=0 and j>=0):
        if board[i][j]==1:
            return False
        i = i - 1
        j = j - 1
    i = row + 1
    j = col + 1
    while(i<len(board) and j<len(board)):
        if board[i][j]==1:
            return False
        i = i + 1
        j = j + 1
    i = row - 1
    j = col + 1
    while(i<len(board) and j<len(board)):
        if board[i][j]==1:
            return False
        i = i - 1
        j = j + 1
    i = row + 1
    j = col - 1
    while(i<len(board) and j<len(board)):
        if board[i][j]==1:
            return False
        i = i + 1
        j = j - 1
    return True

def printSolution(board):
    global count
    count = count + 1
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end='\t')
        print(end='\n')
    print(end='\n')

def nQueen(board, col):
    if col==len(board):
        printSolution(board)
        return True
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col]=1
            nQueen(board, col+1)
            board[i][col]=0
    return False

def driver(n):
    global count
    board = [[0]*n for i in range(n)]
    nQueen(board,0)
    print(count)
            
driver(4)

    
