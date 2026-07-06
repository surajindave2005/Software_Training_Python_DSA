
# Pattern 1

# 1 1 1
# 2 2 2
# 3 3 3

# for i in range(1, 4): #outer loop
#     for j in range(1, 4): #Inner loop 
#       print(i, end=" ");

#     print()


# Pattern 2 
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# n = int(input("Enter any number : "))

# for row in range(1, n+1):
#     for col in range(1, n+1):
#         print(row, end=" ")
#     print()



# Pattern 3

# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 1 1 1 1

# n = int(input("Enter any number : "))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(n+1-i, end=" ")
#     print()



# Pattern 4
# *
# * *
# * * *
# * * * *

# n = int(input("Enter a row number: "))
# for i in range(1, n+1):
#     print("*"*i)




# Pattern 5
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F

# n = int(input("Enter the number of rows: "))

# for i in range(1, n+1):
#     for j in range(1, 1+i): #j(1, 2),(1, 3), (1, 4), (1, 5)  
#         print(chr(64 + i), end = " ");
#     print()

    # n = 5

    # j = (1, 6)
    # *****
    # ****
    # ***
    # **
    # *

    # j = (1, 5)
    # j = (1, 4)
    # j = (1, 3)
    # j = (1, 2)

# n = int(input("Enter the number of rows: "))

# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print("*", end=" ");

#     print()


# A B C D
# A B C
# A B
# A

# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(64+j), end=" ");

#     print()

    # n = 5
    # j = (1, 6)
    #     print(chr(64+1)) -> chr(65)
    #     print(chr(64+2)) -> chr(66)

import time;

# n = int(input("Enter the number of rows: "))

# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         time.sleep(0.4);
#         print(n+1-i, end=" ");

#     print()


# C C C
# B B
# A

# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(chr(65+n-i), end=" ");
#     print()


n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    print(" "*(n-i), end=" ");
    for j in range(1, i+1):
        time.sleep(0.5);
        print("*", end=" ");
    print();