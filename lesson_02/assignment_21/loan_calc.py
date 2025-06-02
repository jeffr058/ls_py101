def prompt(message):
    print(f'==> {message}')

def check_input(input_str):
    if '-' in input_str:
        return True
    
    try:
        float(input_str)
    except ValueError:
        return True
    
    return False

prompt('What is the loan amount?')
loan_amount = input().replace('$', '').replace(',', '')

while check_input(loan_amount):
    prompt('Please enter a valid amount.')
    loan_amount = input().replace('$', '').replace(',', '')

loan_amount_clean = float(loan_amount)

print(type(loan_amount_clean))
print(loan_amount_clean)

# prompt('What is the APR?')
# apr = input()

# prompt('What is the loan duration?')
# loan_duration = input()