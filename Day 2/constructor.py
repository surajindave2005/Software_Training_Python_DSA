# class Demo:
#     def __init__(self):
#         print("Hello I'm a constructor and I always called first ")
    
#     # Instance / Normal method
#     def show(self):
#         print("Hello I'm normal function ")

# obj = Demo();
# obj2 = Demo();
# obj.show();

# class Hod:
#     def __init__(self):
#         self.name = "Suraj Indave";
#         self.age = 23;
#         self.empId = 1001;
    
#     def info(self):
#         print("Employee Name: ", self.name);
#         print("Employee Age: ", self.age);
#         print("Employee Id: ", self.empId);

# obj = Hod();
# obj.info();


# Parameterized constructor 
 
# class Hod:
#     def __init__(self, name, age, rollno):
#         self.name = name;
#         self.age = age;
#         self.rollno = rollno;
    
#     def show(self):
#         print("Name = ", self.name);
#         print("Age = ", self.age);
#         print("Rollno = ", self.rollno);

# obj = Hod("Suraj", 23, 1001);

# obj.show();

# Instance variable

# class New:
#     def __init__(self):
#         self.a = 10;

# obj1 = New();
# obj2 = New();
# obj3 = New()

# print("Obj 1 -> ", obj1.a)
# print("Obj 2 -> ", obj2.a)
# print("Obj 3 -> ", obj3.a)



# Static variable 
# class New:
#     collage_name = "Sandip";

#     def __init__(self):
#         self.name = "Suraj Indave";
    
#     def show(self):
#         print("---------------------------------------");
#         print("Collage Name : =", self.collage_name);
#         print("Student Name: =", self.name);
#         print()


# obj1 = New();

# New.collage_name = "PCCOE" # Static variable

# obj2 = New();
# obj2.name = "Darshan";
# obj3 = New();
# obj3.name = "Shantanu";


# obj1.show();


# obj2.show();
# obj3.show();


# Static and Instance variable single program

# class Collage:
#     collage_name = "Sandip";

#     def __init__(self):
#         self.studentName = "Suraj Indave";
    

# princple = Collage(); 
# teacher = Collage(); 
# accountant = Collage(); 

# print("Princple Name = ", princple.studentName , "| Princple collage name = ", princple.collage_name);
# print("teacher Name = ", teacher.studentName , "| teacher collage name = ", teacher.collage_name);
# print("accountant Name = ", accountant.studentName , "| accountant collage name = ", accountant.collage_name);

# print("----------------------------------------------------------------------------------")
# Collage.collage_name = "PCCOE";
# princple.studentName = "Darshan waykar";

# print("Princple Name = ", princple.studentName , "| Princple collage name = ", princple.collage_name);
# print("teacher Name = ", teacher.studentName , "| teacher collage name = ", teacher.collage_name);
# print("accountant Name = ", accountant.studentName , "| accountant collage name = ", accountant.collage_name);



# class Student:
#     def __init__(self):
#         self.s_name = "Suraj";
#         self.s_rollno = 101;
    
#     def show(self):
#         print("Student name = ", self.s_name);
#         print("Student rollno = ", self.s_rollno);


# obj = Student();

# obj.show();

# obj.s_name = "Darshan"

# # del obj.s_name; # this line show the indicates the internally deleted the s_name variable so it will throw the error in a bellow line 

# print("------------------------------")
# obj.show();

# print(obj.__dict__);

# class Student:
#     @staticmethod
#     def get_personal_detail(fristname, lastname):
#         print("Your name is -> ", fristname , " ", lastname);
    
#     @staticmethod
#     def contact_details(mobile_no, rollno):
#         print("Mobile number: ", mobile_no);
#         print("Rollno number: ", rollno);

# Student.get_personal_detail("Suraj", "Indave");
# Student.contact_details(111111,101);

