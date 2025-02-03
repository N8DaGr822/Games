# Function to print the Tic-Tac-Toe board
def print_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i < 2:
            print('---------')

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full (tie condition)
def is_full(board):
    return all([cell != ' ' for row in board for cell in row])

# Main function to play the game
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get user input for the move
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] != ' ':
                print("Cell already occupied. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        
        # Make the move
        board[row][col] = current_player
        
        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
