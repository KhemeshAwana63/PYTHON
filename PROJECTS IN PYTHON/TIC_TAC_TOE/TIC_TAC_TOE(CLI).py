def TicTacToe():
    board = [" "]*9


    #this fills up the value according to what is their in the index of board list
    def print_board(board):
        print(f'{board[0]} | {board[1]} | {board[2]}')
        print("----------")
        print(f'{board[3]} | {board[4]} | {board[5]}')
        print("----------")
        print(f'{board[6]} | {board[7]} | {board[8]}')

    #now we are going to deal with win cases
    def determining_winner(board):
        win_cases = [(0,1,2),(3,4,5),(6,7,8),  #row cases
                    (0,3,6),(1,4,7),(2,5,8),
                    (2,4,6),(0,4,8)]  #column cases
        for a , b , c in win_cases:
            if board[a] == board[b] == board[c] and board[a] != " ":
                return board[a]   #will  return X or O depending upon what is their
        return None


    #now we are going to see the main function that will deal with all these functions and run the game
    turn = 0
    while True:
        print_board(board)
        player = 'X' if turn%2 == 0 else 'O'
        try:
            move = int(input(f'player {player} choose a position between (1 to 9)')) - 1
            if board[move] != " " or move not in range(9):
                print("invalid number")
                continue
            board[move] = player
            winner = determining_winner(board)  #can return none , X ,O

            if winner:   #this is going to be checked if does not return none
                print_board(board)
                print(f'player {winner} has won')
                break
            if " " not in board:    #if the match is drawn
                print("match drawn")
                break
            turn += 1
        
        except:
            print("invalid input plz try again")