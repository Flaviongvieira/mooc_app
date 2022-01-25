# CA2 - x00180738 - flavio.vieira

import User as User

# Lecturer class
class Lecturer(User.User):
    staff_id = 0
    speciality = ''
    qualifications = ''

    def __init__(self, name_in='', email_in='', staff_id_in=0, speciality_in='', qualifications_in=''):
        try:
            super().__init__(name_in, email_in)
            self.set_staff_id(staff_id_in)
            self.set_speciality(speciality_in)
            self.set_qualifications(qualifications_in)
        except Exception as e:
            raise Exception('The lecturer was not created.')

    # getters
    def get_staff_id(self):
        return self.staff_id

    def get_speciality(self):
        return self.speciality

    def get_qualifications(self):
        return self.qualifications

    # setters
    def set_staff_id(self, staff_id_in):
        if len(str(staff_id_in)) > 2 and str(
                staff_id_in).isnumeric():  # len(str(staff_id_in)) == 6 -> not used since numbers started with 0 and python removes left zeros on int
            self.staff_id = staff_id_in
        else:
            raise Exception('Staff id is incorrect.')

    def set_speciality(self, speciality_in):
        if speciality_in != '':
            self.speciality = speciality_in
        else:
            raise Exception('Speciality cannot be blank.')

    def set_qualifications(self, qualifications_in):
        if qualifications_in.lower() in ['bsc', 'ma', 'msc', 'phd']:
            self.qualifications = qualifications_in.lower()
        else:
            raise Exception('Qualifications must be bsc, ma, msc, or phd.')

    def print_lecturer_details(self):
        print("*********** Lecturer Details ************")
        print("Lecturer email: \t\t\t", self.get_user_email())
        print("Lecturer Name: \t\t\t\t", self.get_user_name())
        print("Lecturer password: \t\t\t", self.get_user_password())
        print("Lecturer registration date: ", self.get_user_date_registered())
        print("Lecturer id: \t\t\t\t", self.get_staff_id())
        print("Lecturer Speciality: \t\t", self.get_speciality())
        print("Lecturer Qualifications: \t", self.get_qualifications())
        print("*****************************************")

# lecturerTest = Lecturer(name_in='Flavio', email_in='flavio@email.com', staff_id_in=12345678, speciality_in='Comp. Science', qualifications_in='bsc')
# lecturerTest.print_lecturer_details()