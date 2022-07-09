import random
from blackjack_art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(card_list):
    """Take a list of cards and return a score"""
    score = sum(card_list)
    if score == 21 and len(card_list) == 2:
        return 0
    elif 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)
    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "You lose. Dealer has blackjack!"
    elif user_score == 0:
        return "You have blackjack! You win!!"
    elif user_score > 21:
        return "You bust. Dealer wins."
    elif computer_score > 21:
        return "Dealer busts. You win!!"
    elif user_score > computer_score:
        return "You win. Your score beats the Dealer!!"
    else:
        return "You lose. Dealer has higher score."


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"    Your cards: {user_cards} Current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_move = input(
                "Type 'y' to get another card, type 'n' to stand: ")
            if user_move == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"    Dealer's final hand: {computer_cards}, Dealer score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':

    play_game()
