#Minesweeper

import random

# Function to initialize the game board
def initialize_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mines = random.sample(range(rows * cols), num_mines)
    
    for mine in mines:
        row = mine // cols
        col = mine % cols
        board[row][col] = 'M'
    
    return board

# Function to calculate the number of adjacent mines for each cell
def calculate_numbers(board):
    rows, cols = len(board), len(board[0])
    numbers_board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'M':
                continue
            count = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0 <= x < rows and 0 <= y < cols and board[x][y] == 'M':
                        count += 1
            numbers_board[i][j] = str(count) if count > 0 else ' '
    
    return numbers_board

# Function to print the board with current guesses
def print_board(board, guesses):
    rows, cols = len(board), len(board[0])
    for i in range(rows):
        row = []
        for j in range(cols):
            if guesses[i][j]:
                row.append(board[i][j])
            else:
                row.append('#')
        print(' '.join(row))
    print()

# Function to reveal a cell
def reveal(board, guesses, numbers_board, row, col):
    if guesses[row][col]:
        return False
    guesses[row][col] = True
    
    if board[row][col] == 'M':
        return False
    
    if numbers_board[row][col] == ' ':
        for x in range(row-1, row+2):
            for y in range(col-1, col+2):
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    reveal(board, guesses, numbers_board, x, y)
    
    return True

# Function to check if the player has won
def check_win(board, guesses):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'M' and not guesses[i][j]:
                return False
    return True

# Main function to play the game
def play_game():
    rows = 5
    cols = 5
    num_mines = 5
    
    board = initialize_board(rows, cols, num_mines)
    numbers_board = calculate_numbers(board)
    guesses = [[False for _ in range(cols)] for _ in range(rows)]
    
    print("Welcome to Minesweeper!")
    
    while True:
        print_board(numbers_board, guesses)
        
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter column (0-4): "))
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print("Invalid input. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter integers.")
            continue
        
        if not reveal(board, guesses, numbers_board, row, col):
            print("Game Over! You hit a mine.")
            print_board(board, guesses)
            break
        
        if check_win(board, guesses):
            print("Congratulations! You've cleared the minefield!")
            break

# Start the game
play_game()
