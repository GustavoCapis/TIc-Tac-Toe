#Create variables for "X", "O" and " " for blank spaces
X = "X"
O = "O"
VOID = " "

#Create variables for the winner and the 3 streak allignment
validGame = True

#Create a board
board = [VOID] * 9

#Define function to restart the game once it's over
def resetGame():
    global validGame
    global board
    validGame = True
    board = [VOID] * 9

#Define function to check for the winner
def checkWinner(winner):
    global validGame
    if winner:
        validGame = False
        line(50, "*")
        print(f"The winner is: {winner}".upper().center(50))
        line(50, "*")
        printBoard()
        
#Define function to check if its a tie
def checkTie(board):
    global validGame
    tie = not VOID in board
    if tie:
        validGame = False
        line(50, "*")
        print("It's a tie!".upper().center(50))
        line(50, "*")       
    return tie

#Define a function to show the board 
def printBoard():
    print("\n")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i + 1]} | {board[i + 2]} |")
        if i < 6:
            print("+---+---+---+")

#Define function for menu customization
def line(n,char):
    print(n * char)
    
#Define function to show the menu  
def showMenu():
    line(50, "-")
    print("### TIC-TAC-TOE ###".center(50))
    line(50, "-")
    print("Let's play Tic-Tac-Toe! \n".center(50))
    print("1. Start")
    print("2. Rules")
    print("3. Exit")
    line(50, "-")

#Define function to check for the winner 
#Conditions for winning the game
#If the spaces are all filled THE SAME horizontally, vertically or in the diagonal  
def checkBoard():
    winner = None
    
    #Horizontally
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != VOID:
            winner = board[i] #Will show "X" or "O"
            return winner

    #Vertically
    if not winner:
        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] and board[i] != VOID:
                winner = board[i]
                return winner
                    
    #Diagonal
    if not winner:
        if board[0] == board[4] == board[8] and board[0] != VOID:
            winner = board[0]
            return winner
                    
        if board[2] == board[4] == board[6] and board[2] != VOID:
            winner = board[2]
            return winner

#Define a function to avoid marking a spot that's already taken
def validateChoice(choice):
    while choice not in range(1, 10) or board[choice - 1] != VOID:
        print("Choose a valid position!")
        choice = int(input("Now choose a position (1 - 9) to mark 'O': "))
        printBoard()
    return choice
        
        
#Menu
showMenu()

#Interaction with the menu input
option = int(input("First, choose one option: "))

while True: 
#Menu Conditions
    if option == 2:
        line(90, "-")
        print("Tic-Tac-Toe rules".upper().center(90))
        line(90, "-")
        print("""- The game is played on a 3x3 grid.
- Two players take turns: one is X, the other is O.
- Players place their mark in empty spaces.
- The first to get three in a row (horizontally, vertically, or diagonally) wins.
- If all spaces are filled with no winner, the game is a tie.""")
        line(90, "-")
        showMenu()
        option = int(input("First, choose one option: "))
        continue
    
    elif option == 3:
        print("Exiting...")
        break
    
    elif option == 1: 
        resetGame()
        print("This is our board:")
        printBoard()
        print("\n")
        
        while validGame:
            choice = int(input("Now choose a position (1 - 9) to mark 'X': "))
            
            choice = validateChoice(choice)
            
            board[choice - 1] = X
            
            printBoard()
            
            winner = checkBoard()
            
            checkWinner(winner)
            if winner != None:
                break
                    
            #Conditions for tie the game
            #If all the spaces are filled
            if checkTie(board):
                break
                         
            choice = int(input("Now choose a position (1 - 9) to mark 'O': "))
            
            choice = validateChoice(choice)
                
            board[choice - 1] = O
            
            printBoard()
             
            winner = checkBoard()
            
            checkWinner(winner)
            if winner != None:
                break
            
            #Conditions for tie the game
            #If all the spaces are filled
            if checkTie(board):
                break
        
        showMenu()
        option = int(input("First, choose one option: "))

        
    else:
        print("Please, choose a valid option!".upper())
    


