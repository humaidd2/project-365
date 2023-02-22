import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw")
    elif user_score == 0 or computer_score > 21:
        print("You win")
    elif computer_score == 0 or user_score > 21:
        print("You Lost, The computer wins")
    else:
        if user_score > computer_score:
            print("You win")
        else:
            print("You Lost")


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print("Your cards: ", user_cards, "Current Score: ", user_score)
        print("Computer's first card: ", computer_cards[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            elif user_should_deal == "n":
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    compare(user_score, computer_score)
    print(f"Your final hand is {user_cards}, score: {user_score}")
    print(f"Computer's final hand is {computer_cards}, score: {computer_score}")


while input("Do you want to play a game of Blackjack? ") == "y":
    play_game()
