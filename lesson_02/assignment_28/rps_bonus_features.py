import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

COMBINATIONS = {
    'rock': ('scissors', 'lizard'),
    'paper': ('rock', 'spock'),
    'scissors': ('paper', 'lizard'),
    'lizard': ('paper', 'spock'),
    'spock': ('scissors', 'rock'),
}

def prompt(message):
    print(f'==> {message}')

def determine_winner(player, computer):
    if computer in COMBINATIONS[player]:
        winner = 'player'
    elif player == computer:
        winner = 'tie'
    else:
        winner = 'computer'
    return winner

def display_winner(player, computer):
    prompt(f'You chose {player}, computer chose {computer}.')

    winner = determine_winner(player, computer)

    if winner == 'player':
        prompt('You win!')
    elif winner == 'computer':
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

while True:
    choice = ''

    prompt(
        f'Choose one: {', '.join(VALID_CHOICES)}\n'
        '---------------------------------------------------------------\n'
        '"r": rock, "p": paper, "sc": scissors, "l": lizard, "sp": Spock'
    )

    while True:

        while True:  # clarify_s_input()
            user_entry = input()

            if user_entry == 's':
                prompt('Please use "sc" for scissors or "sp" for Spock.')
            else:
                break

        for valid_choice in VALID_CHOICES:
            if user_entry.lower() == valid_choice[0:len(user_entry)]:
                choice = valid_choice
                break

        if choice in VALID_CHOICES:
            break

        prompt("That's not a valid choice.")

    computer_choice = random.choice(VALID_CHOICES)

    determine_winner(choice, computer_choice)
    display_winner(choice, computer_choice)

    while True:
        prompt('Do you want to play again? (y/n)')
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt("That's not a valid choice.")

    if answer[0] == 'n':
        break

# capitalize spock in the prompt for VALID_CHOICES? (currently inconsistent)
# use JSON file for messages?