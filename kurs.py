import os
import random
import time


# TODO Add Poker game


# Main menu to select game
def main_menu(wallet):
    clear_console()
    print("----[Welcome to Casino 7bet]----")
    print("----[Select your game]----\n")

    print("[1] Roulette     [2] Blackjack     [3] Slots")
    print("[4] Deposit money     [5] Withdraw money")
    print("[6] Exit\n")

    print("Wallet: ", wallet, " coins")
    game = int(input("\nPlease select your game: "))

    if game == 1:
        roulette_f(wallet)
    elif game == 2:
        blackjack_f(wallet)
    elif game == 3:
        SlotsF(wallet)
    elif game == 4:
        deposit_funds(wallet)
    elif game == 5:
        withdraw_funds(wallet)
    elif game == 6:
        exit()


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def show_wallet(wallet):
    print("\nWallet: ", wallet, " coins ", "\n")


def show_tip():
    print("\n----[Useful Tip]----")
    print("\nTo go back to the main menu at any given time, press the right shift key.")


def bet_check(wallet, bet):
    if bet == 0:
        main_menu(wallet)

    if wallet == 0:
        print("Sorry! Not enough funds!")
        time.sleep(3)
        main_menu(wallet)

    if bet > wallet:
        print("Not enough funds for that bet!")
        time.sleep(1.4)
        main_menu(wallet)


def deposit_funds(wallet):
    clear_console()

    print("----[Deposit Funds]----\n")
    deposit = int(input("How much would you like to deposit?: $"))

    wallet += deposit

    print("Successfully updated wallet with: $", deposit)
    time.sleep(2)

    main_menu(wallet)


def withdraw_funds(wallet):
    clear_console()
    print("----[Withdraw Funds]----\n")
    withdrawal = int(input("How much would you like to withdraw?: $"))

    wallet -= withdrawal

    print("Successfully withdrew: $", withdrawal)
    time.sleep(2)
    main_menu(wallet)


def roulette_f(wallet):
    outcomes = {'00': 1 / 38, '0': 1 / 19, '1': 1 / 38, '2': 1 / 38, '3': 1 / 38, '4': 1 / 38, '5': 1 / 38, '6': 1 / 38,
                '7': 1 / 38, '8': 1 / 38, '9': 1 / 38, '10': 1 / 38, '11': 1 / 38, '12': 1 / 38, '13': 1 / 38,
                '14': 1 / 38,
                '15': 1 / 38, '16': 1 / 38, '17': 1 / 38, '18': 1 / 38, '19': 1 / 38, '20': 1 / 38, '21': 1 / 38,
                '22': 1 / 38, '23': 1 / 38, '24': 1 / 38, '25': 1 / 38, '26': 1 / 38, '27': 1 / 38, '28': 1 / 38,
                '29': 1 / 38, '30': 1 / 38, '31': 1 / 38, '32': 1 / 38, '33': 1 / 38, '34': 1 / 38, '35': 1 / 38,
                '36': 1 / 38}

    colors = {'00': 'green', '0': 'green', '1': 'red', '2': 'black', '3': 'red', '4': 'black', '5': 'red', '6': 'black',
              '7': 'red', '8': 'black', '9': 'red', '10': 'black', '11': 'black', '12': 'red', '13': 'black',
              '14': 'red',
              '15': 'black', '16': 'red', '17': 'black', '18': 'red', '19': 'red', '20': 'black', '21': 'red',
              '22': 'black', '23': 'red', '24': 'black', '25': 'red', '26': 'black', '27': 'red', '28': 'black',
              '29': 'black', '30': 'red', '31': 'black', '32': 'red', '33': 'black', '34': 'red', '35': 'black',
              '36': 'red'}

    while True:

        bet = int(input("Enter your bet amount (or 0 to quit): "))
        bet_check(wallet, bet)
        choice = input("Enter a number (0-36), or '00' for 00, or a color (red/black): ")

        outcome = random.choices(list(outcomes.keys()), list(outcomes.values()))[0]

        print("The ball landed on", outcome, "(", colors[outcome], ")")
        if choice.isdigit():
            if choice == outcome:
                wallet += bet * 35
                print("You win")
            else:
                wallet -= bet
                print("You lose")
        elif choice in ['red', 'black']:
            if choice == colors[outcome]:
                wallet += bet
                print("You win")
            else:
                wallet -= bet
                print("You lose")
        else:
            print("Invalid choice")
            continue

        print("Your balance is now", wallet)

        if wallet < 0:
            print("You're out of money! Thanks for playing.")
            break
    return wallet


