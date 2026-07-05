
# WAP to accept three paper marks like phy, chem, math and calc total, per and display total marks and percentage

# condition 
# 1) if user is pass in all subject then file.write pass else file.write fail and passing marks is 40
# 2) if per is greater then equal to 65 and gender is male then file.write you ate eligible for placement else not eligible for placement

file = open("Marksheet.txt", "w");

name = input("Enter your name: ")
gen = input("Enter your gender: ")
phy = int(input("Enter phy marks: "))
chem = int(input("Enter chem marks: "));
math = int(input("Enter math marks: "));

total_marks = phy+chem+math;
per = (total_marks * 100 )/ 400

file.write("------------------------INFORMATION--------------------------------\n")
file.write(f"Your name is | {name} \n")
file.write(f"Your gender is | {gen}\n"  )
file.write(f"Total Marks | {total_marks}\n" );
file.write(f"Percentage | {per}\n" )

file.write("---------------------- Subjects ----------------------\n")
file.write(f"Chem = {chem} " )
file.write(f"phy = {phy} " )
file.write(f"math = {math} \n" )

file.write("------------------ RESULT -------------------------\n")
if(phy>40 and chem>40 and math>40):
    file.write("pASS!!")
    if(per>65 and gen=='male'):
        print("Marksheet Display..")
        file.write("Your eligible for placement\n")
    else:
        file.write("Your not eligible for placement\n")
else:
    file.write("Fail..")

