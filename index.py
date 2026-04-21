# print('Welcome to the Python world!')
# print(3+5)


# indentation

# x=6
# if x>5:
#     print('x is greater than 5')
# else:
#     print('x is not greater than 5')

# Commenting
# inline comment
# Greetings
# print('Welcome to python class')

'''
This part of code handles the registration part 
'''

# print('Welcome ooo, fill the form below')
# multiline comment

# python variables
# x='five'
# print(x)
# print(x+5)
# print(type(x))

# A variable is a container that holds a value in python. It is used to store data that can be used and manipulated in a program. In Python, you can create a variable by assigning a value to it using the equals sign (=). For example: 

# Casting is the process of converting a variable from one data type to another. In Python, you can cast a variable using built-in functions such as int(), float(), str(), etc. For example:

# Assignmment : Read on rules of variable declaration.
# 1. A variable name must start with a letter or an underscore (_).
# 2. A variable name cannot start with a number.
# 3. A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _).
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables).
# 5. A variable name cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.).
# 6. A variable name should be descriptive and meaningful to improve code readability.
# 7. Avoid using single-character variable names, except for counters or iterators in loops.
# 8. Use lowercase letters for variable names, and separate words with underscores (e.g., my_variable) for better readability.
# 9. Avoid using built-in function names as variable names (e.g., list, str, etc.) to prevent conflicts.
# 10. Always initialize variables before using them to avoid errors.
# 11. Use constants (variables that do not change) in uppercase letters (e.g., PI = 3.14) to distinguish them from regular variables.
# 12. Follow the naming conventions of your project or team for consistency.
# 13. Avoid using global variables when possible, as they can lead to code that is difficult to debug and maintain.
# 14. Use descriptive variable names that convey the purpose of the variable, making it easier for others to understand your code.

# Types of variables declaration
# One variable to one value
# x=5
# multiple variable to multiple values
# x,y,z=5,6,7
# multiple variable to single value
# x=y=z=5
# print(x)
# how to quote in a string
# x='I love eating "potatoes"'
# print(x)

# Variables casing
# 1. camelCase
# myVariableName='John'
# print(myVariableName)
# 2. snake_case
# my_variable_name='John'
# print(my_variable_name)
# 3. PascalCase
# MyVariableName='John'
# print(MyVariableName)

# x,*y,z=['Toyota', 'Honda', 'Mazda', 'Subaru', 'Nissan']
# print(y)

# Concantination
# x='Hello' 
# y=34
# # print(x+' '+y)
# print('my name is '+x+' and I am '+str(y))
# print(f'my name is {x} and I am {y}')

# Assignment: Learn to use .join() method to concatenate strings.

# x=' '.join(['my', 'name', 'is', 'John'])
# print(x)


# Python Output
# print('Hello World')

# python input
# name=input('What is your name? ')
# print(f'Hello, {name}!')
# age=input('What is your age? ')
# print(f'You are {age} years old.')
# best_food=input('What is your best food? ')
# print(f'Your best food is {best_food}.')
# print(f'Hello, {name}! You are {age} years old and your best food is {best_food}.')


# Simple form registration
'''
print('Welcome to the registration form')
first_name=input('What is your first name? ')
first_name=first_name.capitalize()
last_name=input('What is your last name? ')
last_name=last_name.capitalize()
phone_number=input('Enter your phone number: ')
age=input('What is your age? ')
month=input('What is your month? ')
day=input('What is your day of birth? ')
present_year=(input('What is the present year? '))
year=(int(present_year)-int(age))
print(f'Welcome, User {first_name} {last_name}! Your year of birth is {year} ')
print(f'Welcome, User {first_name} {last_name}! You are born on {day} {month} {year} Your phone number is {phone_number} ')
'''

# Note: Any number that is not used for mathematical operations is considered a string in python. 
# Python Datatypes

# 1. text datatypes
# 2. numeric datatypes
# 3. sequence datatypes
# 4. mapping datatypes
# 5. binary datatypes
# 6. none datatypes
# 7. boolean datatypes

# 1. text datatypes
# str - string datatype
# x='Hello World'

# 2. numeric datatypes
# int - integer datatype
# x=5
# float - floating-point datatype
# x=5.0
# complex - complex number datatype
# x=5+3j

