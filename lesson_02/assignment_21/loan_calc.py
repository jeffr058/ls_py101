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
    
def set_num_type(clean_str):
    if '.' in clean_str:
        return float(clean_str)
    else:
        return int(clean_str)

prompt('What is the loan amount?')
loan_amount = input().replace('$', '').replace(',', '')

while not check_input(loan_amount):
    prompt('Please enter a valid amount.')
    loan_amount = input().replace('$', '').replace(',', '')

# loan_amount_clean = set_num_type(loan_amount)

print(type(loan_amount))
print(loan_amount)

# prompt('What is the APR?')
# apr = input()

# prompt('What is the loan duration?')
# loan_duration = input()