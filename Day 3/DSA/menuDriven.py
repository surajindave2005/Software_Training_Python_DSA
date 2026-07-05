
import sys

while True:
    n1 = int(input("Enter n1 value : "))
    n2 = int(input("Enter n2 value "))
    print("1. Add");
    print("2. Subtaction")
    print("3. Multiplication")
    print("4. Division ")
    print("5. Exit ")

    n = int(input("Enter your choice: "))

    match n:
        case 1:
            print("--------------------------------------------")
            print("Your selected Arithmatic operation ")
            print("Result = ", n1+n2);
            print("--------------------------------------------")
            print()


        case 2:
            print("--------------------------------------------")

            print("You selected Subtraction operation: ")
            print("Result = ", n1-n2);
            print("--------------------------------------------")
            print()


        case 3:
            print("--------------------------------------------")

            print("You selected Multiplication operation: ")
            print("Result = ", n1*n2);
            print("--------------------------------------------")
            print()

        case 4:
            print("--------------------------------------------")

            print("You selected Division operation: ")
            print("Result = ", n1/n2);
            print("--------------------------------------------")
            print()
        
        case 5:
            print("----------------------------- Thank you for visiting ----------------------------- ")
            sys.exit();
        
        case _:
            print("Enter valid operation!")
        
