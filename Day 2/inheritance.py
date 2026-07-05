# Single level inheritance
# By default all the data member and member functions are public 

# class Collage:
#     def collage_name(self):
#         print("Collage Name = PCCOE");

# class Student(Collage):
#     def student_info(self):
#         print("Student name = Suraj Indave");
#         print("Student Dept = IT");


# obj = Student();
# obj.collage_name();
# obj.student_info()


# Multilevel inheritance

    # Collage
    #  |
    #  |
    # Student
    #  |
    #  |
    #  Exam

# class Collage:
#     def collage_name(self):
#         print("Collage name = PCCOE ");

# class Student(Collage):
#     def stud_info(self):
#         print("Student Name = Suraj Indave ");
#         print("Student Dept: IT")

# class Exam(Student):
#     def subjects(self):
#         print("--------------  Subjects -------------- ")
#         print("Subject 1 : C")
#         print("Subject 2 : C++")
#         print("Subject 3 : Python")


# obj = Exam();

# obj.collage_name();
# obj.stud_info();
# obj.subjects();


# Multiple inheritance


class SubMarks:
        c = int(input("Enter c lang marks:  "))
        cpp = int(input("Enter cpp lang marks:  "))
        java = int(input("Enter java lang marks:  "))
        python = int(input("Enter python lang marks:  "))

        total = c+cpp+java+python;
        per = ((total*100)/400);

        

class PracMarks:
    prMarks = int(input("Enter c programming practical marks: "));

class Result(SubMarks, PracMarks):
    def Calcresult(self):
        if(self.per>=40 and self.prMarks>=20):
            
            print("Result =Pass");
        else:
            print("Result =Fail");



res = Result();

print("Total Makrks obtained: ", res.total);
print("Percentage : ", res.per);
res.Calcresult();



# class A:
#     def show(self):
#         print("Hello A")

# class B:
#     def show(self):
#         print("Hello B")

# class C(A, B):
#     pass

# obj = C();

# obj.show()