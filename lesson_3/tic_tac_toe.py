import os
import random

OPEN_SQUARE = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
TURN_ORDER = 'choose' # Set to 'player' or 'computer' for user or computer to
                      # automatically take the 1st turn, and set to 'choose'
                      # (or any other value) to allow the user to choose which
                      # entity goes 1st.
SERIES_LENGTH = 5
NUM_GAMES_TO_WIN = (SERIES_LENGTH // 2) + 1

WELCOME_MSG = ('Welcome to Tic Tac Toe Versus The Computer!\n'
               f'* Best of {SERIES_LENGTH} series\n'
               f'* Your moves will be marked with "{PLAYER_MARKER}" '
               f'and the computer\'s with "{COMPUTER_MARKER}"\n')
GOODBYE_MSG = 'Thanks for playing! So long, farewell!\n'

SQUARE_CODE_ABBREVS = {
    'tl': ('top', 'left'),
    'tc': ('top', 'center'),
    'tr': ('top', 'right'),
    'ml': ('middle', 'left'),
    'mc': ('middle', 'center'),
    'mr': ('middle', 'right'),
    'bl': ('bottom', 'left'),
    'bc': ('bottom', 'center'),
    'br': ('bottom', 'right'),
    }



def message(text):
    print(f'==> {text}')


def who_goes_1st(contestant_1st):
    WHO_1ST_MSG = ('Please enter the number 1 to take the 1st turn, '
                   'or enter 2 if you\'d like the computer to start the game.')

    if contestant_1st == 'player':
        input('Press "Enter" to continue.\n')
        return 'player'

    if contestant_1st == 'computer':
        input('Press "Enter" to continue.\n')
        return 'computer'

    while True:
        message(WHO_1ST_MSG)

        who_1st_input_stripped = input().strip()

        if who_1st_input_stripped:
            input_1st_letter = (who_1st_input_stripped)[0]

            match input_1st_letter:
                case '1':
                    return 'player'
                case '2':
                    return 'computer'

        os.system('clear')
        message(f'Invalid entry: "{who_1st_input_stripped}"\n')


def fill_square(board, square_code):
    return board.setdefault(square_code, OPEN_SQUARE)


def print_horizontal_divider():
    print(f'{5 * '-'}+{5 * '-'}+{5 * '-'}')


def print_single_row_vertical_dividers_and_empty_space():
    print(f'{5 * ' '}|{5 * ' '}|{5 * ' '}')


def display_board(board, player_score, computer_score):
    message("Series Scoreboard (games won)\n"
           f"* your score: {player_score}, "
           f"computer's score: {computer_score}")

    print()
    for row_number in range(1, 12):
        match row_number:
            case 4 | 8:
                print_horizontal_divider()
            case 2:
                print(f'  {fill_square(board, ('top', 'left'))}  '
                      f'|  {fill_square(board, ('top', 'center'))}  '
                      f'|  {fill_square(board, ('top', 'right'))}  ')
            case 6:
                print(f'  {fill_square(board, ('middle', 'left'))}  '
                      f'|  {fill_square(board, ('middle', 'center'))}  '
                      f'|  {fill_square(board, ('middle', 'right'))}  ')
            case 10:
                print(f'  {fill_square(board, ('bottom', 'left'))}  '
                      f'|  {fill_square(board, ('bottom', 'center'))}  '
                      f'|  {fill_square(board, ('bottom', 'right'))}  ')
            case _:
                print_single_row_vertical_dividers_and_empty_space()
    print()


def open_squares(board):
    return [square_code for square_code, value in board.items()
            if value == OPEN_SQUARE]


def join_or(lst, delimiter=',', cnjnctn='or'):
    str_lst = [str(item) for item in lst]

    len_str_lst = len(str_lst)
    last_index = len_str_lst - 1

    match len_str_lst:
        case 1:
            new_lst = str_lst
        case 2:
            new_lst = [str_lst[0], 'or' , str_lst[1]]
        case _:
            new_lst = [item + delimiter if index != last_index
                       else cnjnctn + ' ' + item
                       for index, item in enumerate(str_lst)]

    return ' '.join(new_lst)


def player_choose(board, player_score, computer_score):
    PLAYER_CHOOSE_MSG = ('Using its two-letter abbreviation '
                         '(e.g., "tl" for top-left), '
                         'please choose one of the following open spaces:\n')

    open_squares_lst = open_squares(board)

    if not (len(open_squares_lst) == 0 or is_winner(COMPUTER_MARKER, board)):

        open_squares_formatted = ['-'.join(square_code)
                                  for square_code in open_squares_lst]
        open_squares_str = join_or(open_squares_formatted)

        while True:
            message(PLAYER_CHOOSE_MSG)
            message(f'{open_squares_str}\n')

            square_code_abbrev_raw = input()
            square_code_abbrev = square_code_abbrev_raw.strip().lower()

            if (square_code_abbrev in SQUARE_CODE_ABBREVS and
                  SQUARE_CODE_ABBREVS[square_code_abbrev] in open_squares_lst):
                board[SQUARE_CODE_ABBREVS[square_code_abbrev]] = PLAYER_MARKER
                break

            os.system('clear')
            display_board(board, player_score, computer_score)
            message(f'Invalid input: "{square_code_abbrev_raw}"\n')


def check_winning_move(board, open_moves, marker):
    for move in open_moves:
        board_copy = board.copy()
        board_copy[move] = marker
        if is_winner(marker, board_copy):
            return move
    return False


def computer_choose(board, open_moves):
    offensive_move = check_winning_move(board, open_moves, COMPUTER_MARKER)
    if offensive_move:
        return offensive_move

    defensive_move = check_winning_move(board, open_moves, PLAYER_MARKER)
    if defensive_move:
        return defensive_move

    if board[('middle', 'center')] == OPEN_SQUARE:
        return ('middle', 'center')

    return random.choice(open_moves)


def computer_move(board):
    open_squares_lst = open_squares(board)

    if not (len(open_squares_lst) == 0 or is_winner(PLAYER_MARKER, board)):
        board[computer_choose(board, open_squares_lst)] = COMPUTER_MARKER


def is_winner(marker, board):
    WIN_DIAGONAL_1 = [('top', 'left'), ('middle', 'center'),
                      ('bottom', 'right')]
    WIN_DIAGONAL_2 = [('bottom', 'left'), ('middle', 'center'),
                      ('top', 'right')]
    CONSECUTIVE_ROW_OR_COLUMN_SQUARES_REQ_FOR_WIN = 3

    move_squares = [square_code for square_code, value in board.items()
                    if value == marker]
    move_squares_attributes = [attribute for square_code in move_squares
                                         for attribute in square_code]

    for item in move_squares_attributes:
        if (move_squares_attributes.count(item) ==
                                CONSECUTIVE_ROW_OR_COLUMN_SQUARES_REQ_FOR_WIN):
            return True

    if (all(square_code in move_squares for square_code in WIN_DIAGONAL_1) or
           all(square_code in move_squares for square_code in WIN_DIAGONAL_2)):
        return True

    return False


def game_over_winner(board):
    PLAYER_WINS_MSG = 'You win! Good work!\n'
    COMPUTER_WINS_MSG = 'The computer wins.\n'

    if is_winner(PLAYER_MARKER, board):
        os.system('clear')
        message(PLAYER_WINS_MSG)
        return True

    if is_winner(COMPUTER_MARKER, board):
        os.system('clear')
        message(COMPUTER_WINS_MSG)
        return True

    return False


def game_over_tied(board):
    TIE_MSG = 'Tie game!\n'

    if OPEN_SQUARE not in board.values():
        os.system('clear')
        message(TIE_MSG)
        return True

    return False


def play_again():
    PLAY_AGAIN_MSG = 'Would you like to play again? (y/n)'

    while True:
        message(PLAY_AGAIN_MSG)
        play_again_input_stripped = input().strip()

        if play_again_input_stripped:
            play_again_input = (play_again_input_stripped)[0].lower()
        else:
            play_again_input = play_again_input_stripped

        if play_again_input == 'y':
            os.system('clear')
            return True

        if play_again_input == 'n':
            os.system('clear')
            return False

        os.system('clear')
        message(f'Invalid entry: "{play_again_input_stripped}"\n')


def is_series_winner(score):
    return score == NUM_GAMES_TO_WIN


def execute_move(board, player_score, computer_score, turn_mode):
    match turn_mode:
        case 'player':
            player_choose(board, player_score, computer_score)
            computer_move(board)
        case 'computer':
            computer_move(board)
            os.system('clear')
            display_board(board, player_score, computer_score)
            player_choose(board, player_score, computer_score)


def tic_tac_toe_game():
    os.system('clear')
    message(WELCOME_MSG)
    turn_order_mode = who_goes_1st(TURN_ORDER)

    player_score = 0
    computer_score = 0

    while True:
        board = {}
        os.system('clear')

        while True:
            display_board(board, player_score, computer_score)

            execute_move(board, player_score, computer_score, turn_order_mode)

            if (game_over_winner(board) or game_over_tied(board)):

                if is_winner(PLAYER_MARKER, board):
                    player_score += 1
                if is_winner(COMPUTER_MARKER, board):
                    computer_score += 1

                display_board(board, player_score, computer_score)
                input('Press "Enter" to continue.\n')
                break

            os.system('clear')

        if is_series_winner(player_score):
            message('You win the series '
                   f'{player_score} to {computer_score}! Congrats champ!\n')
        elif is_series_winner(computer_score):
            message('The computer wins the series '
                   f'{computer_score} to {player_score}.\n')
        else:
            continue

        player_score = 0
        computer_score = 0

        if not play_again():
            break

    message(GOODBYE_MSG)



tic_tac_toe_game()