
n = int(input("Enter a number of student : "))

d = {}

for i in range(n):
    name = input("Enter student name : ")
    marks = int(input("Enter student marks : "))
    d.update({name:marks});

while True:
        name = input("Enter student Name to get Marks : ")
        marks = d.get(name, -1);

        if(marks == -1):
            print("Student is not found ")
        else:
            print(f"The marks of {name} are {marks}");
        
        op = input("Do you want to find anothwer student mark [YES|NO]")

        if op=='NO':
            break;

print("Thanks for using our Application ")