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