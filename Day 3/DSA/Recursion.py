
# Factorial number 

# def fact(n):
#     if(n<2):
#         return 1;
#     else:
#         return n*fact(n-1);

# result = fact(5);

# print(f"Number = {5} and Factorial number is {fact(5)}");


# Palindrom string 

# def isPalindrom(stringData):
#     if len(stringData) == 0:
#         return True;
#     if stringData[0] != stringData[len(stringData)-1]:
#         return False;
    
#     return isPalindrom(stringData[1:-1]);

# print(isPalindrom("MAM"))
# print(isPalindrom("SURAJ"))
# print(isPalindrom("DADA"))
# print(isPalindrom("DAD"))



# Power calculation 

# def power(base, exponent):
#     if exponent == 0:
#         return 1;
    
#     return base * power(base, exponent-1)

# print("Result - ", power(2, 0))
# print("Result - ", power(2, 2))
# print("Result - ", power(2, 5))

# 2 * power(2, 1)
# 2 * power(2, 0) -> return 1 

# 2 * 2 * 1

# 2 * power(2, 4)
# 2 * power(2, 3)
# 2 * power(2, 2)
# 2 * power(2, 1)
# 2 * power(2, 0) return 1 

# Product of array

# def productOfArray(arr):
#     if (len(arr) == 0):
#         return 1;

#     return arr[0] * productOfArray(arr[1:]);



# print(productOfArray([1,2,3,4]))



# def recursionRange(num):
#     if num<=0:
#         return 0;

#     return num + recursionRange(num-1);
#             # 6 + recursionRange(5) = 21
#             # 5 + recursionRange(4) = 14
#             # 4 + recursionRange(3) = 9
#             # 3 + recursionRange(2) = 5 
#             # 2 + recursionRange(1) = 2
            
# print(recursionRange(6));

# Fibonacci series

# def fibo(n):
#     if(n<2):
#         return 1;
#     return fibo(n-1) + fibo(n-2);

#     # n = 3

#     # n = 2,  n = 1

#     # fibo(2) + fibo(1)

#     # n = 1,  n = 0 -> return 1 
#     # fibo(1) + fibo(1)
#     # 0 1 1 2 3 5 8 .... n

# print(fibo(3));

