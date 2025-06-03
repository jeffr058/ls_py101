import json

with open('loan_calc_messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f'==> {message}')

def is_input_number(input_str):
    if '-' in input_str:
        return True
    
    try:
        float(input_str)
    except ValueError:
        return True
    
    return False

def calculate_monthly_payment(amount, int_rate, length):
    monthly_payment = amount * (int_rate / (1 - (1 + int_rate) ** (-length)))
    return round(monthly_payment, 2)

prompt(messages['welcome'])

while True:

    prompt(messages['get_loan_amount'])
    loan_amount = input().replace('$', '').replace(',', '')

    while is_input_number(loan_amount):
        prompt(messages['invalid_input'])
        loan_amount = input().replace('$', '').replace(',', '')

    loan_amount_clean = float(loan_amount)

    prompt(messages['get_apr'])
    apr = input()

    while is_input_number(apr):
        prompt(messages['invalid_input'])
        apr = input()

    apr_clean = float(apr) / 100
    apr_monthly = apr_clean / 12

    prompt(messages['get_loan_duration'])
    loan_duration = input()

    while is_input_number(loan_duration):
        prompt(messages['invalid_input'])
        loan_duration = input()

    loan_duration_clean = float(loan_duration)
    loan_duration_months = loan_duration_clean * 12

    monthly_payment = calculate_monthly_payment(loan_amount_clean, apr_monthly, loan_duration_months)

    prompt(messages['monthly_payment']+ f'{monthly_payment}.')

    prompt(messages['new_calc'])
    new_calc = input()

    if new_calc and (new_calc[0].casefold() != 'y'):
        prompt(messages['goodbye'])
        break