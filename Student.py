# CA2 - x00180738 - flavio.vieira

import User as User


# Student class
class Student(User.User):
    student_number = ''
    programme_code = ''
    programme_year = 0
    student_type = ''
    list_of_grades = []

    def __init__(self, name_in='', email_in='', student_number_in='', programme_code_in='', programme_year_in='', student_type_in=''):
        try:
            super().__init__(name_in, email_in)
            self.set_student_number(student_number_in)
            self.set_programme_code(programme_code_in)
            self.set_programme_year(programme_year_in)
            self.set_student_type(student_type_in)
            self.list_of_grades = []
        except Exception as e:
            raise Exception('The student was not created.')

    # getters
    def get_student_number(self):
        return self.student_number

    def get_programme_code(self):
        return self.programme_code

    def get_programme_year(self):
        return self.programme_year

    def get_student_type(self):
        return self.student_type

    def get_list_of_grades(self):
        return self.list_of_grades

    # setters
    def set_student_number(self, student_number_in):
        if len(str(student_number_in)) == 9 and str(student_number_in).isnumeric():
            self.student_number = student_number_in
        else:
            raise Exception('Student number incorrect.')

    def set_programme_code(self, program_code_in):
        if program_code_in != '':
            self.programme_code = program_code_in
        else:
            raise Exception('Program code cannot be blank.')

    def set_programme_year(self, programme_year_in):
        if programme_year_in in ['1', '2', '3', '4', '5', '6']:
            self.programme_year = programme_year_in
        else:
            raise Exception('Program Year must be a numeric value between 1 and 6.')

    def set_student_type(self, student_type_in):
        if student_type_in in ['PT', 'FT']:
            self.student_type = student_type_in
        else:
            raise Exception('Student type must be a PT or FT.')

    def print_student_details(self):
        print("************ Student Details ************")
        print("Student email: \t\t\t\t", self.get_user_email())
        print("Student Name: \t\t\t\t", self.get_user_name())
        print("Student password: \t\t\t", self.get_user_password())
        print("Student registration date: \t", self.get_user_date_registered())
        print("Student number: \t\t\t", self.get_student_number())
        print("Program Code: \t\t\t\t", self.get_programme_code())
        print("Program Year: \t\t\t\t", self.get_programme_year())
        print("Student type: \t\t\t\t", self.get_student_type())
        print("*****************************************")


# studentTest = Student(name_in='Flavio', email_in='Flavio@email.com', student_number_in='123456789', programme_code_in='HDip-CS', programme_year_in='1',
#                  student_type_in='PT')
# studentTest.print_student_details()
