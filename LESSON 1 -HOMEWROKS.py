class student:
    def __init__(self,name,age,grade,marks):
        self.name= name
        self.age = age
        self.grade = grade
        self.marks = marks

    def display_details(self):
        print("name",self.name)
        print("age",self.age)

    def check_result(self):
        if self.marks>= 40:
            print(self.name,"has passed")
        else:
            print(self.name,"hasnt passed")

student1=student("rohan",13,5,98)
student1.display_details()