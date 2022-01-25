# CA2 - x00180738 - flavio.vieira

# Main program

import csv
from statistics import mean

import Module as Module
import Student as Student
import StaticUtility as StaticUtility

############### Modules ###############
# import List of modules class
modulesList = []
with open('Modules.csv', "r") as file:
    modules_file = csv.reader(file)
    header = next(modules_file)
    for module in modules_file:
        modulesList.append(module)

# moduleObjectList
moduleObjectList = []
for module in modulesList:
    lecturerObject = Module.Module(module_id_in=module[0], module_name_in=module[1], course_code_in=module[2], department_in=module[3], email_in=module[4], name_in=module[5], staff_id_in=module[6], speciality_in=module[7], qualifications_in=module[8])
    moduleObjectList.append(lecturerObject)

# 1D list of modules ids
list_of_module_id = []
for modules in moduleObjectList:
    list_of_module_id.append(modules.get_module_id())



##################### APPLICATION #####################
# Application menu
def menu_options():
    print("\t***********************")
    print("\t* MOCC System Menu *")
    print("\t* 1) Add Module ")
    print("\t* 2) Add Students to Module ")
    print("\t* 3) Add Students Grades to Module ")
    print("\t* 4) Display Modules")
    print("\t* 5) Display Students ")
    print("\t* 6) Display Students Grades")
    print("\t* 7) Exit ")
    print("\t***********************")


# Option 3 - Add student grades to module - menu
def add_student_option():
    print("\t* Add student Options *")
    print("\t* 1) Add Students from file")
    print("\t* 2) Add Student manually")
    print("\t* 3) Exit ")



