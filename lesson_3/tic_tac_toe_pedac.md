* Display the initial empty 3x3 board.
* Ask the user to mark a square.
* Computer marks a square.
* Display the updated board state.
* If it's a winning board, display the winner.
* If the board is full, display tie.
* If neither player won and the board is not full, go to #2
* Play again?
* If yes, go to #1
* Goodbye!


* Computer "AI" PEDAC:

* def check_winning_move(board):
* Problem:
    * input: board
    * output: computer_choice or False
    * explicit: winning move must be a tuple representing an open square, which, when marked by the computer, completes a full row,column, or diagonal
    * approach: if there is a move which would make is_winner function return True, return that move, else return False 
* Examples:
* Data structure:
* Algorithm:
* def check_winning_move(board):
*   1. for move in open_squares:
*       1. board_copy = copy(board)
*       2. board_copy[move] = COMPUTER_MARKER
*       3. if is_winner(board_copy, COMPUTER_MARKER):
            1. return move
*   2. return False
* Code:            
*       

