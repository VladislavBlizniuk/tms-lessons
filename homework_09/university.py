from student import Student
students = [
    Student('ivan', 7),
    Student('Petr', 8),
    Student('Vika', 9)
]


def calc_sum_scholarship():
    sum_of_scholarships = students[0].get_scholarship()

    for i in students[1:]:
        sum_of_scholarships += i.get_scholarship()
    return sum_of_scholarships

def get_excellent_student_count():
    counter = 0
    for i in students:
        if i.is_excellent() is True:
            counter += 1
        return counter