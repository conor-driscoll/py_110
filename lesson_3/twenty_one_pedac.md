1. Initialize deck
    * P:
        * input: DECK nested list (consisting of suit, value tuples)
        * output: deck (copy of DECK)
    * E:
    * D:
    * A:
    * C:
        * deck = DECK.copy()

2. Deal cards to player and dealer
    * P:
        * input: deck (copied and shuffled version of DECK)
        * output: destructively select 2 cards from deck for both the player and the dealer,
        and return them in a nested list format for each participant.
    * E:
    * D:
    * A: 
    * C:

3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.