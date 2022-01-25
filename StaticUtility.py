# CA2 - x00180738 - flavio.vieira

# GradeCalculator @staticlass
class StaticUtility:

    @staticmethod
    def GradeCalculator(percentage_in):
        if percentage_in < 34:
            grade = 'F'
        elif 34 <= percentage_in <= 39:
            grade = 'D'
        elif 39 < percentage_in <= 49:
            grade = 'C'
        elif 49 < percentage_in <= 54:
            grade = 'C+'
        elif 54 < percentage_in <= 59:
            grade = 'B-'
        elif 59 < percentage_in <= 69:
            grade = 'B'
        elif 69 < percentage_in <= 79:
            grade = 'B+'
        else:
            grade = 'A'
        return grade

