
# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a/b)
# except ZeroDivisionError:
#     print("Can't devied by zero /")

# except ValueError:
#     print("Enter only pure valuee...")

# print("Contine...")


# Perdefine and custom message error
# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a//b)
# except ZeroDivisionError as msg:
#     print("Error is  -> ", msg)

# except ValueError as msg:
#     print("Error is  -> ", msg)

# Handling multiple diff kinds of exception with a single block
# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a//b)
# except (ZeroDivisionError, ValueError) as msg:
#     print("Error is  -> ", msg)

# Default except block

# if we have requarment of multiple except block then in that switiation default exception block should be in last othe wise systex error will encounter
# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a//b)
# except (ZeroDivisionError, ValueError) as msg:
#     print("Error is  -> ", msg)
# except:
#     print("Default exception execute...")


# use else part with exception handling

# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a//b)
# except (ZeroDivisionError, ValueError) as msg:
#     print("Error is  -> ", msg)
# else:
#     print("Else block execting...")

# Finally block
# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a//b)
# except (ZeroDivisionError, ValueError) as msg:
#     print("Error is  -> ", msg)
# finally:
#     print("ALways excute...")


# nested try except block

# try:
#     n1 = int(input("Enter n1 value: " ));
#     n2 = int(input("Enter n2 value: "));

#     try:
#         print("Result is -> " , n1/n2); 
#     except (ArithmeticError) as msg:
#         print("Error - ", msg)
# except (ValueError) as msg:
#     print("Error - " , msg);

# try:
#     a = int(input("Enter value of a "))
#     b = int(input("Enter value of b "))
#     print("Result is = ", a//b)
# except (ZeroDivisionError, ValueError) as msg:
#     print("Error is  -> ", msg)
# else:
#     print("Else block execting...")
# finally:
#     print("Always execute..")

# user define exception

bank_bal = int(input("Enter a bank bal: "));

if(bank_bal<2000):
    raise Exception("Your account balance is below the access limit")
else:
    print("Your amount has withdrawl")