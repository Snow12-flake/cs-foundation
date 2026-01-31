# Sudoku Solver

## Description
Backtracking algorithm that solves any valid Sudoku puzzle. Finds empty cells, 
tries numbers 1-9, and recursively validates row/column/3x3 box constraints.

## Features
- Complete Sudoku solver (any valid puzzle)
- Row, column, 3x3 subgrid validation
- Backtracking: try/undo numbers systematically
- Prints solved puzzle grid
- Handles edge cases (unsolvable puzzles)

## Technologies Used
- Python recursion and backtracking

## How to Run
```bash
cd week5/"Sudoku Solver"
python sudoku_solver.py
# Enter puzzle → displays solved grid