# Assignment: learn about sequence datatypes in python and their methods.
# 3. sequence datatypes
# list - ordered, changeable, and allows duplicate elements means that you can change the elements in a list and it can contain duplicate values.
# x=[1, 2, 3, 4, 5]
# print(x)
# tuple - ordered, unchangeable, and allows duplicate elements means that you cannot change the elements in a tuple and it can contain duplicate values.
# x=(1, 2, 3, 4, 5)
# print(x)
# range - represents a sequence of numbers
# x=range(1, 10)
# print(x)
'''
color=['red','green','blue','yellow']
# print(type(color) )
print(color[-1])
color[0]='black'
print(color)
'''
'''
# tuple
color=('red','black','yellow','purple')
print(type(color))
print(color[0])
color[0]='green'
# Range
# print(range(6))
# print(list(range(6)))


food_items=['rice','beans','yam','wheat']
food_prices=['2500','3000','1500','1500']
for each_fi, each_fp in zip(food_items, food_prices):
    print(each_fi, each_fp)
'''


#mapping datatypes

# dictionary
# sets

# name= {
#     'rice' : '2500',
#     'beans' : '3000',
#     'yam' : '1500',
#     'wheat' : '1500'
# }
# print(name.keys())
# print(name.values())
# name['rice']='500'
# james={'light','smart', 'grit'}
# print(name)
# print(james)


# t_boi={}


# binary datatype
# bytearray
# memoryview
# ascii



# none datatype
# name =None
# if name is None:
#     print('name is empty')
'''

name=input('enter name: ')
if name:
    password=input('enter password: ')
    print('Successful')
else:
    print('Details can not be empty')
    
'''


# name=' '
# def register():
#     name=input('enter name: ')
#     if name.strip() == '' :
#         print('Details cannot be empty')
#         register()
#     if name == 'ade':
#             print('Already registered login instead')
#             exit()
#     else:
#         password=input('Enter Password: ')
#         if password.strip() == '':
#             print('Password can not be empty')
#             register()
#             print('registration successful')
# register()

'''

def Password():
    password=input('What is your password: ')
    if password.strip() == '':
        print('Password can not be empty')
        Password()
def register():
    name=input('What is your name: ')
    if name.strip() == '':
        print("name cannot be empty")
        register()
    else:
        if name.strip() == 'ade':
            print('user already exist')
            exit()
        Password()
        print('registration is successful')
register()
'''


        




# ASSIGMENT
'''


'''
# Build a ussd code 
# def register():
#     print('Type cancel to exit')
#     ussd=input('Input your ussd code: ')
#     if ussd =='*312#':
#         print(
#             '''
#         1. Data Plans
#         2. Enjoy 700MB for N150
#         3. Enjoy 7GB for N1500
#         4. Voice Offers
#         5. Roaming
#             '''
#         )
#         choice=input('Enter your choice: ')
#         if choice =='1':
#             print(
#             '''
#         1. Daily
#         2. 2-3 days
#         3. Weekly
#         4. Monthly
#         5. 2months+
#             '''
#         )
#             choice=input('Enter your choice: ')
#             if choice == '1':
#                 print(
#                     '''
#                 1. N75 =75Mb
#                 2. N100 =110Mb
#                 3. N200 =230Mb
#                 4. N350 =500Mb
#                 5. N500 =1Gb
#                     '''
#                 )
#                 choice=input('Enter your choice: ')
#                 print('You have successfully subscribed')
#                 exit()
#             elif choice == '2':
#                 print(
#                     '''
#                 1. N600 =1.5Gb
#                 2. N750 =2Gb
#                 3. N900 =2.5Gb
#                 4. N1000 =3.2Gb
#                 5. N1200 =4Gb
#                     '''
#                 )
#                 choice=input('Enter your choice: ')
#                 print('You have successfully subscribed')
#                 exit()
#             elif choice == '3':
#                 print(
#                     '''
#                 1. N750 = 1.2Gb+(IG/TT/YT)
#                 2. N500 =500Mb
#                 3. N800 =1Gb
#                 4. N1000 =1.5Gb
#                 5. N1500 =3.5Gb
#                     '''
#                 )
#                 choice=input('Enter your choice: ')
#                 print('You have successfully subscribed')
#                 exit()
#             elif choice == '4':
#                 print(
#                     '''
#                 1. N1500 =2GB +2GB
#                 2. N2000 =2.7GB+2GB
#                 3. N2500 =3.5GB+2GB
#                 4. N3000 =6.75GB
#                 5. N3500 =7GB+2GB
#                     '''
#                 )
#                 choice=input('Enter your choice: ')
#                 print('You have successfully subscribed')
#                 exit()
#             elif choice == '5':
#                 print(
#                         '''
#                     1. N25,000 =90GB/60DAYS
#                     2. N40000 = 150GB/60DAYS
#                     3. N90000 = 480GB/90DAYS
#                     4. N125000 = 800GB/365DAYS
#                         '''
#                     )
#                 choice=input('Enter your choice: ')
#                 print('You have successfully subscribed')
#                 exit()
#             else:
#                 print('Oops, looks like the code you used was incorrect. Please check and try again.')
#                 register()

