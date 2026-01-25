def print_board(board):
    '''
    Converts 9x9 grid to readable format
    board = [[5,3,0,......], [6,0,0,.....], ....]
    '''
    for row in board:
        print(' '.join(map(str, row)))

# Load puzzle
board = []

# fetch the sudoku board from puzzle.txt
with open ('puzzle.txt') as f:  
    for line in f:
        board.append(list(map(int, line.split()))) 
        '''
        Line from puzzle.txt: "5 3 0 0 7 0 0 0 0"
         ↓ line.split()
        ['5', '3', '0', '0', '7', '0', '0', '0', '0']   ← All STRINGS
         ↓ map(int, ...)
        [5, 3, 0, 0, 7, 0, 0, 0, 0]                    ← Now INTEGERS
        '''
        
print("Unsolved:")
print_board(board)

def is_valid(board, row, col, num):
    '''
    Tests if num can go in board[row][col]
    Checks 3 Sudoku rules: row + column + 3x3 box
    Returns True if OK, False if conflict
    False = Duplicate found
    True = does not contain num
    '''
    # Check row
    for x in range(9):
        if board[row][x] == num:
            return False
    
    # Check column  
    for x in range(9):
        if board[x][col] == num:
            return False
    
    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty(board):
    '''
    Finds first empty cell (0)
    Scans row-by-row, left-to-right
    Returns (row,col) tuple or None if solved
    '''
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) 
    return None  # Solved

def solve(board):
    '''
    1. Find empty cell
    2. Try numbers 1-9
    3. If valid → place + recurse
    4. If recurse succeeds → return True
    5. If fails → undo (backtrack) + try next
    6. No numbers work → return False
    '''
    empty = find_empty(board)
    if not empty:
        return True  # All cells filled
    
    row, col = empty
    
    for num in range(1, 10):  
        if is_valid(board, row, col, num):
            board[row][col] = num  # Place it
            
            if solve(board):  # Recurse to next empty
                return True
            
            board[row][col] = 0  # Undo
    
    return False  # No solution

if __name__ == "__main__":
    '''
    Main execution block
    Loads → prints unsolved → solves → prints solved
    '''
    # Load + print original
    board = []
    with open('puzzle.txt') as f:
        for line in f:
            board.append(list(map(int, line.split())))
    
    print("Unsolved:")
    print_board(board)
    
    solve(board)
    
    print("\nSolved:")
    print_board(board)
