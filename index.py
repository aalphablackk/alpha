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


# while True:
#     x=int(input('What is your first input: '))
#     y=int(input('What is your second input: ') )

#     print(
#         '''
#         1. Sum Input
#         2. Multiply Input
#         3. Divide Input
#         4. Subtract Input
#         5. Modulus Input
#         6. Exponential of Input
#         '''
#     )
#     choice=input('What is your choice: ')

#     if choice=='1':
#         print(f'Your result of ({x} + {y}) = {x+y}')
#     if choice=='2':
#         print(f'Your result of ({x} * {y}) = {x*y}')
#     if choice=='3':
#         print(f'Your result of ({x}/{y}) = {x/y}')
#     if choice=='4':
#         print(f'Your result of ({x} - {y}) = {x-y}')
#     if choice=='5':
#         print(f'Your result of ({x} % {y}) = {x%y}')
#     if choice=='6':
#         print(f'Your result of ({x}^{y}) = {x**y}')


'''

x=int(input('Input your number to check for even/odd: '))
if x%2==0:
    print('This is an even number')
elif x%2==1:
    print('This is an odd number')
'''




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

''

# Learning about zeller congrugence
# d=1
# m=11
# y=69
# k=69
# j=19
# while True:
#     months =[
#         ('January', 31, 1),
#         ('February', 28, 2),
#         ('March', 31, 3),
#         ('April', 30, 4),
#         ('May', 31, 5),
#         ('June', 30, 6),
#         ('July', 31, 7),
#         ('August', 31, 8),
#         ('September', 30, 9),
#         ('October', 31, 10),
#         ('November', 30, 11),
#         ('December', 31, 12)
# ]

#     i=[]
#     for month in months:
#         month_name = month[0]
#         last_day_of_the_month = month[1]
#         month_no= month[2]
#         # print(month_name)
#         # print(last_day_of_the_month)
#         # print(f'{month_name} has {last_day_of_the_month} months ')
#         # print(month_no)
#     y=list(input('Input the year: '))
#     m=int(input('input the month: '))
#     d=int(input('Input the day: '))  
#     k=int(y[2]+y[3])
#     if m in month_no and d<=last_day_of_the_month:
#         print(m)
#         print(d)
#         yy=int(y[0]+y[1]+y[2]+y[3])
#         # if int(y)%4==0 and m==2:
#         #     last_day_of_the_month+=1
#         #     pass
#         # else:
#         #     continue
#         pass
#     else: 
#         print('Kindly input the right month and day')
#         continue    



#     # i.append(y)
#     j=int(y[0]+y[1])

#     if m == 1:
#         k-=1
#         m+=12
#         # print(m)
#     if m == 2:
#         k-=1
#         m+=12
#     day=(f'{int((d+(13*(m+1)//5)+k+(k//4)+5-j)%7)}')
#     testday=(f'{int((d+(13*(m+1)//5)+k+(k//4)+(j//4)-2*j)%7)}')
#     # print(str(day))
#     # print(f'{str(testday)} test')
#     if m == 13:
#         m-=12
#         # print(m)
#     if m == 14:
#         m-=12
#     if day == '0':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Sunday')
#     elif day == '1':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Monday')
#     elif day == '2':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Tuesday')
#     elif day == '3':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Wednesday')
#     elif day == '4':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Thursday')
#     elif day == '5':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Friday')
#     elif day == '6':
#         print(f'{d}/{m}/{y[0]+y[1]+y[2]+y[3]} is Saturday')

# print(d)
# print(m)
# print(k)
# print13(j)


# print(f'{int(z+k)}')
'''



# Loops
# For, while, while True

# Loops are inbuilt module on python that are used for iteration.{like a cycle }

# x='strings'
# for i in x:
#     print(i)

# fruits=['pawpaw','melon','pear','cherry','guava',4,4.4]
# for i in fruits:
#     if i == 'cherry':
#         break
#     print(type(i))
#     # print(i)


# for i in range(130):
#     if i == 0:
#         continue
#     print(f'Multiplication table {i}')
#     for j in range(130):
#         print(f'{i} x {j} = {i*j}')


# WHILE
# Works with conditional statement

# i=4
# while i > 0:
#     i *= 10
#     print(i)

# i = 0
# while i < 10:
#     i += 1
#     print(i)


'''
# Movie Ticket