def blackjack_f(wallet):
    playing = True
    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    class Card:
        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + ' of ' + self.suit

    class Deck:
        def __init__(self):
            self.deck = []
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))

        def __str__(self):
            deck_comp = ''
            for card in self.deck:
                deck_comp += '\n' + card.__str__()
            return 'The deck has: ' + deck_comp

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            single_card = self.deck.pop()
            return single_card

    class Hand:
        def __init__(self):
            self.cards = []
            self.value = 0
            self.aces = 0

        def add_card(self, card):
            self.cards.append(card)
            self.value += values[card.rank]
            if card.rank == 'Ace':
                self.aces += 1

        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

    class Chips:
        def __init__(self):
            self.total = wallet
            self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet

    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if chips.bet > chips.total:
                    print("Sorry, your bet can't exceed", chips.total)
                else:
                    break

    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(deck, hand):
        global playing

        while True:
            x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

            if x[0].lower() == 'h':
                hit(deck, hand)
                show_some(player_hand, dealer_hand)  # Added this line to show updated hands

                if player_hand.value > 21:
                    player_busts(player_hand, dealer_hand, player_chips)
                    break
                else:
                    hit_or_stand(deck, player_hand)

            elif x[0].lower() == 's':
                print("Player stands. Dealer is playing.")
                playing = False
            else:
                print("Sorry, please try again.")
                continue
            break

    def show_some(player, dealer):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', dealer.cards[1])
        print("\nPlayer's Hand:", *player.cards, sep='\n ')

    def show_all(player, dealer):
        print("\nDealer's Hand:", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand:", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)

    def player_busts(player, dealer, chips):
        nonlocal wallet
        print("Player busts!")
        chips.lose_bet()
        wallet = chips.total

    def player_wins(player, dealer, chips):
        nonlocal wallet
        print("Player wins!")
        chips.win_bet()
        wallet = chips.total

    def dealer_busts(player, dealer, chips):
        nonlocal wallet
        print("Dealer busts!")
        chips.win_bet()
        wallet = chips.total

    def dealer_wins(player, dealer, chips):
        nonlocal wallet
        print("Dealer wins!")
        chips.lose_bet()
        wallet = chips.total

    def push(player, dealer):
        print("Dealer and Player tie! It's a push.")

    while True:
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)

        show_some(player_hand, dealer_hand)

        while playing:

            hit_or_stand(deck, player_hand)

            show_some(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)

                show_all(player_hand, dealer_hand)

                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand, player_chips)
                    break

                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)
                    break

                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)
                    break

                else:
                    push(player_hand, dealer_hand)
                    break

        print("\nPlayer's winnings stand at", player_chips.total)

        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            time.sleep(2)
            main_menu(wallet)
            break
    wallet = player_chips.total

    return wallet


def SlotsF(wallet):
    symbols = {
        '🍒': {'value': 1.0, 'probability': 0.15},
        '🍋': {'value': 1.5, 'probability': 0.1},
        '🍊': {'value': 2.5, 'probability': 0.1},
        '🍉': {'value': 4.0, 'probability': 0.08},
        '🍇': {'value': 10.0, 'probability': 0.05},
        '🍓': {'value': 40.0, 'probability': 0.03},
        '🍎': {'value': 70.0, 'probability': 0.02},
        '７': {'value': 100.0, 'probability': 0.01}

    }

    num_lines = 3
    num_reels = 3
    num_symbols = 5

    def spin():
        reels = [
            [random.choices(list(symbols.keys()), weights=list(s['probability'] for s in symbols.values()))[0] for i in
             range(num_symbols)] for j in range(num_reels)]
        results = []
        for i in range(num_reels):
            reel_symbols = [reels[i][j] for j in range(num_symbols)]
            payout = 0
            for symbol in set(reel_symbols):
                count = reel_symbols.count(symbol)
                if count >= 3:
                    payout += symbols[symbol]['value'] * (2.0 ** (count - 3))
            results.append(payout)
        return reels, results

    def display(reels, results):
        # Print the reels
        for i in range(num_reels):
            print(reels[i])
        # Print the results
        print('Results:')
        for i in range(num_lines):
            print(f'Line {i + 1}: {results[i]} coins')

    while True:
        inp = input('Press Enter to spin the reels...')
        reels, results = spin()
        wallet -= 2
        display(reels, results)
        total_payout = sum(results)
        wallet += total_payout
        print(f'Your total payout is {total_payout} coins.')
        print(f'Your current balance is {wallet} coins.')
        print("Type q to exit")
        if inp == "q":
            time.sleep(2)
            main_menu(wallet)


def first_menu():
    clear_console()
    print("----[Welcome to Casino 7bet]----\n")
    wallet = int(input("Please deposit funds: "))
    error_handling(wallet)
    main_menu(wallet)


# Check if int
def error_handling(arg1, arg2="", arg3="", arg4=""):
    if isinstance(arg1, int):
        pass
    else:
        usage()


# Restarts scripts when input is not an int
def usage():
    print("Please use an integer!")
    time.sleep(1.3)


first_menu()
