import json
import random

with open('rps_messages.json', 'r') as file:
    messages = json.load(file)

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

def display_winner(player, computer, winner):
    prompt(messages['player_choice'] + f'{player}. ' + 
           messages['computer_choice'] + f'{computer}.')

    if winner != 'tie':
        prompt(messages['round_winner'] + f'{winner.capitalize()}.')
    else:
        prompt(messages['tie'])
        
    prompt(messages['separator'])

while True:
    choice = ''

    prompt(
        messages['choose'] + f'{', '.join(VALID_CHOICES)}\n' + 
        messages['separator'] + '\n' + 
        messages['shortened_choices']
    )

    while True:

        while True:

            user_entry = input()

            if user_entry == 's':
                prompt(messages['specify_s'])
            else:
                break

        for valid_choice in VALID_CHOICES:
            if user_entry.lower() == valid_choice[0:len(user_entry)]:
                choice = valid_choice
                break

        if choice in VALID_CHOICES:
            break

        prompt(messages['invalid'])

    computer_choice = random.choice(VALID_CHOICES)

    round_winner = determine_winner(choice, computer_choice)
    display_winner(choice, computer_choice, round_winner)

    while True:
        prompt(messages['play_again'])
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt(messages['invalid'])

    if answer[0] == 'n':
        break

# don't ask to play again until after 3 wins