from lmsconfig import lmsconfig
import random


class lmsapp(lmsconfig):
    def __init__(self, school_name):
        super().__init__(school_name)
        self.home()

    def home(self):
        print(
            '''
            1. Register
            2. login
            3. exit

            '''
        )

        choice= input('Enter choice: ')
        if choice == '1':
            self.register()
        elif choice == '2':
            self.login()
        elif choice == '3':
            exit()

    def register(self):
        email = input('Enter mail: ')
        fullname = input('Enter fullname: ')
        role= input(
                    '''
                    Enter role(Student/ Staff):
                    ''')
        password = input('Enter password: ')
        confirm_password = input('Enter confirm password: ')
        id = random.randint(111111, 999999)

        result = self.create_account (email, fullname, password, confirm_password, role, id)

        if result['status']:
            if result['role'] == 'student':
                print (result['message_student'])
            elif result['role'] == 'staff':
                print(result['message_staff'])
        else:
            print(result['message'])
        
        self.home()
    



    def login(self):
        email = input('Enter mail: ')
        password = input('Enter password: ')
        result = self.login_user (email,password)
        if result['status']:
            print(result['message_success'])
        else:
            print(result['message'])

        # result = self.login_user(email, password)
        # # print(result)
        # if result['status'] == True:
        #     user = result['data']
        #     print(result['message'])
        #     if user['role'] == 'student':
        #         self.student_dashboard(user)
        #     elif user['role'] == 'staff':
        #         self.staff_dashboard(user)
        # else: 
        #     print(result['message'])
        self.home()
    
    # def student_dashboard(self, user):
    #     # print(user)

    #     print('''
    #     1. Take exams
    #     2. View results
    #     3. View details
    #     4. Log out
    #         ''')
        
    #     choice = input('Enter your choice: ')

    #     if choice == '1':
    #         self.take_exams(user)
    #     elif choice == '2':
    #         self.view_result(user)
    #     elif choice == '3':
    #         self.view_details(user)
    #     elif choice == '4':
    #         self.home()

    # def take_exams(self, user):
    #     exam = self.generate_exams()
    #     responsee=[]
    #     print(f'There are {len(self.question)} questions, Answer All ')
    #     if not exam['status']:
    #         print(exam['message'])
    #     score=0
    #     for i in exam['question']:
    #         print(f'{i['question']} {i['option']} ')
    #         response= input('Enter your ans ')
    #         responsee.append(response)
    #         if response.capitalize().strip() == i['answer'].capitalize().strip():
    #             score+=1
    #             # print('correct')
    #         # else:
    #             # print('wrong')
    #     percent=score/len(self.question)*100
    #     print(user['fullname'])
    #     print(percent)
    #     if percent >= 70 and percent <= 100:
    #         grade="Grade A"
    #     elif percent >= 60 and percent <= 69:
    #         grade='Grade B'
    #     elif percent >= 50 and percent <= 59:
    #         grade='Grade C'
    #     elif percent >= 40 and percent <= 49:
    #         grade='Grade D'
    #     elif percent <= 39 and percent >=0:
    #         grade=('You failed, You can do better')
    #     final_result={
    #         'fullname': user['fullname'],
    #         'id': user['id'],
    #         'percent':percent,
    #         'grade': grade,
    #         'response': responsee
    #     }
    #     self.result.append(final_result)
    #     self.save_results()
    #     self.student_dashboard(user)

    # def view_result(self,user):
    #     for i in self.result:
    #         if i['fullname'] == user['fullname']:
    #             for s,y in i.items():
    #                 if s == 'response':
    #                     continue
    #                 print(s,':',y)
    #         else:
    #             print('No result yet, Kindly take the exam')
    #     self.student_dashboard(user)
    #             # print(type(user['fullname']))
    #             # print(type(i['fullname']))
    # def view_details(self,user):
    #     for i,y in user.items():
    #         if i == 'password':
    #             continue
    #         print(i,':', y)
    #     self.student_dashboard(user)


    #     # print(exam['question'])
            
    # def staff_dashboard(self,user):
    #     print(
    #         '''
    #         1. Add question
    #         2. View question
    #         3. Delete question
    #         4. Edit question
    #         5. View student result
    #         6. Logout
    #         '''
    #     )

    #     choice = input('Enter your choice: ')

    #     if choice == '1':
    #         self.Add_question(user)
    #     elif choice == '2':
    #         self.View_question(user)
    #     elif choice == '3':
    #         self.Del_question(user)
    #     elif choice == '4':
    #         self.Edit_question(user)
    #     elif choice == '5':
    #         self.student_result(user)
    #     elif choice == '6':
    #         print('Thanks for serving your student')
    #         self.home()

    # def Add_question(self, user):
    #     print(f'Welcome {user['fullname']}')
    #     questions = input('Enter question: ')
    #     option_a = input('Enter option A: ')
    #     option_b = input('Enter option B: ')
    #     option_c = input('Enter option C: ')
    #     answers = input('Enter answer: ')

    #     result = self.create_questions(questions, option_a, option_b,option_c, answers)

    #     if result['status']:
    #         print(result['message'])
    #     self.staff_dashboard(user)

    # def View_question(self, user):
    #     i=1
    #     for re in self.question:
    #         print(f'({i}). Questions: {re['question']} '.center(10))
    #         print(f'Options: {re['option'] }')
    #         i+=1
    #     self.staff_dashboard(user)

    # def Del_question(self, user):
    #     i=1
    #     # print(self.question)
    #     for re in self.question:
    #         # print(re)
    #         print(f'({i}). Questions: {re['question']} '.center(10))
    #         print(f'Options: {re['option'] }')
    #         i+=1
    #     choice=int(input('What is your choice: '))
    #     if choice=='1':
    #         self.question.pop(0)
    #     else:
    #         choice-=1
    #         self.question.pop(choice)
    #         self.save_questions()
    #     self.staff_dashboard(user)
    
    # def Edit_question(self, user):
    #     i=1
    #     for re in self.question:
    #         print(f'({i}). Questions: {re['question']} '.center(10))
    #         print(f'Options: {re['option'] }')
    #         i+=1
    #     choice=int(input('Which Question would you like to edit: '))
    #     questions = input('Enter question: ')
    #     option_a = input('Enter option A: ')
    #     option_b = input('Enter option B: ')
    #     option_c = input('Enter option C: ')
    #     answers = input('Enter answer: ')
    #     result = self.edited_questions(questions, option_a, option_b,option_c, answers, choice)
    #     if result['status']:
    #         print(result['message'])
    #     self.staff_dashboard(user)

    # def student_result(self,user):
    #     check_student=int(input('Kindly input the student ID: '))
    #     for i in self.result:
    #         if check_student == int(i['id']):
    #             for s,y in i.items():
    #                 if s == 'response':
    #                     continue
    #                 print(s,':',y)
    #             self.staff_dashboard(user)
    #     else:
    #             print('No result yet')
    #     self.staff_dashboard(user)

        






