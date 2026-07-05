class Student:
    # Data Member
    rollno = 101;
    
    # Member function
    def msg(self):
        print("Student Rollno : ", self.rollno);
    
# object creation 
s1 = Student();
s1.msg();
print("Address of memory: ", s1)
