import random
import datetime
import re


class cbtback():
    __school_name = None
    def __init__(self, school_name):
        self.__school_name = school_name
        self.user=[]
        self.questioncse=[]
        self.questioncve=[]
        self.questioneee=[]
        self.result=[]
        self.exam=[]

    def create_questions(self, questions, option_a, option_b, option_c, answers,deptque):
        new_question = {
            'question': questions,
            'option': [
                option_a,
                option_b,
                option_c
            ],
            'answer': answers,
        }
        if deptque=='CSE':
            self.questioncse.append(new_question)
            return{
                    'status':True,
                    'message_cse':'Question successfully added to CSE question bank',
                    'csebank':self.questioncse,
                }
        if deptque=='CVE':
            self.questioncve.append(new_question)
            return{
                    'status':True,
                    'cvebank':self.questioncve,
                    'message_cve':'Question successfully added to CVE question bank',
                }
        if deptque=='EEE':
            self.questioneee.append(new_question)
            return{
                    'status':True,
                    'eeebank':self.questioneee,
                    'message_eee':'Question successfully added to EEE question bank'
                }
        return{
            'status':False,
            'message': 'There are only CSE,CVE and EEE department at the moment, Kindly try again'
        }
    def view_questions(self,deptque):
        if deptque=='CSE':
            return{
                    'status':True,
                    'message_cse':'Here is your CSE Question Bank',
                    'csebank':self.questioncse
                }
        if deptque=='CVE':
            return{
                    'status':True,
                    'cvebank':self.questioncve,
                    'message_cve':'Here is your CVE Question Bank'
                }
        if deptque=='EEE':
            return{
                    'status':True,
                    'eeebank':self.questioneee,
                    'message_eee':'Here is your EEE Question Bank'
                }
        return{
            'status':False,
            'message': 'There are only CSE,CVE and EEE department at the moment, Kindly try again'
        }
    def editted_question(self,questions, option_a, option_b,option_c, answers,deptque, choice):
        new_question = {
            'question': questions,
            'option': [
                option_a,
                option_b,
                option_c
            ],
            'answer': answers,
        }
        if deptque=='CSE':
                self.questioncse[choice-1] = new_question
                return {
                'csebank':self.questioncse,
                'status': True,
                'message': 'Question editted successfully'
            }
        if deptque=='CVE':
                self.questioncve[choice-1] = new_question
                return {
                'cvebank':self.questioncve,
                'status': True,
                'message': 'Question editted successfully'
            }
        if deptque=='EEE':
                self.questioneee[choice-1] = new_question
                return {
                'eeebank':self.questioneee,
                'status': True,
                'message': 'Question editted successfully'
            }
        return{
            'status':False,
            'message': 'An error occured. There are only CSE,CVE and EEE department at the moment, Kindly try again'
        }
    def delete_question(self,deptque, choice):
        if deptque=='CSE':
                self.questioncse.pop(choice-1)
                return {
                'csebank':self.questioncse,
                'status': True,
                'message': 'Question deleted successfully'
            }
        if deptque=='CVE':
                self.questioncve.pop(choice-1)
                return {
                'cvebank':self.questioncve,
                'status': True,
                'message': 'Question deleted successfully'
            }
        if deptque=='EEE':
                self.questioneee.pop(choice-1)
                return {
                'eeebank':self.questioneee,
                'status': True,
                'message': 'Question deleted successfully'
            }
        return{
            'status':False,
            'message': 'An error occured. There are only CSE,CVE and EEE department at the moment, Kindly try again'
        }

    def get_school_name(self):
        return self.__school_name
    

    def register_user(self, email, fullname, password, confirm_password, role, id,department):
        if password != confirm_password:
            return {
                'status': False,
                'message': 'Password not match'
            }
        # if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        #     return {
        #     'status': False,
        #     'message': 'Invalid email format'
        # }
        # if len(fullname.strip().split()) != 2:
        #     return {
        #     'status': False,
        #     'message': 'Fullname must contain exactly two names'
        # }
        if role!='student' and role!='staff' and role!='admin':
            return {
                'status': False,
                'message': 'Role can only be student/staff'
            }
        if department!='CSE' and department!='CVE' and department!='EEE':
            return {
                'status': False,
                'message': 'Only CSE/CVE/EEE departments exist at the moment'
            }
        # if len(password) < 6:
        #     return {
        #     'status': False,
        #     'message': 'Password must be at least 6 characters long'
        # }


        for user in self.user:
            if user['email'] == email:
                return {
                'status': False,
                'message': 'Email already exist'
                }
        new_user = {
            'id': id,
            'email' : email,
            'fullname': fullname,
            'password' : password,
            'role' : role.lower(),
            'department'  : department.upper()
        }
        self.user.append(new_user)
        return{
                'status': True,
                'role': role,
                'message_student': f'Account created successfully, Your matric number is  {new_user['id']}',
                'message_staff': f'Account created successfully, Your staff id is  {new_user['id']}'
        }
    def login_user(self,email,password):
        for user in self.user:
            if user['email']==email and user['password']==password:
                return{
                    'status': True,
                    'data': user,
                    'message': 'Login successful',
                    'login_message': f'Welcome here, {user['fullname']}, Your Id number is {user['id']}'}
        else:
            return{
                'status': False,
                'message': 'Invalid credentials'
                }
    def view_user(self):
            return{
                'data':self.user
            }
    