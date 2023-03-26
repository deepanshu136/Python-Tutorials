# create INstance Variable in Instance Method
class Student:
    def __init__(self,roll_no,name,age):
        self.roll_no=roll_no
        self.name=name

    #instance method to add instance variable
    def add_marks(self,mark):
        self.mark=mark

stud=Student(20,"emma",14)
stud.add_marks(76)

print('Roll Number:',stud.roll_no,stud)