import random
from art import logo, vs
from game_data import data


def get_random_account():
    return random.choice(data)


def game():
    print(logo)
    score = 0
    player_a = get_random_account()
    player_b = get_random_account()

    game_over = False
    while not game_over:
        print(f"Compare A: {player_a['name']}, a {player_a['description']}, from {player_a['country']}")
        print(vs)
        print(f"Compare B: {player_b['name']}, a {player_b['description']}, from {player_b['country']}")
        ans = input("Who has more followers? Type 'A' or 'B': ").lower()
        if ans == "a" and player_a['follower_count'] > player_b['follower_count']:
            player_b = get_random_account()
            score += 1
        elif ans == "b" and player_b['follower_count'] > player_a['follower_count']:
            player_a = player_b
            player_b = get_random_account()
            score += 1
        else:
            game_over = True
    print(f"Sorry, That was wrong. Final Score: {score}")


game()
