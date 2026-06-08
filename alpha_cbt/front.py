from back import cbtback
import random

class cbtfront(cbtback):
    def __init__(self, school_name):
        super().__init__(school_name)
        self.home()


    def home(self):
        print(
            '''
            1. Register
            2. Login
            3. View
            4. exit
            '''
        )

        choice= input('Enter choice: ')
        if choice == '1':
            self.register()
        elif choice == '2':
            self.login()
        elif choice == '3':
            self.view()
        elif choice == '###':
            self.admin_page()
        elif choice == '4':
            exit()
        
        
            
        # ==============REGISTER DASHBOARD=============
    

    def register(self):
        email=input('Input your mail: ')
        fullname = input('Enter fullname: ').capitalize()
        role= input(
                    '''
                    Enter role(Student/ Staff):
                    ''').lower()
        department= input('What department are you? CSE/CVE/EEE: ').upper()
        password = input('Enter password: ')
        confirm_password = input('Enter confirm password: ')
        id= random.randint(111111,999999)
        link= self.register_user(email, fullname, password, confirm_password, role, id,department)
        if link['status']:
            if link['role'] == 'student':
                print (link['message_student'])
            elif link['role'] == 'staff':
                print(link['message_staff'])
        else:
            print(link['message'])
        self.home()

        # ==============LOGIN DASHBOARD=============


    def login(self):
        email=input('Input your mail: ')
        password = input('Enter password: ')
        link = self.login_user(email,password)
        try:
            if link['status']:
                user=link['data']
                print(link['message'])
                print(link['login_message'])
                if user['role']=='student':
                    self.student_dashboard(user)
                elif user['role']=='staff':
                    self.staff_dashboard(user)
            # else:
            #     print(link['message'])
            #     self.home()
        except Exception as e:
            print(e)
            print('Kindly register before signing in if you are new')
            self.home()



    def view(self):
        try:
            link=self.view_user()
            print(f"{'Id':<10}{'Email':<25}{'Fullname':<20}{'Role':<15}{'Department':<20}")
            print("-" * 90)
            for user in link['data']:
                print(f"{user['id']:<10}{user['email']:<25}{user['fullname']:<20}{user['role']:<15}{user['department']:<20}")
        except Exception as e:
            print('No registered Users yet')
            print(e)
        self.home()


        # ==============STUDENT DASHBOARD=============
    def student_dashboard(self,user):
        try:
            print(
                '''
                1.  Take Exam
                2.  View Result
                3.  View Details
                4.  Logout
                '''
            )
            choice=input('What do you wish to do: ')
            if choice == '1':
                pass
            if choice == '2':
                pass
            if choice == '3':
                pass
            if choice == '4':
                self.home(user)
        except Exception as e:
            print(e)
            print('An error occured')

        # ==============STAFF DASHBOARD=============

    def staff_dashboard(self,user):
        try:
            print(
                '''
                1. Manage Exams
                2. Manage Students
                3. Log out()
                '''
            )

            choice=input('What do you wish to do: ')
            if choice == '1':
                print(
                    '''
                    1. Update Exam questions
                    2. View Exam questions
                    3. Edit Exam questions
                    4. Delete Exam questions
                    5. Go back
                    '''
                )
                choice=input('What do you wish to do: ')
                if choice=='1':
                    self.update_exam(user)
                if choice == '2':
                    self.view_question(user)
                if choice == '3':
                    self.edit_question(user)
                if choice == '4':
                    self.delete_exam(user) 
                if choice == '5':
                    self.staff_dashboard(user)
            if choice == '2':
                print(
                    '''
                    1. View student result
                    2. View student Profile
                    3. Go back
                    '''
                )
                choice=input('What do you wish to do: ')
                if choice == '1':
                    pass
                if choice == '2':
                    pass
                if choice == '3':
                    self.staff_dashboard(user)

            if choice == '3':
                self.home()
        except Exception as e:
            print(e)
            print('An error occured')

    



    def update_exam(self,user):
                deptque= input('Which department question bank do you want to update CSE/CVE/EEE: ').upper()
                print(f'Welcome {user['fullname']}, Id: {user['id']}')
                questions = input('Enter question: ')
                option_a = input('Enter option A: ')
                option_b = input('Enter option B: ')
                option_c = input('Enter option C: ')
                answers = input('Enter answer: ')

                link = self.create_questions(questions, option_a, option_b,option_c, answers,deptque)

                if link['status']:
                    if deptque=='CSE':
                        print(link['message_cse'])
                        # print(link['csebank'])
                    elif deptque=='CVE':
                        print(link['message_cve'])
                        # print(link['cvebank'])
                    elif deptque=='EEE':
                        print(link['message_eee'])
                        # print(link['eeebank'])
                else:
                        print(link['message'])
                self.staff_dashboard(user)
                

    def view_question(self,user):
        deptque= input('Which department questiobank do you want to view (CSE/CVE/EEE): ').upper()
        link = self.view_questions(deptque)
        if deptque == 'CSE':
            # print(link['message_cse'])
            for q in link['csebank']:
                print(f"Q: {q['question']}")
                print(f"Options: {q['option']}")
                print(f"Answer: {q['answer']}")
                print("-" * 40)
        elif deptque == 'CVE':
            # print(link['message_cve'])
            for q in link['cvebank']:
                print(f"Q: {q['question']}")
                print(f"Options: {q['option']}")
                print(f"Answer: {q['answer']}")
                print("-" * 40)
        elif deptque == 'EEE':
            # print(link['message_eee'])
            for q in link['eeebank']:
                print(f"Q: {q['question']}")
                print(f"Options: {q['option']}")
                print(f"Answer: {q['answer']}")
                print("-" * 40)
        self.staff_dashboard(user)


    def edit_question(self,user):
                # try:
                    deptque= input('Which department question bank do you want to edit (CSE/CVE/EEE): ').upper()
                    link = self.view_questions(deptque)
                    print(link['csebank'])
                    i=1
                    if deptque=='CSE':
                            for re in link['csebank']:
                                print(f'({i}). Questions: {re['question']} '.center(10))
                                print(f'Options: {re['option'] }')
                                i+=1
                            choice=int(input('Which Question would you like to edit: '))
                            questions = input('Enter question: ')
                            option_a = input('Enter option A: ')
                            option_b = input('Enter option B: ')
                            option_c = input('Enter option C: ')
                            answers = input('Enter answer: ')
                            linkedit = self.editted_question(questions, option_a, option_b,option_c, answers,deptque,choice)
                            # if link['status']:
                            print(linkedit['message'])
                            self.staff_dashboard(user)
                    elif deptque=='CVE':
                            for re in link['cvebank']:
                                print(f'({i}). Questions: {re['question']} '.center(10))
                                print(f'Options: {re['option'] }')
                                i+=1
                            choice=int(input('Which Question would you like to edit: '))
                            questions = input('Enter question: ')
                            option_a = input('Enter option A: ')
                            option_b = input('Enter option B: ')
                            option_c = input('Enter option C: ')
                            answers = input('Enter answer: ')
                            linkedit = self.editted_question(questions, option_a, option_b,option_c, answers,deptque,choice)
                            # if link['status']:
                            print(linkedit['message'])
                            self.staff_dashboard(user)
                    elif deptque=='EEE':
                            for re in link['eeebank']:
                                print(f'({i}). Questions: {re['question']} '.center(10))
                                print(f'Options: {re['option'] }')
                                i+=1
                            choice=int(input('Which Question would you like to edit: '))
                            questions = input('Enter question: ')
                            option_a = input('Enter option A: ')
                            option_b = input('Enter option B: ')
                            option_c = input('Enter option C: ')
                            answers = input('Enter answer: ')
                            linkedit = self.editted_question(questions, option_a, option_b,option_c, answers,deptque,choice)
                            # if link['status']:
                            print(linkedit['message'])
                            self.staff_dashboard(user)
                    else:
                        print(['message'])          
                    self.staff_dashboard(user)
                # except Exception as e:
                #     print(e)
                #     print('An error occured')
                #     self.staff_dashboard(user)
    def delete_exam(self,user):
        # try:
                    deptque= input('Which department question bank do you want to delete (CSE/CVE/EEE): ').upper()
                    link = self.view_questions(deptque)
                    # print(link['csebank'])
                    if deptque=='CSE':
                            for i,re in enumerate (link['csebank'], start=1):
                                print(f'({i}). Questions: {re['question']} ')
                                print(f'Options: {re['option'] }')
                            choice=int(input('Which Question would you like to delete: '))
                            linkedit = self.delete_question(deptque,choice)
                            print(linkedit['message'])
                    elif deptque=='CVE':
                            for i,re in enumerate (link['cvebank'],start=1):
                                print(f'({i}). Questions: {re['question']} ')
                                print(f'Options: {re['option'] }')
                            choice=int(input('Which Question would you like to delete: '))
                            linkedit = self.delete_question(deptque,choice)
                            print(linkedit['message'])
                    elif deptque=='EEE':
                            for i,re in enumerate (link['eeebank'],start=1):
                                print(f'({i}). Questions: {re['question']} '.center(10))
                                print(f'Options: {re['option'] }')
                            choice=int(input('Which Question would you like to delete: '))
                            linkedit = self.delete_question(deptque,choice)
                            print(linkedit['message'])
                    else:
                        print(['message'])          
                    self.staff_dashboard(user)
        # except Exception as e:
        #             print(e)
        #             print('An error occured')
        #             self.staff_dashboard(user)
                



        # ==============ADMIN DASHBOARD=============


    def admin_page(self):
            choice= input('Go back home: ')
            if choice=='###':
                self.admin_dashboard()
            else:
                self.home()

    def admin_dashboard(self):
        print('Welcome Admin page')
        print(
            '''
            1. Manage Users
            2. Manage Exams
            3. Track pass/fail
            4. Exit()
            '''
        )

        choice=input('What do you wish to do: ')
        if choice == '1':
            print(
                '''
                1. Add users
                2. View users
                3. Edit users
                4. Delete users
                5. Go back
                '''
            )
            choice=input('What do you wish to do: ')
            if choice == '1':
                pass
            if choice == '2':
                pass
            if choice == '3':
                pass
            if choice == '4':
                pass
            if choice == '5':
                self.admin_dashboard()

        if choice == '2':
            print(
                '''
                1. Add exams
                2. View exams
                3. Edit exams
                4. Delete exams
                5. Go back
                '''
            )
            choice=input('What do you wish to do: ')
            if choice == '1':
                pass
            if choice == '2':
                pass
            if choice == '3':
                pass
            if choice == '4':
                pass
            if choice == '5':
                self.admin_dashboard()

        if choice == '3':
            pass
        if choice == '4':
            self.home()
        

alpha = cbtfront('Alpha_Academy')

