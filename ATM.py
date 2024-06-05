import string
import os

# Creating lists of users, their PINs, and bank statements
users = ['user1', 'user2', 'user3']
pins = ['1111', '2222', '3333']
amounts = [10000, 20000, 15000]
count = 0

# WHILE LOOP CHECKS EXISTENCE OF THE ENTERED USERNAME
print(" Welcome to ATM MANAGEMENT SYSTEM ")

while True:
    user = input('ENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print("INVALID USERNAME")
        
# COMPARING PIN
while count < 3:
    pin = input('PLEASE ENTER PIN: ')
    if pin.isdigit():
        if user == users[0] and pin == pins[0]:
            break
        elif user == users[1] and pin == pins[1]:
            break
        elif user == users[2] and pin == pins[2]:
            break
        else:
            count += 1
            print(" INVALID PIN ")
    else:
        print(' THE PIN CONSISTS OF 4 DIGITS ')

# IN CASE OF A VALID PIN CONTINUING OR EXITING
if count == 3:
    print('3 UNSUCCESSFUL PIN ATTEMPTS, EXITING')
    print('!!!!! YOUR CARD HAS BEEN LOCKED!!!!!!')
else:
    print('LOGIN SUCCESSFUL, CONTINUE')
    print()
    print(' ', str.capitalize(users[n]), "Welcome to ATM")
    print(' ATM SYSTEM ')

while True:
    print('SELECT FROM FOLLOWING OPTIONS:')
    print('Check Balance (S)')
    print('Withdraw (W)')
    print('Depositing (D)')
    print('Change PIN (P)')
    print('QUIT (Q)')
    response = input("Type the letter of your choice:")
    
    if response == 's' or response == 'S':
        print(str.capitalize(users[n]),'YOU HAVE', amounts[n], 'RUPEES IN YOUR ACCOUNT:')
    elif response == 'w' or response =='W':
        cash_out= int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print()
        if cash_out % 10 != 0:
            print('AMOUNT YOU WANT TO WITHDRAW IS TO BE IN MULTIPLES OF 10')
        elif cash_out > amounts[n]:
            print('YOU HAVE INSUFFICENT BALANCE')
        else:
            amounts[n] = amounts[n] - cash_out
            print('YOUR NEW BALANCE IS:', amounts[n],'RUPEES')
    elif response == 'd' or response =='D':
        print()
        cash_in = int(input('ENTER AMOUNT YOU WANT TO DEPOSIT:'))
        print()
        if cash_in % 10 != 0:
            print('AMOUNT YOU WANT TO DEPOSIT IS TO BE IN MULTIPLES OF 10')
        else:
            amounts[n] = amounts[n] + cash_in
            print('YOUR NEW BALANCE IS:', amounts[n],'RUPEES')
    elif response == 'p' or response == 'P':
        new_pin=input('ENTER A NEW PIN:')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            new_ppin = input('CONFIRM NEW PIN:')
            if new_ppin != new_pin:
                print('PIN MISMATCH')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print(' NEW PIN MUST CONSIST OF 4 DIGITS ')
            print('AND MUST BE DIFFERENT TO PREVIOUS PIN')
    elif response == 'q' or response == 'Q':
        break
    else:
        print('RESPONSE NOT VALID')
