'''
Bank App
    Home
Register
Email
Fullname
Password

Login
Email
Password

exit

    Dashboard
Check Balance
Withdraw
deposit
exit


Exit
'''
from random import randint
import json
import os
import datetime

# user=[]
def Get_database():
    if os.path.exists('Banking_db.json'):
        with open('Banking_db.json', 'r') as file:
            return json.load(file)
    else:
        with open('Banking_db.json','w') as file:
            json.dump([],file)
        return []
    
def save_user(user):
    with open('Banking_db.json','w') as file:
        json.dump(user, file, indent=4)




def home():
    user=Get_database()

    for i in user:
        i['status']=False
    print(
        '''
        Welcome here
        1. Register
        2. login
        3. Exit
        4. details
        '''
    )
    choice=input('What is your choice:  ')
    if choice=='':
        print('Kindly input the right choice: ')
        home()
    if choice =='1':
        register()
    if choice =='2':
        login()
    if choice =='3':
        exit()
    if choice =='4':
        userrr()

def register():
        
    user=Get_database()

    # print(user)
    print('Kindly fill the details to create your account'.center(50))
    email=input('Kindly input your email: ').strip()
    # if '@' not in email:
    #         print('Kindly input the correct email format')
    #         register()
    # if len(email)<2:
    #     print('Please enter the correct details')
    #     register()
    for us in user:
        checkmail=str(us['email'])
        if checkmail ==email:
            print('Email already exists')
            register()
    fullname=input('Kindly input your fullname: ')
    # if len(fullname)<2:
    #     print('Please enter the correct details')
    #     register()
    password=input('Kindly input your password: ')
    # if len(password)<2:
    #     print('Please enter the correct details')
    #     register()
    confirm_password=input('Kindly confirm your password: ')
    print(password)
    print(confirm_password)
    if password.strip()==confirm_password.strip():
        print('password correct')
    else:
        print('Try again')
        register()
    status=False
    balance=0
    account_number= randint(0000000000,9999999999)
    transaction=[]
    details={
        'email':email,
        'fullname':fullname,
        'password':password,
        'status': False,
        'balance':balance,
        'account_number':account_number,
        'transaction':transaction
    }
    
    user.append(details)
    save_user(user)
    home()

def userrr():
    user=Get_database()
    for us in user:
        # print(us)
        for i,y in us.items():
            print(f'{i}: {y},')

    home()

def login():
    user=Get_database()
    print(user)
    email=input('Kindly input your email: ')
    password=input('Kindly input your password: ')
    for i in user:
        if i['password'] == password and i['email'] == email:
            print(f'Login successful, Welcome {i['fullname']} your account number is {i['account_number']}')
            i['status']=True
            dashboard(i)
            return
    print('Invalid Login \n 1. try again \n 2. Create account')
    invalid()
    
    
def invalid():
    choice=input('What is your choice: ').strip()
    if choice=='1':
            login()
    if choice=='2':
            register()
    if choice=='':
        print('Kindly input the right choice: ')
        invalid()

def dashboard(i):
    user=Get_database()
    print(
        '''
        1. Withdraw
        2. Deposit
        3. Transaction
        4. Go back to Home
        5. Bank transfer
        '''
     )
    choice=input('Kindly choose: ')
    if choice=='':
        print('Kindly input the right choice: ')
        dashboard(i)
    if choice=='1':
        withdraw(i)
    if choice=='2':
        deposit(i)
    if choice=='3':
        transaction(i)
    if choice=='4':
        home()
    if choice=='5':
        transfer(i)
def withdraw(i):
    user=Get_database()
    print(i)
    choice=input('How much would you like to withdraw: ')
    if choice=='':
        print('Kindly input the right choice: ')
        withdraw(i)
    if float(choice)>i['balance']:
        print('Insufficient funds')
        dashboard(i)
    else:
        i['balance']-=float(choice)
        withdraww=f'{choice} withdrawn, New balance is {i['balance']} {datetime.datetime.now()}'
        i['transaction'].append(withdraww)
        # print(user)
        for us in user:
            print(us)
            if us['email']==i['email']:
                us['transaction']=i['transaction']
        save_user(user)
        print(i['transaction'])
    dashboard(i)

def deposit(i):
    user=Get_database()
    print(i)
    choice=input('How much would you like to withdraw: ')
    if choice=='':
        print('Kindly input the right choice: ')
        deposit(i)
    i['balance']+=float(choice)
    depositt=f'{choice} Deposited, New balance is {i['balance']} {datetime.datetime.now()}'
    i['transaction'].append(depositt)
    for us in user:
        print(us)
        if us['email']==i['email']:
            us['transaction']=i['transaction']
    # print(user)
    save_user(user)
    print(i['transaction'])
    dashboard(i)
def transaction(i):
    user=Get_database()

    for us in i['transaction']:
        print(us)
    dashboard(i)
def transfer(i):
    user=Get_database()

    print(f'Here are the available account number: ')
    for use in user:
        if use['account_number']==i['account_number']:
            continue
        print(use['account_number'])
    choice=int(input('Kindly input the account you want to transfer to: '))
    # print(use['account_number'])
    if choice==i['account_number']:
        print('Invalid account. \nNote: you can not transfer to your account')
        transfer(i)
    amount=int(input('How much do you want to deposit: '))
    for us in user:
        acc=us['account_number']
        match choice:
            case acc:
                print('Account found')
                print(acc)
                print(i['balance'])
                print(us['balance'])
                i['balance']-=amount
                us['balance']+=amount
                transferr=f'{amount} transferred to {acc}, New balance is {i['balance']} {datetime.datetime.now()}'
                recieved=f'{amount} recieved from {i['account_number']}, New balance is {us['balance']} {datetime.datetime.now()}'
                i['transaction'].append(transferr)
                us['transaction'].append(recieved)
                for us in user:
                    print(us)
                    if us['email']==i['email']:
                        us['transaction']=i['transaction']
                        # i['balance']=i['balance']
                save_user(user)
                print(us)
                print(i)
                break
    home()
home()