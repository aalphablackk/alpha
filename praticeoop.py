class Bank:
    # transaction=''
    def __init__(self, bankname, balance):
        self.bankname = bankname
        self.balance = balance
        self.transaction = []
        self.home()
        # self.deposit()
        # self.withdraw()

    def home(self):
        print(
            '''
            1. Deposit
            2. Withdraw
            3. transaction
            4. Balance
            '''
        )
        choice=input('What is your choice: ')
        if choice=='1':
            self.deposit()
        elif choice == '2':
            self.withdraw()
        elif choice == '3':
            self.transact()
        elif choice == '4':
            self.balancee()
    def deposit(self):
        amount = int(input('Enter amount to deposit: '))
        if amount <=0:
            print('Invalid amount')
        else:
            self.balance+= amount

            # print(f'Deposit of {amount} successful your balance is: {self.balance}')
            depo=f'Deposit of {amount} successful your balance is: {self.balance}'
            self.transaction.append(depo)
            print(self.transaction[-1])
            # return
        self.home()

    def withdraw(self):
        # print(self.transaction)
        amount = int(input('Enter the amount you want to withdraw: '))
        
        if self.balance < amount:
            print('Insufficient balance')
        else:
            self.balance-= amount

            # print(f'Withdrawal of {amount} successful your balance is: {self.balance}')
            withd=f'Withdrawal of {amount} successful your balance is: {self.balance}'
            self.transaction.append(withd)
            print(self.transaction[-1])
            # return
        self.home()
        

    def transact(self):
        for y in self.transaction:
            print(y)
        self.home()
        # pass
    def balancee(self):
        print(f'Welcome your current balance is {self.balance}')
        self.home()

uba = Bank('uba_bank', 1000 )