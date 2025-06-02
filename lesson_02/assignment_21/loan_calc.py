def prompt(message):
    print(f'==> {message}')

def check_input(input_str):
    if (input_str == ''):
        return False
    elif any(not char.isdecimal() for char in input_str):
        if ('.' in input_str) and (input_str.count('.') <= 1):
            return True
        else:
            return False
    else:
        return True

prompt('What is the loan amount?')
loan_amount = input().replace('$', '').replace(',', '')

while not check_input(loan_amount):
    prompt('Please enter a valid amount.')
    loan_amount = input().replace('$', '').replace(',', '')

loan_amount_clean = float(loan_amount)

print(type(loan_amount_clean))
print(loan_amount_clean)

# prompt('What is the APR?')
# apr = input()

# prompt('What is the loan duration?')
# loan_duration = input()