#         elif choice =='2':
#             print(
#             '''
#             Special Offer for you! Get 700MB for N150. Data is valid for 1 day.
#         1. Activate
#         0. Back
#             '''
#         )
#             choice=input('Enter your choice: ')
#             if choice == 1:
#                 print('Activation of 700MB smart Daily at N150 was successful')
#                 exit()
#             else:
#                 register()
#         elif choice =='3':
#             print(
#             '''
#             Special Offer for you! Get 7GB for N1500. Data is valid for 1 week.
#         1. Activate
#         0. Back
#             '''
#         )
#             choice=input('Enter your choice: ')
#             if choice == 1:
#                 print('Activation of 7GB smart Daily at N1500 was successful')
#                 exit()
#             else:
#                 register()
#         elif choice =='4':
#             print(
#             '''
#         1. GistPlus - 4X
#         2. Sachet Bundles - 15K/sec
#             '''
#         )
#             choice=input('Enter your choice: ')
#             exit()
#         elif choice =='5':
#             print(
#             '''Error performing request, Kindly try again later
#             '''
#         )
#             register()
#         else:
#             print('Oops, looks like the code you used was incorrect. Please check and try again.')
#             register()
#     elif ussd == 'cancel':
#         exit()
#     else:
#         print('Ussd code is *312#')
#         register()
# register()

        


# Assignment
# shams_mass=78
# taiwo_mass=92
# shams_height=1.69
# taiwo_height=1.95
# shams_bmi=(shams_mass/shams_height)**2
# taiwo_bmi=(taiwo_mass/taiwo_height)**2
# print(shams_bmi)
# print(taiwo_bmi)
# if shams_bmi> taiwo_bmi:
#     print('Shamsudeen has an higher index')
# else:
#     print('Taiwo has an higher index')



# 7. boolean datatypes
# x=True
# y=False



# Python Operators

# 1. Arithmetic Operators

# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	
# %	    Modulus	        x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y

# x=7
# y=2
# print(x%y)

# 2. Comparison Operators
# ==,<=,>=,!=,<,>

# x=25
# y=20
# print(x!=y)


# 3. Logical Operators
    # AND, OR, NOT
    # AND= TRUE when both conditions are true 
    # OR= TRUE when atleast one condition is true

# x=25
# y=20
# z=30

# if x > y or y == z:
#     print('all condition are met')
# else:
#     print('you made a mistake no condition was met')


# A grading application

'''

student_score = int(input('Enter your score:'))

if student_score >= 70 and student_score <= 100:
    print("Grade A")
elif student_score >= 60 and student_score <= 69:
    print('Grade B')
elif student_score >= 50 and student_score <= 59:
    print('Grade C')
elif student_score >= 40 and student_score <= 49:
    print('Grade D')
elif student_score <= 39 and student_score >=0:
    print('You failed, You can do better')

else:
    print("That's not a grade score")
'''



# 4. Identity Operators
    # is, is not
# x=100
# y=100
# t= [100,200,300,400,500]
# p= [100,200,300,400,500]
# print(t is p)
# print(id(t))
# print(id(p))
# print(x is y)
# print(x is not y)



# 5. Membership Operators
        # in, not in
# balance = 100
# cart =[]
# fruits = ['guava', 'pear', 'apple','banana']
# print(f'Your available balance is {balance}')
# print(f'These are the available fruits in stock at the moment ')
# for i in fruits:
#         print(i)
# x = input('What fruit do you want to add to cart: ')
# if x in fruits:
#     print(f'{x} is available in store')
#     cart.append(x)
#     while True:
#         print(
#         '''
#         1. Make Order now
#         2. Add to cart
#         3. View cart
#         4. Exit
#         '''