menu_option = 0
while menu_option != 7:

    menu_options()
    menu_option = int(input("\tPlease enter menu option: "))

    # Option 1 - Add Module
    if menu_option == 1:
        print('**************** Option 1 - Add Module ****************')
        module_id_in = input('Please enter module id: ')
        if module_id_in in list_of_module_id:
            print('Module {} already exist!'.format(module_id_in))
        else:
            module_name_in = input('Please insert the module name: ')
            course_code_in = input('Please insert the course code: ')
            department_in = input('Please insert the department: ')
            lecturer_name_in = input('Please insert the lecturer name: ')
            lecturer_email_in = input('Please insert the lecturer email: ')
            lecturer_id_in = input('Please insert the lecturer id: ')
            lecturer_speciality_in = input('Please insert the lecturer speciality: ')
            lecturer_qualification_in = input('Please insert the lecturer qualification: ')

            new_module = Module.Module(module_id_in=module_id_in, module_name_in=module_name_in, course_code_in=course_code_in, department_in=department_in,
                                       name_in=lecturer_name_in, email_in=lecturer_email_in, staff_id_in=lecturer_id_in, speciality_in=lecturer_speciality_in, qualifications_in=lecturer_qualification_in)
            moduleObjectList.append(new_module)
            list_of_module_id.append(new_module.get_module_id())
            new_module.print_module_details()


    # Option 2 - Add Students to Module
    elif menu_option == 2:
        student_add_option = 0
        print('**************** Option 2 - Add Students to Module ****************')
        module_id = input('Please enter module id: ')
        for i in moduleObjectList:
            if module_id == i.get_module_id():
                i.print_module_details()
                while student_add_option != 3:
                    add_student_option()
                    student_add_option = input('Please select an option from 1 to 3: ')
                    if not str(student_add_option).isnumeric():
                        print('Please select an option between 1 and 3!')
                    else:
                        student_add_option = int(student_add_option)
                        if student_add_option == 1:
                            file_name_in = input('Please insert the file name: ')
                            i.auto_add_class_list(file_name_in)
                            print('File {0} added successfully to {1} - {2}.'.format(file_name_in, i.get_module_name(), i.get_module_id()))

                        elif student_add_option == 2:
                            # Request student info
                            student_number_in = input('Please insert the student number: ')
                            name_in = input('Please insert the student name: ')
                            email_in = input('Please insert the student email: ')
                            programme_code_in = input('Please insert the program code: ')
                            programme_year_in = input('Please insert the program year: ')
                            student_type_in = input('Please insert the student type: ')
                            # call append_to_class_list method
                            i.append_to_class_list(name_in=name_in, email_in=email_in, student_number_in=student_number_in, programme_code_in=programme_code_in, programme_year_in=programme_year_in, student_type_in=student_type_in)
                            print('{0} - {1} has been added to {2} - {3}'.format(name_in, student_number_in, i.get_module_name(), i.get_module_id()))

                        elif student_add_option == 3:
                            print('Main menu')

                        else:
                            print('Please select an option between 1 and 3!')
        else:
            print('Module {} does not exist in the system.'.format(module_id))


    # Option 3 - Add Students Grades to Module
    elif menu_option == 3:
        print('****************  Option 3 - Add Students Grades to Module **************** ')
        module_id = input('Please enter module id: ')
        for module in moduleObjectList:
            if module_id == module.get_module_id():
                module.print_module_details()
                grades_counter = int(input('Please enter number of grades to add to {}: '.format(module.get_module_name())))
                grade_1D_list = []
                for grade in range(grades_counter):
                    student_number_op = int(input('Please enter the student number: '))
                    assessment_name_op = input('Please enter the assessment name: ')
                    percentage_achieved_op = int(input('Please insert the % achieved: '))
                    grade_op = StaticUtility.StaticUtility.GradeCalculator(percentage_achieved_op)
                    new_assessment_record = [student_number_op, assessment_name_op, percentage_achieved_op, grade_op]
                    grade_1D_list.append(new_assessment_record)
                module.append_to_assessment_list(grade_1D_list)

    # Option 4 - Display Modules
    elif menu_option == 4:
        print('**************** Option 4 - Display Modules ****************')
        # local variables to determine number of modules and students
        total_number_of_modules = 0
        total_number_of_students = 0
        computing_modules = 0
        science_modules = 0
        marketing_modules = 0
        business_modules = 0
        art_modules = 0
        # loop sequence to count number of modules and students
        for module in moduleObjectList:
            module.print_module_details()
            total_number_of_modules += 1
            for student in module.get_student_class_list():
                total_number_of_students += 1
            if module.get_department() == 'Computing':
                computing_modules += 1
            elif module.get_department() == 'Science':
                science_modules += 1
            elif module.get_department() == 'Marketing':
                marketing_modules += 1
            elif module.get_department() == 'Business':
                business_modules += 1
            elif module.get_department() == 'Art':
                art_modules += 1
        # print results
        print('The total number of modules is : {}'.format(total_number_of_modules))
        print('The total number of students is : {}'.format(total_number_of_students))
        print('The total number of modules in Computing Department : {}'.format(computing_modules))
        print('The total number of modules in Science Department : {}'.format(science_modules))
        print('The total number of modules in Business Department : {}'.format(business_modules))
        print('The total number of modules in Marketing Department : {}'.format(marketing_modules))
        print('The total number of modules in Art Department : {}'.format(art_modules))


    # Option 5 - Display Students in specified module
    elif menu_option == 5:
        print('**************** Option 5 - Display Students ****************')
        module_id = input('Please enter module id: ')
        # check if module exists
        if module_id not in list_of_module_id:
            print('Module {} does not exist in the system.'.format(module_id))
        else:
            for module in moduleObjectList:
                if module_id == module.get_module_id():
                    number_of_students_module = 0
                    module.print_module_details()
                    for student in module.get_student_class_list():
                        student: Student.Student
                        student.print_student_details()
                        number_of_students_module += 1
                    print('The total number of students in {} is: {}'.format(module.get_module_name(), number_of_students_module))

    # Option 6 - Display Students Grades
    elif menu_option == 6:
        print('**************** Option 6 - Display Students Grades ****************')
        module_id = input('Please enter module id: ')
        # check if module exists
        if module_id not in list_of_module_id:
            print('Module {} does not exist in the system.'.format(module_id))
        else:
            # local variables for summary display
            a = 0
            bPlus = 0
            b = 0
            bMinus = 0
            cPlus = 0
            c = 0
            cMinus = 0
            d = 0
            f = 0
            # total_number_of_grades = a + bPlus + bMinus + cPlus + c + cMinus + d + f

            # loop through modules list until find correct module
            for module in moduleObjectList:
                if module_id == module.get_module_id():
                    module.print_module_details()
                    module_grades_list = []
                    # print header
                    print("{0:<20}".format("Student number") + "{0:<20}".format("Assessment name") + "{0:<20}".format("% achieved") + "{0:<20}".format("Grade"))
                    for grade in module.get_assessment_list():
                        for line in grade:
                            # print student grade details
                            print("{0:<20}".format(line[0]) + "{0:<20}".format(line[1]) + "{0:<20}".format(line[2]) + "{0:<20}".format(line[3]))

                            # create list of all grades
                            module_grades_list.append(line[2])

                            # check grade and increase correct counter
                            if line[3] == 'A':
                                a += 1
                            elif line[3] == 'B+':
                                bPlus += 1
                            elif line[3] == 'B':
                                b += 1
                            elif line[3] == 'B-':
                                bMinus += 1
                            elif line[3] == 'C+':
                                cPlus += 1
                            elif line[3] == 'C':
                                c += 1
                            elif line[3] == 'C-':
                                cMinus += 1
                            elif line[3] == 'D':
                                d += 1
                            elif line[3] == 'F':
                                f += 1

                    # display summary of numbers per each grade
                    print('*' * 50)
                    print('Total: {0}'.format(len(module_grades_list)))
                    print("Highest: {0}".format(max(module_grades_list)))
                    print("Lowest: {0}".format(min(module_grades_list)))
                    print("Average: {0}".format(round(mean(module_grades_list), 2)))
                    print('*'*50)
                    print("A: \t{0}".format(a))
                    print("B+: {0}".format(bPlus))
                    print('B: \t{0}'.format(b))
                    print("B-: {0}".format(bMinus))
                    print("C+: {0}".format(cPlus))
                    print("C: \t{0}".format(c))
                    print("C-: {0}".format(cMinus))
                    print("D: \t{0}".format(d))
                    print("F: \t{0}".format(f))
                    print('*' * 50)


    # Option 7 - Exit App
    elif menu_option == 7:
        print('Thanks for using the app!')
        # save modules file
        with open("Modules.csv", "w", newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(['ModuleId', 'ModuleName', 'CourseCode', 'Department', 'Lecturer_Email', 'Lecturer_Name', 'Lecturer_StaffId', 'Lecturer_Speciality', 'Lecturer_Qualification'])
            for new_module in moduleObjectList:
                writer.writerow([new_module.get_module_id(), new_module.get_module_name(), new_module.get_course_code(),
                                 new_module.get_department(), new_module.get_lecturer_email(),
                                 new_module.get_lecturer_name(), new_module.get_lecturer_id(),
                                 new_module.get_lecturer_speciality(), new_module.get_lecturer_qualification()])

    else:
        print("Error - Please select an option between 1 and 7.")