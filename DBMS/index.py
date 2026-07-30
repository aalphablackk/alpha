# print('Mysql imported succefully')
import mysql.connector as sql

conn = sql.connect(
    host = '127.0.0.1',
    port = '3306',
    user = 'root',
    database = 'alpha_cbt',
    password = ''
)

conn.autocommit = True
# mycursor = conn.cursor()
mycursor = conn.cursor(dictionary=True)

print('Database connection successful')

# query = "DROP DATABASE alpha_cbt"
# query = "CREATE DATABASE alpha_cbt"
# query =  """CREATE TABLE user(
# user_id INT AUTO_INCREMENT PRIMARY KEY,
# id VARCHAR(6) UNIQUE,
# email VARCHAR(50) UNIQUE,
# fullname VARCHAR(50),
# role VARCHAR(20),
# phone VARCHAR(11),
# password VARCHAR(50)
# query =  """CREATE TABLE questions(
# question TEXT UNIQUE,
# option_a TEXT,
# option_b TEXT,
# option_c TEXT,
# answer TEXT
# )"""
query =  """
CREATE TABLE results(
id INT AUTO_INCREMENT PRIMARY KEY,
fullname VARCHAR(50) NOT NULL,
student_id VARCHAR(6) NOT NULL,
subject VARCHAR(50),
percent VARCHAR(50),
grade VARCHAR(1) NOT NULL,
time_submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

FOREIGN KEY(id)
REFERENCES users(user_id)
ON DELETE CASCADE
)"""
mycursor.execute(query)
# query = "DROP TABLE user"
# query = "ALTER TABLE users ADD DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
# query = "ALTER TABLE users CHANGE DATE registered_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
# query = "ALTER TABLE users CHANGE phone phone_number VARCHAR(50)"
# query = "ALTER TABLE users ADD address VARCHAR(50) AFTER phone_number"
# query = "ALTER TABLE users ADD column next_kin VARCHAR(50) AFTER phone_number"
# query = "alter table users ADD column confirm_password VARCHAR(50) AFTER password"
# query = "ALTER TABLE users drop confirm_password"
# query = "INSERT INTO users(id, email, fullname, role, password) VALUES(%s, %s, %s, %s, %s)"
# values = ('212121', 'james@gmail.com', 'james shams', 'student', '1234')
# conn.commit()

# mycursor.execute(query, values)

# query = 'UPDATE  users SET fullname=%s where user_id=%s'
# values = ('shams James', 3)
# mycursor.execute(query, values)

# query = 'DELETE users where id=%s'

# import random
# def home(): 
#     print('''
#         1. Register
#         2. Login
#         3. Edit profile
#         4. Delete Profile
#         5. search profile
#         6. View All
#         7. exit
#         ''')
#     choice= input('What is your choice: ')
#     if choice == '1':
#         register()
#     if choice == '2':
#         login()
#     if choice == '3':
#         edit_profile()
#     if choice == '4':
#         delete_profile()
#     if choice == '5':
#         search_profile()
#     if choice == '6':
#         view_all()
#     if choice == '7':
#         exit()

# def login():
#         email= input('Input mail: ')
#         password= input('input password: ')
      
        
#         try:
#             query = 'SELECT *FROM users where email=%s'
#             values = (email,)
#             mycursor.execute(query, values)
#             result= mycursor.fetchone()
#             if result:
#                 print("Login successful")
#             # for user in result:              # print(user)
#         except Exception as e:
#             print("Invalid credentials")
#         # print('Email already exist')
#             # print(user['2'])
#             home()

    
        
# def register():
#         email= input('Input mail: ')
#         name= input ('Input name: ')
#         password= input('input password: ')
#         password= input('input password: ')
#         id = random.randint(111111, 999999)
#         role= input('student/staff: ')
#         query = "INSERT INTO users(id, email, fullname, role, password) VALUES(%s, %s, %s, %s, %s)"
#         values = (id, email, name, role, password)
#         mycursor.execute(query, values)
#         home()
# def edit_profile():
#     try:
#         email= input('Input your registered mail: ')
#         name= input ('Input name: ')
#         password= input('input password: ')
#         query = 'UPDATE  users SET fullname=%s, password=%s where email=%s'
#         values = (name,password, email)
#         mycursor.execute(query, values)
#     except Exception as e:
#         print('Email already exist')
#         home()
# def delete_profile():
#      value= input('Input your id: ')
#      query = 'DELETE FROM users where user_id=%s'
#      values = (value,)
#      mycursor.execute(query, values)
#      home()
# def search_profile():
#      value= input('Input your email: ')
#      query = 'SELECT *FROM users where email=%s'
#      values = (value,)
#      mycursor.execute(query, values)
#      result= mycursor.fetchone()
#      print(result)
#      home()

# def view_all():
#     try:
#         query = 'SELECT email,id, user_id FROM users'
#         mycursor.execute(query)
#         result =mycursor.fetchall()
#         for user in result:
#              print(user)
#     except Exception as e:
#         print(e)
#     home()    
# home()


# Presentation on all the types of errors 
# Types of error.
# err

# Assignment
    #  Research on Enumerate(role, for role in query)

# SQL QUERIES 

    # Data definition Language      DDL
        # create alter(changing what has been created, add to the column) drop(deletes the whole table) truncate(deletes the content of the table)
    # Data Manipulation Language    DML
        # Insert(to input) update(changes the content of the table) delete
    # Data query Language           DQL
        # select(gets from the database)

# CRUD operation 
    # Create  w-write x- create
    # Read    r-read
    # Update  a-append
    # Delete  
















# Database Management
# Xampp
# x- cross platform
# a - Apache
# m- Mysql
# p- perl
# p- php

# Three tier Architecture- Every application has these:

    # Database
        # Relational dbms- are structured in a way that they are presented in rows and columns.
            # SQL- structured Query Language - 
                #  Table relationships
                    # one to one relationship - 
                    # one to many relationship
                    # many to many relationship
                #  Foreign keys and references
                #   on-delete and cascade
        # Non- relational dbms
    # Backend
    # Frontend


# for installing sql---pip install mysql_connector