# 
'''


# Betting system
# balance=100
# namee={}
# agee={}
# nameee={}
# while True:
#     name=input('Input your name: ')
#     age=int(input('Input your age: '))
#     agee.update(namee)
#     if age < 18 and age >=0:
#         print('You are too young to bet')
#         nameee[f'{name}']= f'{age}'
#         agee.update(nameee)
#         continue
#     else:
#         pass
#     namee[f'{name}']= f'{age}'


#     print (
#         '''
#         1. Continue
#         2. Login as another user
#         3. View User
#         '''
#     )
#     choice=(input('What is your choice: '))
#     if choice == '1':
#         print(f'Welcome {name}')
#         pass
#     if choice == '2':
#         continue
#     if choice == '3':   
#         d=(len(namee))
#         print(f'Registered Users: {d}')        
#         for x, y in namee.items():
#             print(f'User: {x}    Age: {y}')
#         e=(len(nameee))
#         print(f'Underage Users: {e}')        
#         for x, y in nameee.items():
#             print(f'User: {x}    Age: {y}')
#         print(f'Total Users: {d+e}')        
#         continue
#     while balance>=20:
#         import random
#         x=int(random.randint(1,5))
#         print(f'Your balance is {balance}')
#         print('Type exit to cancel')
#         y=int(input('Guess your number between 1-5: '))
#         if y > 5 or y < 0:
#             print('Your guessed number should be between 1-5. Try again')
#             continue
#         if y == x:
#             print(f'You guessed right. The right answer is {x}')
#             balance +=20
#             print(f'Your new balance is {balance} ')
#         elif y == int():
#             print('You have to guess a number')
#             continue        
#         else:
#             print(f'Your guess is wrong. The right answer is {x}' )
#             balance -=20
#             print(f'Your new balance is {balance} ')
#     else:
#         print('Insufficient balance kindly top up your balance')
#         continue


# Python collections and Array
# Sequence datatypes
# List

# color =['red','white','brown','purple','yellow']
# print(type(color))
# print(color[0])
# color[0]='pink'
# print(color)
# print(color[0:3])
# color[0:2]='green','blue'
# color[0:2]=['green','blue'] 

# print(color)

# list methods
# color.append('rede') adds to index[-1]
# color.clear() empties the list but still a list
# x=color.copy() duplicates the list in a specified variable
# print(color.count('white'))
# color.extend(['red','feff'])
# color.index('red')
# color.insert(1, 'blue')
# color.pop(0)
# color.remove('red')
# color.reverse()
# color.sort
# print(color)
# print(x)


# String functions

# x='STRINGS, {}'
# print(x.capitalize())
# print(x.upper())
# print(x.lower())
# print(x.casefold())
# print(x.center(100))
# print(x.count('S'))
# print(list[x.encode])
# print(x.endswith('S'))
# print(x.format('alpha'))




# 27/04/2026
# Calender

# months =[
#     ('January', 31),
#     ('February', 28),
#     ('March', 31),
#     ('April', 30),
#     ('May', 31),
#     ('June', 30),
#     ('July', 31),
#     ('August', 31),
#     ('September', 30),
#     ('October', 31),
#     ('November', 30),
#     ('December', 31)
# ]


# days_of_the_week =['Sun','Mon','Tue','Wed','Thur','Fri','Sat']

# year = 2026

# for month in range(12):
#     month_name = months[month][0]
#     last_day_of_the_month = months[month][1]
#     print(f'{month_name} {year}'.center(20))
#     # print(f'{days_of_the_week}')
#     print(' '.join(days_of_the_week).center(30))

#     y=2026
#     m= month + 1
#     if m < 3:
#         m += 12
#         y -= 1
#         # print(y)
#     # print(y)
#     k=y %  100
#     j=y // 100
#     # print(k)
#     # print(j)

