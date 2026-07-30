import mysql.connector as sql
try:
    conn = sql.connect(
        host = '127.0.0.1',
        port = '3306',
        user = 'root',
        database = 'alpha_cbt',
        password = ''
    )

    conn.autocommit = True
    mycursor = conn.cursor(dictionary=True)
except Exception as e:
    print(e)
else:
    print('Database connection successful')

import json
import datetime
import random

class lmsconfig:
    __school_name = None 

    def __init__(self, school_name):
        self.__school_name = school_name

    def get_schoolname(self):
        return self.__school_name


    def create_account(self, email, fullname, password, confirm_password,role, id):
        if password!= confirm_password:
            return{
                'status': False,
                'message': 'password not match'
            }
        # query= 'SELECT *FROM users'
        # mycursor.execute(query)
        # users= mycursor.fetchall()
        # for user in users:
        #     if user['email'] == email:
        #         return {
        #         'status': False,
        #         'message': 'Email already exist'
        #         }
        try:
            query = 'INSERT INTO users(email,fullname,password,id,role) VALUES(%s,%s,%s,%s,%s)'
            value = (email,fullname,password,id,role)
            mycursor.execute(query,value)
            return{
                    'status': True,
                    'role': role,
                    'message_student': f'Account created successfully, Your matric number is  {id}',
                    'message_staff': f'Account created successfully, Your staff id is  {id}',
            }
        except sql.errors.IntegrityError as e:
            return{
                'status': False,
                'message':'email already exist'
            }
        except Exception as e:
            return{
                'status': False,
                'message': str(e)

            }
        


    def login_user(self,email,password):
        try:
            query= 'SELECT *FROM users where email=%s'
            values = (email,)
            mycursor.execute(query,values)
            resul= mycursor.fetchone()
            # print(resul)
            if resul:
                return{
                    'status': True,
                    'message_success': 'Login Successful',
                    'data':resul
                }
            return{
                'status': False,
                'message': 'Invalid Credentials',
            }

        except Exception as e:
            return{
                'status': False,
                'message': str(e)
            }
    
    def generate_exams(self):
        query= 'SELECT *FROM questions'
        mycursor.execute(query)
        data=mycursor.fetchall()

        if len(data) == 0:
            return {
                'status': False,
                'message': 'No question Available You can not take the more than once'
            }
        shuffled_quest = data
        random.shuffle(shuffled_quest)
        for i in shuffled_quest:
            print(i)
            print(i['question'])
                    

        return {
            'status': True,
            'question': shuffled_quest,
            'Time': 30,
            'data':data
        }

    def create_questions(self,question,option_a,option_b,option_c,answer):
        try:
            query = 'INSERT INTO questions(question,option_a,option_b,option_c,answer) VALUES(%s,%s,%s,%s,%s)'
            value = (question,option_a,option_b,option_c,answer)
            mycursor.execute(query,value)
            return{
                    'status': True,
                    'message': f'Questions added succesfully'
            }
        except sql.errors.IntegrityError as e:
            return{
                'status': False,
                'message':'Questions not added. Please try again'
            }
        except Exception as e:
            return{
                'status': False,
                'message': str(e)
            }
    def marke_question(self):
        


# ASSIGNMENT
# 1. Generate all questions by id
# 2. Create result table

        # for user in self.user:
        #     if user['email']== email and user['password'] ==password:
        #         return {
        #             'status': True,
        #             'message': f'Welcome {user['fullname']}',
        #             'data': user
        #         }
        # return {
        #     'status': False,
        #     'message': f'Invalid details'
        # }    
        # print(email)

            
        # new_user = {
        #     'id': random.randint(100000, 999999),
        #     'email' : email,
        #     'fullname': fullname,
        #     'password' : password,
        #     'role' : role.lower()
        # }



        # self.user.append(new_user)
        # self.save_users()