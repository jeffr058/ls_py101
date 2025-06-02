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

prompt('What is the loan amount?')
loan_amount = input().replace('$', '').replace(',', '')

while is_input_number(loan_amount):
    prompt('Please enter a valid amount.')
    loan_amount = input().replace('$', '').replace(',', '')

loan_amount_clean = float(loan_amount)

prompt('What is the APR?')
apr = input()

while is_input_number(apr):
    prompt('Please enter a valid number.')
    apr = input()

apr_clean = float(apr) / 100
apr_monthly = apr_clean / 12

prompt('What is the loan duration in years?')
loan_duration = input()

while is_input_number(loan_duration):
    prompt('Please enter a valid number.')
    loan_duration = input()

loan_duration_clean = float(loan_duration)
loan_duration_months = loan_duration_clean * 12

monthly_payment = calculate_monthly_payment(loan_amount_clean, apr_monthly, loan_duration_months)

print(monthly_payment)