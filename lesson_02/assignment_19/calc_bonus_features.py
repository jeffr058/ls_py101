import json

with open('calculator_messages.json', 'r') as file:
    data = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(data['welcome'])

while True:
    prompt(data['num1'])
    number1 = input()

    while invalid_number(number1):
        prompt(data['num_error'])
        number1 = input()

    prompt(data['num2'])
    number2 = input()

    while invalid_number(number2):
        prompt(data['num_error'])
        number2 = input()

    prompt(data['operator'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(data['operator_error'])
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt(f'{data['result']} {output}')

    prompt(data['new_calc'])
    new_calc = input()

    if new_calc and new_calc[0].lower() != 'y':
        break