#     h=(1+(13*(m+1))//5 + k +(k//4) + (j//4) + 5*j) % 7
#     # print(h)
#     start_day =(h+6)%7
#     # print(start_day)

#     for _ in range(start_day):
#         # print(_)
#         print('    ', end='')
#     day =1
#     while day<= last_day_of_the_month:
#         print(f'{day:4}', end='')
#         start_day +=1
#         if start_day % 7==0:
#             print()
#         day += 1
#     print()
     



# Tuple
# x=('James',54,'true', 'James')
# print(type(x))
# print(x(-1))
# print(x)
# y=x.__add__(tuple['wale'])
# print(y)
# ordered, accept duplicates, unchanged
# print(x.count('James'))
# print(x.index('James'))


# scores ={
#     'Maths':50,
#     'english': 55,
#     'chemistry': 60,
#     'colors':['red','white'],
#     'english': 50
# }

# print(type(scores))
# print(scores)
# print(len(scores))
# scores['agric']=40

# print(scores.get('Maths'))
# print(scores)
# print(scores.keys())


# cbt application
# registration
# questions and answer
# view result

# Question = ['Who is the president of Nigeria', 
#             'whats the name of the instructor',
#             'if 2x=4, find x', 
#             'what is the best car brand?'
#             ]

# Answer=[
#     'Jagaban',
#     'Isreal',
#     '2',
#     'Tesla'
# ]
# user=[]
# # scores=''
# final_result={}
# for i in range(2):
#     name = input('Enter your name mr man: ')
#     print(f'welcome {name}, baba answer your question')
#     user_ready = input('are you ready to take your test: yes/no ?:')
#     score=0
#     if user_ready  == 'yes':
#         for each_question, each_answer in zip(Question, Answer):
#             print(each_question)
#             user_ans = input('Enter your ans ')
#             if user_ans.capitalize().strip() == each_answer.capitalize():
#                 score+=1
#                 print('correct')
#             else:
#                 print('wrong')
#         percent=score/len(Question)*100
#         # print(f'Hi, {name} Your percentage score is {percent}%')
#         # user.append(name)
#         # scores.append(score)

#         final_result={
#             'name':name,
#             'percent':percent
#         }
#         pass
#         user.append(final_result)
#         # print(f'The final results are:')
#         for r in user:
#             print(f'{r['name']} your score is {r['percent']}')
#             percent=r['percent']
#             if percent >= 70 and percent <= 100:
#                 print("Grade A")
#             elif percent >= 60 and percent <= 69:
#                 print('Grade B')
#             elif percent >= 50 and percent <= 59:
#                 print('Grade C')
#             elif percent >= 40 and percent <= 49:
#                 print('Grade D')
#             elif percent <= 39 and percent >=0:
#                 print('You failed, You can do better')





  
    # print(f'{Question[0]}')
    # user_ans = input('Enter your ans')
    # if user_ans == Answer[0]:
    #     print('You are right')



    # Assignment
    # To do list  add view edit delete
# totask=[]
# while True:
#     print(
#         '''
#     Welcome to your To Do list 
#         1. Add
#         2. Delete
#         3. view
#         4. Edit
#         '''   
#         )
#     choice=input('What is your choice: ')
#     if choice=='1':
#         todo=input('What task do you want to add: ')
#         time=input('what is the time am/pm: ')
#         todolist={
#         'todo':todo,
#         'time':time
#         }
#         totask.append(todolist)
#         print(totask)
#         continue
#     elif choice=='2':
#         print('Here are your To do list'.center(30))
#         i=1
#         for r in totask:
#             print(f'({i}). You need to {r['todo']} by {r['time']}'.center(10))
#             i+=1
#         choice=int(input('What is your choice: '))
#         if choice=='1':
#             totask.pop(0)
#         else:
#             choice-=1
#             totask.pop(choice)
#         continue
#     elif choice=='3':
#         print('Here are your To do list'.center(30))
#         i=1
#         for r in totask:
#             print(f'({i}). You need to {r['todo']} by {r['time']}'.center(10))
#             i+=1
#             # choice=int(input('Kindly input 1 to go back: '))
#             # continue
#     elif choice=='4':
#         print('Here are your To do list'.center(30))
#         i=1
#         for r in totask:
#             print(f'({i}). You need to {r['todo']} by {r['time']}'.center(10))
#             i+=1
#         choice=int(input('What task would you like to edit: '))
#         if choice=='1':
#             todo=input('What task do you want to change to: ')
#             time=input('what is the time you want to change to am/pm: ')
#             print('Task changed successfully')
#             print(f' You need to {r['todo']} by {r['time']}'.center(10))
#             taskk={
#                 'todo':todo,
#                 'time':time
#             }
#             totask[0]=taskk
#             # totask.append(todolist)
#         else:
#             choice-=1
#             todo=input('What task do you want to add: ')
#             time=input('what is the time am/pm: ')
#             taskk={
#             'todo':todo,
#             'time':time
#         }
#             totask[choice]=taskk
#             # print(f' You need to {r['todo[choice]']} by {r['time[choice]']}'.center(10))
#         continue


