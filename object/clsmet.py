class College:
    college_name = "JUT"
    total_students = 0

    def __init__(self, name):
        self.name = name
        College.total_students += 1

    @classmethod
    def show_college(cls):
        print("College:", cls.college_name)

    @classmethod
    def show_count(cls):
        print("Total students:", cls.total_students)

s1 = College("Sunny")
s2 = College("Amit")

College.show_college()
College.show_count()
