balans = 10000
a = input('Deposit or Withdraw: ')
b = int(input('Amount of money: '))

if a == 'Deposit':
    balance += b
    print(f'Balance: {balance}')
if a == 'Withdraw':
    balance -= b
    if balance < 0:
        print("Ther aren't enough balance in your account!")
    else:
        print(f'Balance: {balance}')