# 29/04/2026

# Dictionary Methods

# details ={
#     'name': 'Olaiya',
#     'department':'Datascience',
#     'course':'python',
#     'address': {
#         'area':'Ogooluwa',
#         'street': 'Gof Junction'
#     }
# }
# print(type(details))
# print(details['name'])
# print(details['address'])
# details['name']='alpha black'
# print(details)
# print(details['address']['area'])
# details['address']['area']='owode'
# details.clear()
# y=details.copy()
# print(y)
# print(details.fromkeys(['name'],'wale'))
# print(details)
# print(details.get('name'))
# print(details.items())
# print(details.keys())
# print(details.values())
# details.pop('name')
# print(details.popitem())
# details.update({'side_hustle':'jamojamo'})
# print(details)


# for i, j in details.items():
#     print(i,    j)
# for i, j in enumerate(details.items(), start=1):
#     print(f'{i}. {j[0]}: {j[1]}')


# Cbt application using dictionary

# registration
# questions and answer
# view result

# Question = {'Who is the president of Nigeria': 'Jagaban',
#             'whats the name of the instructor': 'Isreal',
#             'if 2x=4, find x': '2', 
#             'what is the best car brand?':'Tesla'
# }

# user=[]
# # scores=''
# final_result={}
# for i in range(3):
#     name = input('Enter your name mr man: ')
#     print(f'welcome {name}, baba answer your question')
#     user_ready = input('are you ready to take your test: yes/no ?:')
#     score=0
#     if user_ready  == 'yes':
#         for i, j in Question.items():
#             print(i)
#             user_ans = input('Enter your ans ')
#             if user_ans.capitalize().strip() == j:
#                 score+=1
#                 print('correct')
#             else:
#                 print('wrong')
#         percent=score/len(Question)*100
#         # print(f'Hi, {name} Your percentage score is {percent}%')
#         # user.append(name)
#         # scores.append(score)

#         final_result={
#             'name':name,
#             'percent':percent
#         }
#         pass
#         user.append(final_result)
#     else:
#         continue
#     print(f'The final results are:')
#     user.sort(key=lambda x: x['percent'], reverse=True)
#     for r in user:
#         print(f'{r['name']} your score is {r['percent']}')
#         percent=r['percent']
#         if percent >= 70 and percent <= 100:
#             print("Grade A")
#         elif percent >= 60 and percent <= 69:
#             print('Grade B')
#         elif percent >= 50 and percent <= 59:
#             print('Grade C')
#         elif percent >= 40 and percent <= 49:
#             print('Grade D')
#         elif percent <= 39 and percent >=0:
#             print('You failed, You can do better')


    # In Python, lambda is used to create small, anonymous functions (functions without a name).



# Set

# sets = {1,2,3,4,3}
# fruits ={'apple','tomato','pear','watermelon'}
# print(type(sets))
# print(fruits)
# print(sets)
# assignment 1
# Verify the reason why it seems set are ordered for int and not for strings


