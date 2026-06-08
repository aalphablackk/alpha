import json
import datetime
import random


class lmsconfig:
    __school_name = None

    def __init__(self, school_name):
        self.__school_name = school_name

        self.users_file = 'users.json'
        self.questions_file = 'questions.json'
        self.results_file = 'results.json'

        self.user = []
        self.question = []
        self.result = []

        self.load_users()
        self.load_questions()
        self.load_results()

    def load_users(self):
        try:
            with open(self.users_file, 'r') as file:
                self.user = json.load(file)
        except FileNotFoundError:
            self.user = []

    def load_questions(self):
        try:
            with open(self.questions_file, 'r') as file:
                self.question = json.load(file)
        except FileNotFoundError:
            self.question = []

    def load_results(self):
        try:
            with open(self.results_file, 'r') as file:
                self.result = json.load(file)
        except FileNotFoundError:
            self.result = []

    def save_users(self):
        with open(self.users_file, 'w') as file:
            json.dump(self.user, file, indent=4)

    def save_questions(self):
        with open(self.questions_file, 'w') as file:
            json.dump(self.question, file, indent=4)

    def save_results(self):
        with open(self.results_file, 'w') as file:
            json.dump(self.result, file, indent=4)

    def get_schoolname(self):
        return self.__school_name

    def create_account(self, email, fullname, password, confirm_password, role):
        if password != confirm_password:
            return {
                'status': False,
                'message': 'password not match'
            }
        for user in self.user:
            if user['email'] == email:
                return {
                    'status': False,
                    'message': 'Email already exist'
                }

        new_user = {
            'id': random.randint(100000, 999999),
            'email': email,
            'fullname': fullname,
            'password': password,
            'role': role.lower()
        }

        self.user.append(new_user)
        self.save_users()
        return {



            'status': True,
            'role': role,
            'message_student': f'Account created successfully, Your matric number is  {new_user['id']}',
            'message_staff': f'Account created successfully, Your staff id is  {new_user['id']}',
        }

    def login_user(self, email, password):
        for user in self.user:
            if user['email'] == email and user['password'] == password:
                return {
                    'status': True,
                    'message': f'Welcome {user['fullname']}',
                    'data': user
                }
        return {
            'status': False,
            'message': f'Invalid details'
        }

    def generate_exams(self):
        if len(self.question) == 0:
            return {
                'status': False,
                'message': 'No question Available You can not take the more than once'
            }
        shuffled_quest = self.question.copy()
        random.shuffle(shuffled_quest)

        return {
            'status': True,
            'question': shuffled_quest,
            'Time': 30,
        }

    def create_questions(self, questions, option_a, option_b, option_c, answers):
        new_question = {
            'question': questions,
            'option': [
                option_a,
                option_b,
                option_c
            ],
            'answer': answers
        }

        self.question.append(new_question)
        self.save_questions()

        return {
            'status': True,
            'message': 'Question added successfully'
        }

    def edited_questions(self, questions, option_a, option_b, option_c, answers, choice):
        new_question = {
            'question': questions,
            'option': [
                option_a,
                option_b,
                option_c
            ],
            'answer': answers
        }
        if choice == '1':
            self.question[0] = new_question
        else:
            choice -= 1
            self.question[choice] = new_question
        self.save_questions()
        return {
            'status': True,
            'message': 'Question editted successfully'
        }

    # load result
    # save result
    # submit exam

    # LMS- Learning Management System
# Database Schema

# Users, question , result

# Backend

# Create account
    # Fullname, email, password, id, role
# Login
    # email, password, forgot password


# Frontend
# Register

# Login
    # Students Dashboard
        # take tests view results
    # Staff Dashboard
        # view Add delete edit question
    # Admin Dashboard
        # view add delete user, results


# Modules
    # Import time , import json and import random


# class lmsconfig:
#     __students=[]
#     def __init__(self, lmsname, lmspass):
#         self.lms_name = lmsname
#         self.lms_pass = lmspass

#     def createaccount(self, email, password, confirmpassword, role, fullname, department, course, matricno, level):
#         for user in self.__students:
#             if email == user['email']:
#                 return{
#                     'Status':False,
#                     'message':'Email already exists'
#                 }
#         if password!= confirmpassword:
#             return{
#                 'Status':False,
#                 'message':'Password do not match'
#             }
#         new_student={
#             'email' : email,
#             'password': password,
#             'role': role,
#             'fullname': fullname,
#             'department': department,
#             'course': course,
#             'matricno':matricno,
#             'level':level
#         }
#         self.__students.append(new_student)

#         return{
#             'Status': True,
#             'message': f'Registration successful, Your Matric number is {matricno}'
#         }