lms = lmsapp('Sqi_Academy')
























































# from lmsconfig import lmsconfig
# import random
# class lmsapp(lmsconfig):
#     def __init__(self, lmsname, lmspass):
#         super().__init__(lmsname, lmspass)
#         self.home()
#     def home(self):
#         print(
#             f''' 
#             Welcome to the {self.lms_name}
#             1. Signup 
#             2. Signin
#             3. exit

#             '''
#         )
#         choice=input('What is your choice: ')
#         if choice=='1':
#             self.signup()
#         if choice=='2':
#             pass
#         if choice=='3':
#             exit()
#     def signup(self):
#         email=input('Input your email: ')
#         fullname=input('Input your fullname: ')
#         password=input('Input your password: ')
#         confirmpassword=input('Input your confirm password: ')
#         level=input('Input your level: ')
#         department=input('Input your department: ')
#         course=input('Input your course: ')
#         course=input('Input your course: ')
#         matricno= random.randint(111111,999999)
#         role= input('''
#                     1. Teacher
#                     2. Student
#                     What is your role: 
#                     ''')
        
#         result = self.createaccount(email, password, confirmpassword, role, fullname, department, course, matricno, level)
#         if result :
#             print(result['message'])
#         else:
#             print(result['message'])
# lms=lmsapp('sqi', 1234)



