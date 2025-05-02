'''import time
from datetime import datetime
class Student:
    def __init__(self , name , reg_no , company):
        self.name = name 
        self. reg_no = reg_no
        self.company = company
    
    def login(self , login_time):
        print(f"{self.name} Reg No: {self.reg_no} of {self.company} Logged in at {login_time.strftime('%H:%M:%S')}")
    
    def logout(self , logout_time):
        print(f"{self.name} Reg No: {self.reg_no} of {self.company} Logged out at {logout_time.strftime('%H:%M:%S')}")

class Mentor:
    def __init__(self , mentor_name, company):
        self.company = company
        self.mentor_name = mentor_name
    
    def guide(self):
        print(f"Mentor {self.name} is guiding students from {self.company}")


class Table:
    def __init__(self , table_no , company):
        self.table_no = table_no
        self.company = company
        self.status = "Available"
        self.student_assigned = None
        self.login_time = None
        self.logout_time = None

    def assign_table(self, student):
        if self.status == "Available" and self.company == student.company:
            self.student_assigned = student
            self.status = "Occupied"
            self.login_time = datetime.now()
            print(f"{self.table_no} ({self.company} assigned to {student.name})")
            student.login(self.login_time)
            return True
        return False
    
    def release_table(self):
        if self.status == "Occupied":
            self.logout_time = datetime.now()
            duration = self.logout_time - self.login_time
            student = self.student_assigned
            student.logout(self.logout_time)
            print(f"{self.table_no} released from {student.name} Duration:{duration}")
            self.status = "Available"
            self.student_assigned = None
            self.login_time = None
            self.logout_time = None 



tables = [
    Table("GE-1", "GE"),
    Table("GE-2", "GE"),
    Table("MS-1", "Microsoft"),
    Table("MS-2", "Microsoft")
]
students = [
    Student("Aisha", "21CS001", "GE"),
    Student("Rahul", "21CS002", "Microsoft"),
    Student("Sneha", "21CS003", "GE"),
    Student("Arjun", "21CS004", "Microsoft"),
    Student("Maya", "21CS005", "GE"),  
]

for student in students:
    assigned = False
    for table in tables:
        if table.assign_table(student):
            assigned = True
            break
    if not assigned:
        print(f"No space for {student.name} - {student.company}")

time.sleep(5)
for table in tables:
    table.release_table()'''

