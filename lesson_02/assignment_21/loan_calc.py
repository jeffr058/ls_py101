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
    
def clean_input(input_str):
    symbols = ['$', ',']
    
    for symbol in symbols:
        if symbol in input_str:
            input_str = input_str.replace(symbol, '')
    
    clean_str = input_str
    
    return clean_str
    
def set_num_type(clean_str):
    if '.' in clean_str:
        return float(clean_str)
    else:
        return int(clean_str)

prompt('What is the loan amount?')
loan_amount = clean_input(input())

while not check_input(loan_amount):
    prompt('Please enter a valid amount.')
    loan_amount = clean_input(input())

loan_amount_clean = set_num_type(loan_amount)
print(type(loan_amount_clean))
print(loan_amount_clean)

# prompt('What is the APR?')
# apr = input()

# prompt('What is the loan duration?')
# loan_duration = input()