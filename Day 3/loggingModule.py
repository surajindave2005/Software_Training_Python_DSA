import logging as log

# log.basicConfig(filename="log.txt", level=log.DEBUG);

# log.debug("This indicates the debugging information")
# log.info("This indicates the important information ")
# log.error("This indicate the error information ")
# log.warning("This indicate the warning information ")
# log.critical("This indicates the critical information ")


# print("File created!!")


try:
    log.basicConfig(filename="log2.txt", level=log.DEBUG);

    a = int(input("Enter a value "))
    b = int(input("Enter b value "));

    print("Result is -> ", a/b);
except (ArithmeticError, ValueError) as msg:
    print("Error -> ", msg);
    log.exception(msg);
    log.exception("----------------------------------------");


# WAP to accept three paper marks like phy, chem, math and calc total, per and display total marks and percentage

# condition 
# 1) if user is pass in all subject then print pass else print fail and passing marks is 40
# 2) if per is greater then equal to 65 and gender is male then print you ate eligible for placement else not eligible for placement
