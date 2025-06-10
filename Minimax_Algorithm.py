def print_board(board):
    
    count=0
    for row in board:
        print("|".join(row))
        if count<len(board)-1:
            print("......")
        count+=1
        
    print()



















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
    
    