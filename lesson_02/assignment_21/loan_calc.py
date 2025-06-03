import json

with open('loan_calc_messages.json', 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f'==> {message}')

def is_input_invalid(input_str):
    if '-' in input_str:
        return True

    try:
        float(input_str)
    except ValueError:
        return True

    return False

def is_input_correct(input_type, display_input):
    prompt(messages[input_type] + display_input)
    prompt(messages['is_correct'])

    user_confirm = input()

    if user_confirm and (user_confirm[0].casefold() != 'y'):
        return False

    return True

def calculate_monthly_payment(amount, int_rate, length):
    monthly_payment = amount * (int_rate / (1 - (1 + int_rate) ** (-length)))
    return monthly_payment

prompt(messages['welcome'])

while True:

    while True:
        prompt(messages['get_loan_amount'])
        loan_amount = input().replace('$', '').replace(',', '')

        while is_input_invalid(loan_amount):
            prompt(messages['invalid_input'])
            loan_amount = input().replace('$', '').replace(',', '')

        loan_amount_clean = float(loan_amount)

        display_loan_amount = f'{loan_amount_clean:,.2f}.'

        if is_input_correct('confirm_loan_amount', display_loan_amount):
            break

    while True:
        prompt(messages['get_apr'])
        apr = input()

        while is_input_invalid(apr):
            prompt(messages['invalid_input'])
            apr = input()

        display_apr = f'{apr}%.'

        if is_input_correct('confirm_apr', display_apr):
            break

    apr_clean = float(apr) / 100
    apr_monthly = apr_clean / 12

    while True:
        prompt(messages['get_loan_duration'])
        loan_duration = input()

        while is_input_invalid(loan_duration):
            prompt(messages['invalid_input'])
            loan_duration = input()

        display_loan_duration = f'{loan_duration} years.'

        if is_input_correct('confirm_loan_duration', display_loan_duration):
            break

    loan_duration_clean = float(loan_duration)
    loan_duration_months = loan_duration_clean * 12

    monthly_payment = calculate_monthly_payment(
        loan_amount_clean,
        apr_monthly,
        loan_duration_months,
    )

    prompt(messages['monthly_payment']+ f'{monthly_payment:,.2f}.')

    prompt(messages['new_calc'])
    new_calc = input()

    if new_calc and (new_calc[0].casefold() != 'y'):
        prompt(messages['goodbye'])
        break