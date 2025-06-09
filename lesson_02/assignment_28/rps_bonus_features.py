import json
import random
import pdb
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

def declare_grand_winner(dict):
    for key, value in dict.items():
        if (key != 'tie') and (value == 3):
            prompt(f"{messages['grand_winner']} {key.capitalize()}!")
            prompt(messages['separator'])

score_dict = {'player': 0, 'computer': 0, 'tie': 0}
restart = True
ask_play_again = False

while restart == True:
    prompt(
        f"{messages['choose']} {', '.join(VALID_CHOICES)}\n"
        f"{messages['separator']}\n" 
        f"{messages['shortened_choices']}"
    )

    while True:

        while True:

            choice = input()
            if choice == 's':
                prompt(messages['specify_s'])
            else:
                break

        for valid_choice in VALID_CHOICES:
            if choice and choice.lower() == valid_choice[0:len(choice)]:
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
    
    declare_grand_winner(score_dict)

    for key, value in score_dict.items():
        if (key != 'tie') and (value == 3):
            ask_play_again = True

    while ask_play_again == True:
        prompt(messages['play_again'])
        answer = input().lower()



        while True:
            if answer.startswith('y') or answer.startswith('n'):
                break
            else:
                prompt(messages['invalid'])
                answer = input().lower()


        if answer[0] == ('y'):
            for key, value in score_dict.items():
                score_dict[key] = 0
            ask_play_again = False
        else:
            restart = False
        
        break

# play again - dont let it loop back to asking y/n
# change UI of program (separators)
