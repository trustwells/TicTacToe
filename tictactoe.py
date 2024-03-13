
#Trust Wells

board = [    
            [" ", "1", "|", "2", "|", "3", " "], 
            ["_", "_", "_", "_", "_", "_", "_"], 
            [" ", "4", "|", "5", "|", "6", " "], 
            ["_", "_", "_", "_", "_", "_", "_"], 
            [" ", "7", "|", "8", "|", "9", " "]
        ]

turn = 1

def PrintBoard(board, number=0, symbol=""):

    for i in range(5):
        for j in range(7):

            if board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol
            elif board[i][j] == str(number):
                board[i][j] = symbol

            print(board[i][j], end="")

        print("")

        

# Main function of the game
def PlaceXO(turn):
    count = 0
    if (turn == 1):
        symbol = "X"
        choice = int(input("Enter the spot to place your X:  "))
        turn = 2
    else:
        symbol = "O"
        choice = int(input("Enter the spot to place your O:  "))
        turn = 1
    
    PrintBoard(board, choice, symbol)
    CheckWin(board, symbol)
    
    if CheckWin(board, symbol) == -1:
        print(symbol + "s Win!")
        return
    else:
        for n in range(5):
            for m in range(7):
                if (board[n][m] == "X") or (board[n][m] == "O"):
                    count += 1
                    if count >= 9:
                        print("Draw!")
                        return
        PlaceXO(turn)
    
    
    #Checks for three in a row, and if so ends the game
def CheckWin(board=[], symbol=""):
    #Iterates through in what I thought is a sort of efficient manner... could be very wrong though lol
    for i in range(5):
        if (board[i][1]==symbol) and (board[i][3]==symbol) and (board[i][5]==symbol):
            return -1
    for j in range(7):
        if (board[0][j]==symbol) and (board[2][j]==symbol) and (board[4][j]==symbol):
            return -1
    if (board[0][1]==symbol) and (board[2][3]==symbol) and (board[4][5]==symbol):
        return -1
    if (board[0][5]==symbol) and (board[2][3]==symbol) and (board[4][1]==symbol):
        return -1
    
    



PrintBoard(board)
PlaceXO(turn)