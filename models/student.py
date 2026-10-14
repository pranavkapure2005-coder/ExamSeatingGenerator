
class Student:
    def __init__(self, roll_no, name, branch):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch

    def display_details(self):
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Branch:", self.branch)

    def to_dict(self):
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "branch": self.branch
        }


if __name__ == "__main__":
    student1 = Student("101", "Amit", "AIDS")
    student2 = Student("102", "Priya", "COMP")

    student1.display_details()
    print("-" * 25)
    student2.display_details()
