# 14/5/2025
# class-- int
# OOP- Object oriented programming--- is the aspect of programming where codes are written in class for the purpose of reusability
# object is the variable created from the class i.e x
# Basically everything in python either belongs to a class or created from a class
# What is a class?
# Class is a group of modules and method designed to perform an operation 
# Features of class
# Attributes/properties/ Variables
    # Name of the class
# Methods/functions
    # action performed by a class
# Objects
    # are the variables created from the class. 
# Constructor
    # part of the class that gets initialized before any other operations
# Reference
    # inbuilt parameters of a constructor (self)

# x=int(5)
# print(type(x))

# class bankapp:
#     name= 'uba_bank'
#     owner= 'Tony_Elumelu'
#     def __init__(self,/,*db_name, db_password):
#         self.home()
#     def home(self):
#         print('Welcome')
#     def deposit(self):
#         print('Deposit what you want')
# uba=bankapp(db_password=22)
# print(uba)
# uba.deposit()
# print(type(uba))
# print(uba.owner)


# next week

# Components of OOP
# Encapsulation(Private, public, protected, Static)
# Inheritance()

# 18/05/2026
# class car: #car is the class here
#     brand = 'benzo' #brand here is the properties
#     model = 'benzoli'
#     yop = 2026
#     color = 'black'


#     def __init__(self,brand, model, yop):
#         self.brand = brand
#         self.model = model
#         self.yop = yop
#         self.drive()
    
    # def introduce(self): #self here is the reference while introduce is the method/function
    #     print(f'This is {self.brand}, {self.model}, {self.yop}, {self.color} car')
    
    # def drive(self):
    #     print(f'the car {self.brand}, {self.model}, {self.color} is moving')

# car1=car() #car1 here is the object
# car1=car(james, real, yop) #car1 here is the object
# car2 = car()
# car2.model = 'benzola'
# car2.color = 'pink'
# car2.drive()
# print(car1.brand)
# print(car1.model)
# print(car1.introduce())
# print(car2.introduce())
# print(car1.drive())
# print(car2.drive())


# Components of OOP
# Encapsulation, inheritance abstraction polymophism
# 
# Encapsulation
    # private property, public property and protected property

    # __   Privatalized  _ Protected    the default is Public


# class Bankapp:

    # __slots__ =['__balance']
#     bankname='SQI_bank'
#     __balance = 2000

#     def check_balance(self):
        # print(f'Your balance is : {self.balance}')
        # return self.__balance


# uba=Bankapp()
# print(uba._Bankapp__balance)
# uba.__balance = 5000
# print(uba.__balance)
# print(uba.check_balance())


# Inheritance

# class father:
#     name = 'Charles'
#     height = '6.7ft'
#     surname = 'Taiwo'
#     course = 'Data science'

# fath = father()

# class son(father):
#     name='james'
#     course='computer science'

# son1=son()
# print(son1.course)



# class Bank:
#     # transaction=''
#     def __init__(self, bankname, balance, transaction):
#         self.bankname = bankname
#         self.balance = balance
#         self.transaction = transaction
#         self.home()
#         # self.deposit()
#         # self.withdraw()

#     def home(self):
#         print(
#             '''
#             1. Deposit
#             2. Withdraw
#             3. transaction
#             4. Balance
#             5. Exit
#             '''
#         )
#         choice=input('What is your choice: ')
#         if choice=='1':
#             self.deposit()
#         elif choice == '2':
#             self.withdraw()
#         elif choice == '3':
#             self.transact()
#         elif choice == '4':
#             self.balancee()
#         elif choice == '5':
#             exit()
#     def deposit(self):
#         amount = int(input('Enter amount to deposit: '))
#         if amount <=0:
#             print('Invalid amount')
#         else:
#             self.balance+= amount

#             # print(f'Deposit of {amount} successful your balance is: {self.balance}')
#             depo=f'Deposit of {amount} successful your balance is: {self.balance}'
#             self.transaction.append(depo)
#             print(self.transaction[-1])
#             # return
#         self.home()

#     def withdraw(self):
#         # print(self.transaction)
#         amount = int(input('Enter the amount you want to withdraw: '))
#         if amount <=0:
#             print('Invalid amount')
#             self.home()
#         if self.balance < amount:
#             print('Insufficient balance')
#         else:
#             self.balance-= amount

#             # print(f'Withdrawal of {amount} successful your balance is: {self.balance}')
#             withd=f'Withdrawal of {amount} successful your balance is: {self.balance}'
#             self.transaction.append(withd)
#             print(self.transaction[-1])
#             # return
#         self.home()
        

#     def transact(self):
#         for y in self.transaction:
#             print(y)
#         self.home()
#         # pass
#     def balancee(self):
#         print(f'Welcome your current balance is {self.balance}')
#         self.home()

# uba = Bank('uba_bank', 1000, [] )























# Assignment Class properties and Object Properties

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).

# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects

# class Person:
#   species = "Human" # Class property

#   def __init__(self, name):
#     self.name = name # Instance property

# p1 = Person("Emil")
# p2 = Person("Tobias")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)



# Change a class property:

# class Person:
#   lastname = ""

#   def __init__(self, name):
#     self.name = name

# p1 = Person("Linus")
# p2 = Person("Emil")

# Person.lastname = "Refsnes"

# print(p1.lastname)
# print(p2.lastname)




# class
# Module is a collection of classes that is designed for a specific operation
# from random import randint
# pyttsx3 librosas
# Library is a collection of module
# frameworks is like a builtin template 


# Modulization 
from random import randint
class Bankconfig:
    __students=[]
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance
        # self.trab
    def register(self, email, password, fullname, account_number):
        for user in self.__students:
            if email== user['email']:
                return {
                    'Status': False,
                    'message': 'Email already exists'
                }
        return{
            'Status': True,
            'message': f'Registration successful, your account number is {account_number}'
        }

class Bankapp(Bankconfig):
    def __init__(self, bank_name, balance):
       return super().__init__(bank_name, balance)

    def Home(self):
        print(f"""Welcome to {self.bank_name} Bank
              1. Register
              2. Login
              3.  exit
              
              """)
        choice=input('What is your choice: ')
        if choice=='1':
            self.signup()
        if choice=='2':
            pass
        if choice=='3':
            exit()
    def signup(self):
        email=input('Input your email: ')
        fullname=input('Input your fullname: ')
        password=input('Input your password: ')
        account_number= randint(00000000,99999999)
        result = self.register(email, password, fullname, account_number)
        if result :
            print(result['message'])
        else:
            print(result['message'])
            
     
bank=Bankapp('sqi', 0.0)
bank.Home()