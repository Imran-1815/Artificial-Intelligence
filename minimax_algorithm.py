def print_board(board):
    
    count=0
    for row in board:
        print("|".join(row))
        if count<len(board)-1:
            print("......")
        count+=1
        
    print()
def is_winner(board,player):
    for i in range(3):
        if all(board[i][j]==player for j in range(3)) or all(board[j][i]==player for j in range(3)):
            return True
    
    if all(board[i][i]==player for i in range(3)) or all(board[i][2-i]==player for i in range(3)):
        return True
    
    return False

def is_full(board):
    for row in board:
        for cell in row:
            if cell==" ":
                return False
    
    return True

def Minimax(board,depth,is_maximizing):
    if is_winner(board,"X"):
        return 1
    
    if is_winner(board,"0"):
        return -1
    
    if is_full(board):
        return 0
    
    if is_maximizing:
        best_score=-float('inf')
        
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="X"
                    
                    score=Minimax(board,depth+1,False)
                    
                    board[i][j]=' '
                    best_score=max(score,best_score)
        return best_score
    
    else:
        best_score=float('inf')
        
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="0"
                    
                    score=Minimax(board,depth+1,True)
                    
                    board[i][j]=' '
                    best_score=min(score,best_score)
        return best_score



def best_move(board):
    best_score=-float('inf')
    move=None
    
    for i in range(3):
        for j in range(3):
            if board[i][j]==" ":
                board[i][j]="X"
                score=Minimax(board,0,False)
                board[i][j]=" "
                
                if score>best_score:
                    best_score=score
                    move=(i,j)
    
    return move





board=[[" "," "," " ],
       [" "," "," " ],
       [" "," "," " ]]

print_board(board)

while True:
    # human move
    row=int(input("enter between 0-2"))
    col=int(input("enter between 0-2"))
    
    if board[row][col]!=" ":
        print("cell not emplty. retry")
        continue
    board[row][col]="0"
    
    if is_winner(board,"0"):
        print_board(board)
        print('you win')
        break
    
    if is_full(board):
        print_board(board)
        print("Draw")
        break
    
    #Ai_move
    
    ai_move=best_move(board)
    board[ai_move[0]][ai_move[1]]="X"
    
    print("Ai played")
    print_board(board)
    
    if is_winner(board,"X"):
        print("Ai wins")
        break
    
    if is_full(board):
        print(" the game is draw")
        
        break




















    
    