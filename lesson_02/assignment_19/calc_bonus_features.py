import json

with open('calculator_messages.json', 'r') as file:
    messages = json.load(file)

messages_en = messages['english']
messages_fr = messages['french']

user_lang = messages_en

def prompt(message):
    print(f"==> {message}")

def num_type(number_str):
    if '.' in number_str:
        return float(number_str)
    else:
        return int(number_str)

def invalid_number(number_str):
    try:
        num_type(number_str)
    except ValueError:
        return True

    return False

prompt(messages['language'])
lang_choice = input()

while lang_choice not in ['1', '2']:
    prompt(messages['lang_error'])
    lang_choice = input()

match lang_choice:
    case '1':
        user_lang = messages_en
    case '2':
        user_lang = messages_fr

prompt(user_lang['welcome'])

while True:
    prompt(user_lang['num1'])
    number1 = input()

    while invalid_number(number1):
        prompt(user_lang['num_error'])
        number1 = input()

    prompt(user_lang['num2'])
    number2 = input()

    while invalid_number(number2):
        prompt(user_lang['num_error'])
        number2 = input()

    prompt(user_lang['operator'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(user_lang['operator_error'])
        operation = input()

    match operation:
        case '1':
            output = num_type(number1) + num_type(number2)
        case '2':
            output = num_type(number1) - num_type(number2)
        case '3':
            output = num_type(number1) * num_type(number2)
        case '4':
            output = num_type(number1) / num_type(number2)

    prompt(f"{user_lang['result']} {output}")

    prompt(user_lang['new_calc'])
    new_calc = input()

    if new_calc and new_calc[0].lower() != 'y':
        break