#     )
#         choice = input('Enter your choice: ')
#         if choice == '1':
#             if balance <= len(cart)*30:
#                 print('Insuficient balance, Kindly Top up balance')
#                 # break
#             elif cart == []:
#                 print(' cart is empty')
#             else:
#                 balance -= len(cart)*30
#                 print(f'Order is successful.')
#                 print(f'Your available balance is {balance}')
#                 if balance<30:
#                     print('Top up balance')
#                 else:
#                     print('you can buy more')
#                 cart.clear()
#         if choice == '2':
#             cart_item=input('What fruit do you want to add to cart: ')
#             if cart_item in fruits:
#                 print(f'{cart_item} is available in store')
#                 cart.append(cart_item)
#                 print(f'Your cart is {cart}')
#             else:
#                 print(f'Your available balance is {balance}')
#                 print(f'{cart_item} is not available in store')
#                 print(f'These are the available fruits in stock ')
#                 for i in fruits:
#                     print(i)
#         if choice == '3':
#             if cart == []: 
#                 print('Your cart is empty')
#             else:
#                 print(f'This is what you have in your cart {cart}')
#                 print(
#                     '''
#                     1. Make Order now
#                     2. Add to cart
#                     '''
#                 )
#                 choice=input('Enter your choice: ')
#                 if choice=='1':
#                     # print(len(cart))
#                     if balance <= len(cart)*30:
#                         print('Insuficient balance, Kindly Top up balance')
#                         break
#                     else:
#                         balance -= len(cart)*30
#                         cart.clear()
#                         print(f'Order is successful.')
#                         print(f'Your available balance is {balance}')
#                         print('You can buy more')
#                         if balance<30:
#                             print('Top up balance')
#                         else:
#                             print('You can buy more')
#                 if choice =='2':
#                     cart_item=input('What fruit do you want to add to cart: ')
#                     if cart_item in fruits:
#                         print(f'{cart_item} is available in store')
#                         cart.append(cart_item)
#                         print(f'Your cart is {cart}')
#                     else:
#                         print(f'Your available balance is {balance}')
#                         print(f'{cart_item} is not available in store')
#                         print(f'These are the available fruits in stock ')
#                         for i in fruits:
#                             print(i)
#         if choice =='4':
#             print('Good bye see you next time')
#             exit()
    
# else:
#     print(f'{x} is not available in store')
#     print(f'These are the available fruits in stock ')
#     for i in fruits:
#         print(i)
    
        


# 6. Bitwise Operators
# & AND
# | or
# ^ XOR




# 7. Assignment Operators is used to give values to operators
#  =	x = 5	        x = 5	
# +=	x += 3	        x = x + 3	
# -=	x -= 3	        x = x - 3	
# *=	x *= 3	        x = x * 3	
# /=	x /= 3	        x = x / 3	
# %=	x %= 3	        x = x % 3	
# //=	x //= 3	        x = x // 3	
# **=	x **= 3	        x = x ** 3	
# &=	x &= 3	        x = x & 3	
# |=	x |= 3	        x = x | 3	
# ^=	x ^= 3	        x = x ^ 3	
# >>=	x >>= 3	        x = x >> 3	
# <<=	x <<= 3	        x = x << 3	
# :=	print(x := 3)	x = 3  print(x)
# y=3
# x=5
# x += 3
# print(x)
# x += y
# print(x)
# print(y)
'''

x=5
for i in range(x):
    name = input('Enter name: ')
    print(f'welcome {i+1}{name}')
print(x)
'''

# i=1
# i+=1
# while i  <= 200:
#     print('I am sorry')
# else:
#     exit()






# Operators Precedence
# Assignment
# Building a simple Calculator
# using membership operators to confirm which operator you can perform before performing any opertors


while True:
    x=int(input('What is your first input: '))
    y=int(input('What is your second input: ') )

    print(
        '''
        1. Sum Input
        2. Multiply Input
        3. Divide Input
        4. Subtract Input
        5. Modulus Input
        6. Exponential of Input
        '''
    )
    choice=input('What is your choice: ')

    if choice=='1':
        print(f'Your result is {x+y}')
    if choice=='2':
        print(f'Your result is {x*y}')
    if choice=='3':
        print(f'Your result is {x/y}')
    if choice=='4':
        print(f'Your result is {x-y}')
    if choice=='5':
        print(f'Your result is {x%y}')
    if choice=='6':
        print(f'Your result is {x**y}')




# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	
# %	    Modulus	        x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y


# Conditional statements

# if, elif, else


# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
'''


if age >= 18 and age<60:
    print('You are old enough to vote')
elif age >= 0 and age<18:
    print('You are too young')
elif age>=60:
    print('You are too old for the program')
else:
    print('Input your actual age')
'''


# Nested conditional statement
'''

if name=='Ade':
    if age >=18 and age <= 60:
        print('Welcome current James')
    elif age<18:
        print('Welcome young James')
    elif age>60:
        print('Welcome Old James')
elif name=="shams":
    if age >=18 and age <= 60:
        print('Welcome current Shams')
    elif age<18:
        print('Welcome young Shams')
    elif age>60:
        print('Welcome Old Shams')
elif name=='Taiwo':
    if age >=18 and age <= 60:
        print('Welcome current Taiwo')
    elif age<18:
        print('Welcome young Taiwo')
    elif age>60:
        print('Welcome Old Taiwo')
else: 
    print('Not a member')
    
        
'''