# set1={2,3,4,5,6,7,9}
# set2 = {2,4,6,8}
# set3 ={2}
# set1.add(2)
# print(set1.difference(set2))
# set1.difference_update(set2)
# set1.discard(2)
# set1.remove(2)
# print(set1.intersection(set2))
# set1.intersection_update(set2)
# print(set1.isdisjoint(set2))
# print(set1.issubset(set2))
# print(set1.issuperset(set3))
# print(set1.pop())
# print(set1.symmetric_difference(set2))
# print(set1.union(set2))
# set1.update(set2)
# set1.update(['apple',False,True])
# print(set1)
# print(set1)
# print(set1)


# binary datatypes
# memoryview
# bytearray

# b = bytearray([83,104,97,109,115])
# print(b[0])
# b[0] = 55
# print(ord('D'))
# print(chr(83))
# print(chr(b[0]))
# b_memory = memoryview(b)
# print(b_memory)
# print(b)




# python function
# parametised and unparametized functions

# def my_name(name):
#     print(f'my name is {name}')
# my_name('shams')


5/5/2026
# Assignment read up on functions
'''
A function is a block of code which only runs when it is called.
it has to be called to get an output
A function helps avoid code repetition.

A function can return data as a result.



Function Names
Function names follow the same rules as variable names in Python:

A function name must start with a letter or underscore
A function name can only contain letters, numbers, and underscores
Function names are case-sensitive (myFunction and myfunction are different)
It's good practice to use descriptive names that explain what the function does.



'''

# inch =4
# cm=inch*2.54
# print(cm)
# inch=5
# cm=inch*2.54
# print(cm)

# def inch_to_cm():
#   inch=int(input('How many inch: '))
#   print(inch*2.54)
# inch_to_cm()
# inch_to_cm()
# inch_to_cm()
# inch_to_cm()

# Functions is used to avoid repititions

# def my_greetings():
    # return 'Have a nice day'
# print(my_greetings())
# message=my_greetings()
# print(message)

# my_greetings='have a nice day'
# print(my_greetings)

# Functions can send data back to the code that called them using the return statement.

# Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement.

# def function():
#     pass


# Function arguements
# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the actual value that is sent to the function when it is called.

# def my_function(name): # name is a parameter
    # print(name + ' Python')
# my_function('Shams') # "Shams" is an argument
# my_function('Taiwo')
# my_function('Isreal')



# By default, a function must be called with the correct number of arguments.

# If your function expects 2 arguments, you must call it with exactly 2 arguments. If you call it with incorrect numbers of arguments you will get an error.



# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Shams", "Taiwo")



# Default parameter value


# def my_function(name= 'Sir/ma'): # name is a parameter
#     print('Dear ' + name + ' Welcome to Python')
# my_function('Shams') # "Shams" is an argument
# my_function('Taiwo')
# my_function('Isreal')
# my_function()


# Keyword Arguments


# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)

# my_function(name = "Buddy",animal = "dog" ) # This way, with keyword arguments, the order of the arguments does not matter.
# my_function("Buddy","dog") # Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.


# You can mix positional and keyword arguments in a function call but positional arguments must come before keyword arguments.

# def my_function(animal, name, age):
#   print("I have a", age, "year old", animal, "named", name)
# my_function("dog", age = 5, name = "Buddy")

# For functions you can have different data types such as list, dict,
# List
# def my_function(fruits):
#     for fruit in fruits:
#         print(fruit)
# my_fruits = ["apple", "banana", "cherry"]
# my_function(my_fruits)


# Dictionary
# def my_functions(person):
#   print('Name:' + person['name'])
#   print('age:' + person['age'])

# my_person= {'name':' james', 'age' : ' 36'}
# my_functions(my_person)


# Return values

# def my_function(x,y):
#     return x - y
# result=my_function(5,3)
# print(result)
# print(my_function(5,3))
# print(my_function(y=5,x=3))


# Also it can return any data types
# list
# def my_function():
#   return ["apple", "banana", "cherry"]

# fruits = my_function()
# print(fruits)
# print(my_function())
# print(fruits[1])
# print(fruits[2])
# Tuple
# Unpacking items inside a function
# def my_function():
#   return (10, 20, 30)

