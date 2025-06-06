import random
import pdb

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'==> {message}')

def display_winner(player, computer):
    prompt(f'You chose {player}, computer chose {computer}.')

    if ((player == 'rock' and computer == 'scissors') or
        (player == 'rock' and computer == 'lizard') or
        (player == 'paper' and computer == 'rock') or
        (player == 'paper' and computer == 'spock') or
        (player == 'scissors' and computer == 'paper') or
        (player == 'scissors' and computer == 'lizard') or
        (player == 'lizard' and computer == 'paper') or
        (player == 'lizard' and computer == 'spock') or
        (player == 'spock' and computer == 'scissors') or
        (player == 'spock' and computer == 'rock')):
        prompt('You win!')
    elif ((computer == 'rock' and player == 'scissors') or
        (computer == 'rock' and player == 'lizard') or
        (computer == 'paper' and player == 'rock') or
        (computer == 'paper' and player == 'spock') or
        (computer == 'scissors' and player == 'paper') or
        (computer == 'scissors' and player == 'lizard') or
        (computer == 'lizard' and player == 'paper') or
        (computer == 'lizard' and player == 'spock') or
        (computer == 'spock' and player == 'scissors') or
        (computer == 'spock' and player == 'rock')):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

while True:
    prompt(f'Choose one: {', '.join(VALID_CHOICES)}')

    while True:
        user_entry = input()

        for valid_choice in VALID_CHOICES:
            if user_entry.lower() == valid_choice[0:len(user_entry)]:
                choice = valid_choice
    
        if choice in VALID_CHOICES:    
            break
        else:
            prompt("That's not a valid choice.")

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    while True:
        prompt('Do you want to play again? (y/n)')
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            choice = ''
            break
        
        prompt("That's not a valid choice.")

    if answer[0] == 'n':
        break

# why does 's' result in choosing spock?
# on prompt print available shortened input options