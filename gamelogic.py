import random
import configparser

def read_initial_money():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return int(config['GameSettings']['MY_MONEY'])

def play_game():
    money = read_initial_money()
    slots = list(range(1, 31))

    while True:
        print(f"Your current money: ${money}")
        bet_slot = int(input("Choose a slot (1-30) to place your bet: "))
        bet_amount = int(input("Enter your bet amount: "))

        winning_slot = random.choice(slots)

        if bet_slot == winning_slot:
            money += 2 * bet_amount
            print(f"Congratulations! You won ${2 * bet_amount} on slot {winning_slot}.")
        else:
            money -= bet_amount
            print(f"Sorry, you lost ${bet_amount}. The winning slot was {winning_slot}.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print(f"Game over. Your final money: ${money}")

if __name__ == "__main__":
    play_game()
