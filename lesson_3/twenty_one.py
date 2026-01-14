from random import shuffle
from os import system
from time import sleep
from functools import partial



SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
          'King', 'Ace']
SERIES_LENGTH = 5
WINS_T0_CLINCH_SERIES = (SERIES_LENGTH // 2) + 1
TARGET_NUM = 21 # Setting this value to a large integer would risk an
                # IndexError caused by the deck running out of cards.
DEALER_HITS_UNTIL = TARGET_NUM - 4



def message(text):
    print(f'--> {text}')


def table_display(player_hand, dealer_hand, first_look, player_games_won,
                  dealer_games_won, player_count, dealer_count=None):
    message(f"Current series status: you have {player_games_won} win(s) & "
            f"'The House' has {dealer_games_won}.\n")

    message("Your hand: "
           f"{', '.join([' of '.join(card) for card in player_hand])} "
           f"(total: {player_count})\n")

    if first_look:
        message(f"Dealer's hand: {' of '.join(dealer_hand[1])} "
                f"(total: {full_count_hand([dealer_hand[1]])})\n\n")
    else:
        message("Dealer's hand: "
               f"{', '.join([' of '.join(card) for card in dealer_hand])} "
               f"(total: {dealer_count})\n\n")


def welcome():
    WELCOME_MSG = (f"Welcome to a best of {SERIES_LENGTH} series of our "
                   f"'{TARGET_NUM}' card game!\n")
    GAME_DESCRIPTION_MSG = ('(a stripped-down version of Blackjack, w/out '
                            'splits, double-downs, or other complex plays)'
                            '\n')
    RULES_MSG = ("Cards 2-10 have the value of their identifying number. "
                 "Jacks, Queens, & Kings have a value of 10. For each Ace, "
                 "its value can be designated either 1 or 11 as needed, and "
                 "the value may be changed over the course of a 'hand' "
                 "(game).\n"
                f"--> The objective is to get as close to {TARGET_NUM} "
                 "as possible, without exceeding it (aka 'busting').\n"
                 "--> You will be dealt two cards face up, and the dealer "
                 "will deal themselves one card face down and one face up.\n"
                 "--> Then, you'll take the first turn by observing your "
                 "cards and the dealer's visible card, and electing to 'hit' "
                 "(receive an additional card) or 'stay' (decline additional "
                 "cards). Until you decide to stay or you bust, you may "
                 "continue to hit. If you bust, the dealer wins and the game "
                 "is over, but if you elect to stay, your turn ends and the "
                 "game moves on to the dealer's turn.\n"
                 "--> For the dealer's turn, they must hit up until their "
                f"card value count reaches {DEALER_HITS_UNTIL}, and they must "
                f"stay if their count reaches {DEALER_HITS_UNTIL} or above, "
                 "without busting. If the dealer busts, you win.\n"
                 "--> If both turns have ended in stays, you win if your "
                 "total is higher, the 'house' wins if the dealer's total is "
                 "higher, and it's a 'push' (tie) if the totals are equal.\n"
                f"--> First to win {WINS_T0_CLINCH_SERIES} hands wins the "
                 "series!\n\n")
    DEAL_MSG = "Press the 'Enter' key to initiate dealing"

    system('clear')

    message(WELCOME_MSG)
    message(GAME_DESCRIPTION_MSG)
    message(RULES_MSG)
    message(DEAL_MSG)
    input()

    system('clear')


def initial_count_hand(hand):
    TEN_JACK_QUEEN_KING_VALUE = 10

    count = 0
    ace_number = 0

    for card in hand:
        str_value = card[0]
        if str_value in '23456789':
            count += int(card[0])
        elif str_value in '10JackQueenKing':
            count += TEN_JACK_QUEEN_KING_VALUE
        else:
            ace_number += 1

    return count, ace_number


def full_count_hand(hand):
    ACE_VALUE_11_MODE = 11

    count, ace_number = initial_count_hand(hand)

    for uncounted_aces in range(ace_number, 0, -1):
        if count + ACE_VALUE_11_MODE + uncounted_aces - 1 <= TARGET_NUM:
            count += ACE_VALUE_11_MODE
        else:
            count += uncounted_aces
            break

    return count


def player_turn(player_hand, dealer_hand, deck, player_games_won,
                dealer_games_won):
    BLACKJACK_MSG = (f"You're at {TARGET_NUM}!\n\n"
                     "--> Press 'Enter' to continue to the dealer's turn.")

    STAY_MSG = ("You have opted to 'stay'.\n\n"
                "--> Press 'Enter' to continue to the dealer's turn.")

    while True:
        player_count = full_count_hand(player_hand)
        table_display(player_hand, dealer_hand, True, player_games_won,
                      dealer_games_won, player_count)

        if player_count == TARGET_NUM:
            message(BLACKJACK_MSG)
            input()
            system('clear')
            break
        if player_count > TARGET_NUM:
            system('clear')
            break
        if player_count < TARGET_NUM:
            if player_stay(player_hand, dealer_hand, player_games_won,
                           dealer_games_won, player_count):
                system('clear')
                table_display(player_hand, dealer_hand, True,
                              player_games_won, dealer_games_won, player_count)
                message(STAY_MSG)
                input()
                system('clear')
                break
            deal_card(player_hand, deck)
            system('clear')

    return player_count


def player_stay(player_hand, dealer_hand, player_games_won, dealer_games_won,
                player_count):
    STAY_OR_HIT_MSG = ("Enter 's' (or 'S' or anything beginning with 's'/'S') "
                       "to 'stay'.\n--> "
                       "Enter 'h' (or 'H' or anything beginning with 'h'/'H') "
                       "to 'hit'.")

    partial_table_display = partial(table_display, player_hand, dealer_hand,
                        True, player_games_won, dealer_games_won, player_count)

    return get_valid_input(STAY_OR_HIT_MSG, 's', 'h', partial_table_display)


def get_valid_input(input_msg, true_char, false_char, display=None):
    NO_CHAR_MSG = "No characters entered.\n"

    while True:
        message(input_msg)
        stripped_input = input().strip()

        if not stripped_input:
            system('clear')
            if display:
                display()
            message(NO_CHAR_MSG)
            continue

        first_char_lower = stripped_input[0].lower()

        if first_char_lower == true_char:
            return True
        if first_char_lower == false_char:
            return False

        system('clear')
        if display:
            display()
        message(f'Invalid input: {stripped_input}\n')


def deal_card(hand, deck):        # Both arguments mutated
    hand.append(deck.pop(0))


def initial_deal(player_hand, dealer_hand, deck):
    for _ in range(2):
        deal_card(player_hand, deck)
        deal_card(dealer_hand, deck)


def dealer_turn(dealer_hand, deck):
    count = full_count_hand(dealer_hand)

    while count < DEALER_HITS_UNTIL:
        deal_card(dealer_hand, deck)
        count = full_count_hand(dealer_hand)

    return count


def announce_result(player_count, dealer_count):
    DEALER_BUST_MSG = ('Congratulations!\n\n--> The dealer busted, so you win!'
                       '\n\n')
    PLAYER_BUST_MSG = "Better luck next time!\n\n--> You busted.\n\n"
    PLAYER_GREATER_MSG = ("Congratulations!\n\n--> Your total of "
                         f"{player_count} beats the dealer's {dealer_count}!"
                          "\n\n")
    DEALER_GREATER_MSG = ("Better luck next time!\n\n--> The dealer's total of"
                         f" {dealer_count} beats your {player_count}.\n\n")
    PUSH_MSG = (f"It's a push!\n\n--> Your total of {player_count} "
                f"ties the dealer's {dealer_count}!\n\n")

    if dealer_count > TARGET_NUM:
        return "player wins", DEALER_BUST_MSG

    if player_count > TARGET_NUM:
        return "dealer wins", PLAYER_BUST_MSG

    if player_count > dealer_count:
        return "player wins", PLAYER_GREATER_MSG

    if dealer_count > player_count:
        return "dealer wins", DEALER_GREATER_MSG

    return "tie game", PUSH_MSG


def play_again():
    PLAY_AGAIN_MSG = "Enter 'p' to play again or 'e' to exit."

    play_again_bool = get_valid_input(PLAY_AGAIN_MSG, 'p', 'e')
    system('clear')
    return play_again_bool


def twenty_one_game():
    NEXT_GAME_MSG = "Press 'Enter' to continue to the next game in the series."
    PLAYER_WINS_SERIES_MSG = "Woohoo! You win the series!\n\n"
    HOUSE_WINS_SERIES_MSG = "'The House' wins the series.\n\n"
    GOODBYE_MSG = 'Thanks for playing! So long, farewell!\n'

    welcome()

    while True:
        player_games_won = 0
        dealer_games_won = 0

        while True:
            deck = [(value, suit) for suit in SUITS for value in VALUES]
            shuffle(deck)
            player_hand = []
            dealer_hand = []

            initial_deal(player_hand, dealer_hand, deck)

            player_count = player_turn(player_hand, dealer_hand, deck,
                                       player_games_won, dealer_games_won)

            if player_count <= TARGET_NUM:
                dealer_count = dealer_turn(dealer_hand, deck)
            else:
                dealer_count = full_count_hand([dealer_hand[1]])

            result, result_msg = announce_result(player_count, dealer_count)

            if result == 'player wins':
                player_games_won += 1
            elif result == 'dealer wins':
                dealer_games_won += 1

            if player_count > TARGET_NUM:
                table_display(player_hand, dealer_hand, True, player_games_won,
                              dealer_games_won, player_count, dealer_count)
            else:
                table_display(player_hand, dealer_hand, False,
                              player_games_won, dealer_games_won, player_count,
                              dealer_count)

            message(result_msg)

            if player_games_won == WINS_T0_CLINCH_SERIES:
                sleep(3)
                message(PLAYER_WINS_SERIES_MSG)
                break
            if dealer_games_won == WINS_T0_CLINCH_SERIES:
                sleep(3)
                message(HOUSE_WINS_SERIES_MSG)
                break

            message(NEXT_GAME_MSG)
            input()
            system('clear')

        if not play_again():
            message(GOODBYE_MSG)
            break



twenty_one_game()