# x,*y = my_function()
# print("x:", x)
# print("y:", y)
# print(y[1])


# Only positional arguement  ,/
# def my_function(name, /): 
#     print(name + " " )

# my_function("Shams")


# we can only have a positional arguement else there will be an error

# my_function("Emil")
# Only keyword arguement *,
# we can only have a keyword arguement else there will be an error
# def my_function(*, name):
#     print(name)
# my_function('Emil')



# Combining Positional-Only and Keyword-Only
# Arguments before / are positional-only, and arguments after * are keyword-only

# def my_function(a, b, /, *, c, d): # i.e a and b will be positional arguement while c and d will be keyword arguement. 
    # return a + b + c + d
# print(my_function(5, 10, c=15, d=30))

# What makes you a better programmer is how much you can maximized your code



# Functions 
# Global and Local variable

# y=20
# def add():
#     global x
#     x=5
#     # y=10
#     print(x+y)
# add()
# def sub():
#     # x=30
#     print(x-y)
# sub()


# def deposit(amount, balance):
#     global new_balance
#     new_balance = balance+amount
#     print(f'Dear user your balance is {new_balance}')
# deposit(1000, 100)
# deposit(1000, new_balance)
# def withdrawal(amount, new_balance):
#     new_balance-= amount
#     print(f'Dear user your balance is {new_balance}')
# withdrawal(500, new_balance)





# 6/5/2026
# ARGS AND KWARGS

# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept an unknown number of arguments.

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add an * before the parameter name.
# def my_function(*kids):
#   print("The youngest child is " + kids[0:1])

# my_function("Emil", "Tobias", "Linus")
# my_function("Emil", "Tobias", "Linus")

# parameter allows a function to accept any number of positional arguments then the args becomes a tuple containing all the passed arguments.
# def my_function(*args):
#   print("Type:", type(args))
#   print("First argument:", args[0])
#   print("Second argument:", args[1])
#   print("All arguments:", args)

# my_function("Emil", "Tobias", "Linus")

# Using *args with Regular Parameters
# You can combine regular parameters with *args.
# Note: Regular parameters must come before *args
# read,*greetings, name=('Hello','Ade','shams','Taiwo','James')
# print(greetings)

# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)
#     print(type(name))

# my_function("Hello", "Emil", "Tobias", "Linus")


# An example
# def total_no(*number):
#     for num in number:
#         total=0
#         total+=num
#         print(total)
#     return total
# print(total_no(1,2,3))


# Maximum number
# def my_function(*numbers):
#   if len(numbers) == 0:
#     return None
#   max_num = numbers[1]
#   print(max_num)
#   for num in numbers:
#     if num > max_num:
#       max_num = num
#   return max_num

# print(my_function(3, 7, 2, 9, 1))



# **Kwargs-- Arbitrary Keyword Arguments
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the items accordingly

# def my_function(**kid):
#   print("His last name is " + kid["lname"] +" and first name is "+ kid["fname"])
#   print(type(kid))

# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(fname, lname):
#   print("His last name is " + lname +" and first name is "+ fname)

# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(**details):
#   print("Type:", type(details))
#   print("Name:", details["name"])
#   print("Age:", details["age"])
#   print("City:", details["city"])
#   print("All data:", details)

# my_function(name = "Tobias", age = 30, city = "Bergen")

# You can combine regular parameters with **kwargs but regular parameters must come before **kwargs
# def my_function(username, **details):
#   print("Username:", username)
#   print("Additional details:")
# #   for key, value in details.items():
#     # print("   ", key + ":", value)
#   print(details)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")



# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.
# However, the order must be:
# regular parameters
# *args
# **kwargs

# def my_function(title, *args, **kwargs):
#   print("Title:", title)
#   print("Positional arguments:", args[1])
#   print("Keyword arguments:", kwargs['city'])

# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


# Unpacking a list
# def my_function(a, b, c):
#   return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers) # Same as: my_function(1, 2, 3)
# print(result)


