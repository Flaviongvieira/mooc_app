# CA2 - x00180738 - flavio.vieira

import random
import string
import datetime as dt


# User class
class User:
    user_email = ''
    user_password = ''
    user_name = ''
    user_date_registered = ''
    number_of_users = 0

    def __init__(self, name_in='', email_in=''):
        try:
            self.set_user_name(name_in)
            self.set_user_email(email_in)
            self.set_user_password()
            self.set_user_date_registered()
            User.number_of_users += 1
        except Exception as e:
            raise Exception('The user was not created.')

    # getters
    def get_user_name(self):
        return self.user_name

    def get_user_email(self):
        return self.user_email

    def get_user_password(self):
        return self.user_password

    def get_user_date_registered(self):
        return self.user_date_registered

    # setters
    def set_user_email(self, email_in):
        if email_in.__contains__('@') and len(email_in) > 6 and email_in.endswith('.com'):
            if email_in.index('@') < email_in.index('.com'):
                self.user_email = email_in
        else:
            raise Exception('Email inserted is not in the correct format.')

    def set_user_name(self, name_in):
        if name_in != '':
            self.user_name = name_in
        else:
            raise Exception('User name cannot be blank!')

    def set_user_password(self):
        self.user_password = ''.join(random.choice(string.ascii_letters) for i in range(6))

    def set_user_date_registered(self):
        self.user_date_registered = dt.datetime.today()

    # print user details
    def print_user_details(self):
        print("*****************************************")
        print("************* User Details **************")
        print("User email: \t\t\t", self.get_user_email())
        print("User Name: \t\t\t\t", self.get_user_name())
        print("User password: \t\t\t", self.get_user_password())
        print("User registration date: ", self.get_user_date_registered())
        print("*****************************************")


# userTest = User('Flavio', 'flavio@email.com')
# userTest.print_user_details()