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
    prompt(
        f"{messages['player_choice']} {player}. "
        f"{messages['computer_choice']} {computer}."
    )

    if winner != 'tie':
        prompt(f"{messages['round_winner']} {winner.capitalize()}.")
    else:
        prompt(messages['tie'])
        
    prompt(messages['separator'])

def keep_score(dict, winner):
    dict[winner] += 1

    return dict

score_dict = {'player': 0, 'computer': 0, 'tie': 0}

while True:
    choice = ''

    prompt(
        f"{messages['choose']} {', '.join(VALID_CHOICES)}\n"
        f"{messages['separator']}\n" 
        f"{messages['shortened_choices']}"
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
    score = keep_score(score_dict, round_winner)
    
    prompt(
        f"{messages['player_score']} {score_dict['player']}. "
        f"{messages['computer_score']} {score_dict['computer']}. "
        f"{messages['num_of_ties']} {score_dict['tie']}."
    )

    while True:
        prompt(messages['play_again'])
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt(messages['invalid'])

    if answer[0] == 'n':
        break

# don't ask to play again until after 3 wins