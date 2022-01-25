# CA2 - x00180738 - flavio.vieira

import csv
import Lecturer as Lecturer
import Student as Student

# Module class
class Module(Lecturer.Lecturer):
    __module_id = 0
    __module_name = ''
    __course_code = ''
    __department = ''
    __student_class_list = []
    __assessment_list = []

    # Module class initializer
    def __init__(self, module_id_in='', module_name_in='Unknown', course_code_in='', department_in='Computing', name_in='', email_in='', staff_id_in=0, speciality_in='', qualifications_in=''):
        try:
            super().__init__(name_in, email_in, staff_id_in, speciality_in, qualifications_in)
            self.set_module_id(module_id_in)
            self.set_module_name(module_name_in)
            self.set_course_code(course_code_in)
            self.set_department(department_in)
            self.__student_class_list = []
            self.__assessment_list = []
        except Exception as e:
            raise Exception('Module not created.')

    # getters
    def get_module_id(self):
        return self.__module_id

    def get_module_name(self):
        return self.__module_name

    def get_course_code(self):
        return self.__course_code

    def get_department(self):
        return self.__department

    def get_lecturer_email(self):
        return self.user_email

    def get_lecturer_name(self):
        return self.user_name

    def get_lecturer_id(self):
        return self.staff_id

    def get_lecturer_speciality(self):
        return self.speciality

    def get_lecturer_qualification(self):
        return self.qualifications

    def get_student_class_list(self):
        return self.__student_class_list

    def get_assessment_list(self):
        return self.__assessment_list

    # setters
    def set_module_id(self, module_id_in):
        if module_id_in != '':
            self.__module_id = module_id_in
        else:
            raise Exception('Module id cannot be empty.')

    def set_module_name(self, module_name_in):
        if module_name_in == '':
            self.__module_name = 'Unknown'
        else:
            self.__module_name = module_name_in

    def set_course_code(self, course_code_in):
        if course_code_in != '':
            self.__course_code = course_code_in

    def set_department(self, department_in):
        if department_in in ['Computing', 'Science', 'Marketing', 'Business', 'Art']:
            self.__department = department_in
        else:
            self.__department = 'Computing'

    # auto_add_classlist Method
    def auto_add_class_list(self, file_name_in):
        # import file
        # studentClassList = []
        with open(file_name_in, "r") as file:
            student_file = csv.reader(file)
            header = next(student_file)
            for student in student_file:
                studentClassObject = Student.Student(name_in=student[1], email_in=student[0], student_number_in=student[2], programme_code_in=student[3], programme_year_in=student[4], student_type_in=student[5])
                self.__student_class_list.append(studentClassObject)

    # append_to_class_list Method
    def append_to_class_list(self, name_in='', email_in='', student_number_in='', programme_code_in='', programme_year_in='', student_type_in=''):
        studentClassObject = Student.Student(name_in, email_in, student_number_in, programme_code_in, programme_year_in, student_type_in)
        self.__student_class_list.append(studentClassObject)

    # append_to_assessment_list Method
    def append_to_assessment_list(self, assessment_to_add):
        list_to_add = []
        for row in assessment_to_add:
            list_to_add.append(row)
        self.__assessment_list.append(list_to_add)


    # 11. print_module_details() - Module class
    def print_module_details(self):
        print("************* Module Details ************")
        print("Module Id: \t\t\t\t", self.get_module_id())
        print("Module Name: \t\t\t", self.get_module_name())
        print("Course Code: \t\t\t", self.get_course_code())
        print("Department: \t\t\t", self.get_department())
        print("Lecturer email: \t\t", self.get_lecturer_email())
        print("Lecturer name: \t\t\t", self.get_lecturer_name())
        print("Lecturer staff id: \t\t", self.get_lecturer_id())
        print("Lecturer speciality: \t", self.get_lecturer_speciality())
        print("Lecturer qualifications:", self.get_lecturer_qualification())
        print("*****************************************")


# moduleTest = Module(module_id_in='456789', module_name_in='Python', course_code_in='H DIp C.S.', department_in='Computing', name_in='Flavio', email_in='flavio@email.com', staff_id_in=123456, speciality_in='Software', qualifications_in='phd')
# moduleTest.print_module_details()
# moduleTest.print_lecturer_details()
# moduleTest.print_user_details()
# print(type(moduleTest.get_student_class_list()))

# # Testing auto_add_class_list Method
# moduleTest.auto_add_class_list('students.csv')
# print(moduleTest.get_student_class_list())
# number_students = 0
# for i in moduleTest.get_student_class_list():
#     i: Student.Student
#     i.print_student_details()
#     number_students += 1
# print(number_students)

# Testing append_to_class_list Method
# moduleTest.append_to_class_list(name_in='Flavio', email_in='flavio@email.com', student_number_in='123456789', programme_code_in='H.Dip. C.S.', programme_year_in='1', student_type_in='PT')
# number_students = 0
# for i in moduleTest.get_student_class_list():
#     i: Student.Student
#     i.print_student_details()
#     number_students += 1
# print(number_students)