# Unpacking a Dict

# def my_function(fname, lname):
#   print("Hello", fname, lname)

# person = {"fname": "Emil", "lname": "Refsnes"}
# my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

# So basically the Use of * and ** in function definitions is to collect arguments i.e if we don't know the number of arguements we want to have in comparison to the parameters given, and also to use them in function calls to unpack arguments.


# More on Functions

# Bank app

# bankapp with function
# register
#   email
#   fullname
#   account no
#   address
#   phone number
#   account_balance
#   password 
#   balance
# login
    # Email 
    # password
# dashboard
# Withdrawal
# Deposit
# Transaction history
# check balance


# json javascripts object notation
# w = create,
# r = read
# .dumps
# .loads
# r-raw strings
# import json
# import os
# import pandas as pd
# if os.path.exists('Bank_db.json'):
#     print('file exists')
#     file = pd.read_json(r'')
#     print(file)
# # os.mkdir('noname')
# # with open('Bank_db.json','w') as f:
# #     json.dump([], f)

# from random import randint
# Bank_db = []
# # for i in range(2):
# def Get_database():
#     if os.path.exists('Bank_db.json'):
#         with open('Bank_db.json', 'r') as file:
#             json.load(file)
#     else:
#         with open('Bank_db.json','w') as file:
#             json.dump([],file)
#         return[]
# def save_db(db):
#     db = Get_database()



# def register():
#     print("Welcome fill the details below")
#     email = input("Enter your email: ")
#     fullname = input("Enter your fullname:")
#     account_number=randint(0000000000, 9999999999)
#     address = input("Enter your address: ")
#     phone_number = input("Enter your phone number: ")
#     account_balance = 0.0
#     password =input("Enter your password: ")
#     confirm_password = input("Confirm your password: ")
#     if password != confirm_password:
#         print("Password do not match")
#         register()
#     for i in range(len(Bank_db)):
#         if Bank_db[i]["email"] == email:
#             print(i)
#             print("Email already exist, try login instead")
#             register()
#     user_details={
#     "email": email,
#     "fullname": fullname,
#     "account_number": account_number,
#     "address": address,
#     "phone_number": phone_number,
#     "account_balance": account_balance,
#     "password": password,
#     "Status": False,
#     "is_admin": False,
#     }
#     Bank_db. append (user_details)
#     print(f"Registration successful, your account number is {account_number}")
#     login()
# def login():
#     print("Welcome back, please login to your account")
#     email = input("Enter your email: ")
#     password= input("Enter your password: ") 
#     for i in range(len(Bank_db)):
#         print (i)
#         if Bank_db[i]["email"] == email and Bank_db[i]["password"] == password:
#             print(f'Login successful, welcome {Bank_db[i]["fullname"]}')
#             Bank_db[i]["Status"] = True
#             print(Bank_db[i])
#             dashboard()
#             break
#         elif Bank_db[i]["email"] != email or Bank_db[i]["password"] != password:
#             print("Invalid details")
#             Home()
#         # elif Bank_db[i]['email'] not in Bank_db:
#         #     print("Email not found, please register") 
#         #     login()
# def dashboard():
#     pass

# def Home():
#     print(
#         '''
#         1. Register
#         2. Login
#         3. Exit
#         '''
#     )
#     choice=input('Enter choice: ')
#     if choice=='1':
#         register()
#     elif choice=='2':
#         login()
#     elif choice=='3':
#         print('THANKS FOR BANKING WITH US!!!')
#         exit()
#     else:
#         print('Invalid input')
#         Home()
# Home()


# Assignment TASK MANAGEMENT SYSTEM
# 1. add,view,edit,delete
# add alarm, add 10 min snooze, 
# from datetime import time as t
# Difference btw json arguments load and loads, dump and dumps 
# For Monday== scheduler, threading, 


# import mod
# x=mod.yoo('Alpha')
# import mod as you
# x=you.yoo('Alpha')
# print(x)
# print(dir(mod))

# import datetime
# x=datetime.datetime.now()
# # print(x.year)
# print(x.strftime('%A'))
# print(x)



