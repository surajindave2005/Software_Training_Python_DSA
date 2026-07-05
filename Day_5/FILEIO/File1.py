# file = open("Data.txt", "w");
# print(type(file))

# print("File Name : ", file.name);
# print("File Mode : ", file.mode);

# print("File Readable " , file.readable())
# print("File Writable " , file.writable())
# print("File closed : ", file.closed)

# file.close();

# print("File closed : ", file.closed)


# 'w' mode file open
# file = open("Data.txt", "w");

# file.write("This is my line 1\n");
# file.write("This is my line 2\n");
# file.write("This is my line 3\n");
# file.write("This is my line 4\n");
# file.write("This is my line 5\n");

# file.write("Suraj");

# # 'a' mode file open
# file = open("Data.txt", "a");

# file.write("This is my line 1\n");
# file.write("This is my line 2\n");
# file.write("This is my line 3\n");
# file.write("This is my line 4\n");
# file.write("This is my line 5\n");

# file.write("Suraj");

# file.close()

# print("File operation done!")

# file = open("listData.txt", "w");
# citys = ["Pune", "Nashik", "Mumbai"];

# file.writelines(f"{citys}");

# file.close();

# Read File
# readFile = open("Data.txt", "r");
# print(readFile.read())
# readFile.close();

# with statement 

# with open("test.txt", "w") as file:
#     file.write("Hello world");
#     print("File Closed: " , file.closed);

# print("File Closed: " , file.closed);

# read file with statement

# with open("test.txt") as readFile:
#     print(readFile.read());


# tell(), seek() method working

# f = open("Data.txt", "r");
# print("Current index pos of file pointet : ", f.tell());

# print(f.read());
# f.seek(5);

# print("Current index pos of file pointet : ", f.tell());

# print(f.read());

# img = open("cat.jpg", "rb");
# copy = open("copyCat.jpg", "wb");

# data = img.read();
# copy.write(data);

# print("Img copied!");
# print(data)

import csv;

# f = open("StudentRecord.csv", "a", newline="");
# a = csv.writer(f);
# # [] list represent the column 
# # a.writerow(["Student_Id", "Name", "Marks", "Dept"]);

# studentId = int(input("Enter student Id: "))
# name = input("Enter student name: ");
# marks = int(input("Enter student marks : "))
# dept = input("Enter student dept: ")

# a.writerow([studentId, name, marks, dept]);

# print("Record Inserted!");

# f.close();


# task

file = open("Marksheet.csv", "a", newline="");
a = csv.writer(file);

# a.writerow(["Rollno", "Name", "Mobileno", "Sub 1", "Sub 2", "Sub 3", "Total", "Pecentage", "Email id", "Result"]);

rollno = int(input("Enter student rollno: "));
name = input("Enter student name: ");
mobileno = int(input("Enter student mobile no "));
emailId = input("Enter email id ")
sub1 = int(input("Enter sub1 marks: "))
sub2 = int(input("Enter sub2 marks: "))
sub3 = int(input("Enter sub3 marks: "))

total = sub1+sub2+sub3;

per = (total*100)/400;

print(total);
print(per);


if(sub1 > 40 and sub2 > 40 and sub3 > 40):
    a.writerow([rollno, name, mobileno, sub1, sub2, sub3, total, per, emailId, "Pass"]);
else:
    a.writerow([rollno, name, mobileno, sub1, sub2, sub3, total, per, emailId, "Fail"]);

print("Record Inserted!");

file.close();


