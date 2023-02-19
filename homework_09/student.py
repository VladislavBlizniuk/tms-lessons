class Student:
    def __init__(self, ful_name, agerage_mark):
        self.full_name = ful_name
        self.agerage_mark = agerage_mark


    def get_scholarship(self):
        if self.agerage_mark < 6:
            return 60
        elif 6 <= self.agerage_mark < 8:
            return 80
        elif self.agerage_mark >= 8:
            return 100

    def is_excellent(self):
        return self.agerage_mark >= 9