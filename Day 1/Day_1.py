# Q1
# a = [1,2,3,4,5,6,7,8,9]
# print(a[::2]); # [1, 3, 5, 7, 9]

# Q2
# a = [1,2,3,4,5,6,7,8,9]
# a[::2] = 10, 20,30, 40, 50, 60
# print(a);

# Q3
# 1   2   3   4   5
# 0   1   2   3   4 

# 5   4   3   2   1
# 4   3   2   1   0

# l = [1,2,3,4,5]
# print(l[3:0:-1]) # 4 3 2 

# Q4)

# types of args
# postional args
# default args
# keyword args
# variable_length / variable_number_of args
# Unknown args

    # value = 3. values = [1,2,3]
# def func(value, values):
#     var = 1;
#     values[0] = 44 # [44, 2, 3]

# t = 3
# v = [1,2,3]
# func(t, v);
# print(t, v[0]) # 3, 44

# Q5)

# arr = [
#     [1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12, 13,14, 15]
# ];

# print("Data Elements are..")
# for i in range(0, 4):
        # arr[i] => rows target and last element remove each row
#     print(arr[i].pop(), end="  ")

# Q6

# def f(i, values=[]):
#     values.append(i)
#     print(values)  
#     # return  values; 

# f(1);
# f(2);
# f(3);

# # [1] [1,2] [1,2,3]


# Q7)

# i = 1
# arr[0] = 2

# i = 2
# arr[1] = 3

# i = 3
# arr[2] = 4

# i = 4
# arr[3] = 5

# i = 5
# arr[4] = 6


# Answer : 2 3 4 5 6 6

# arr = [1,2,3,4,5,6]

# for i in range(1, 6):
#     arr[i-1] = arr[i]

# for i in range(0, 6):   
#     print(arr[i], end=" ")

# Q8)

# fl2 = ["A" "B", "C", "P"]

# fl3 = ["A" "B", "C", "P"]

# fl2[0] = 

# G, K, C, P


# Answer: 22

# fl1 = ["Apple", "Berry", "Cherry", "Papaya"]

# fl2 = fl1; # shalow copy

# fl3 = fl1[:] # deep copy (create a sepreate memory)

# fl2[0] = 'Guava'
# fl3[1] = 'Kiwi'

# sum = 0

# for ls in (fl1, fl2, fl3):
#     if ls[0] == 'Guava':
#         sum+=1;
#     if ls[1] == 'Kiwi':
#         sum+=20
    
# print(sum);


# zip() -> stores the multiple range() function in a single function


# for row, col in zip(range(1, 6), range(5, 0, -1)):
#     if row==3 and col==3:
#         continue;
#     print(row, "  ", col)


# Q pending
# data = [
#     [
#         [1,2], [3,4]
#     ],
#     [
#         [5,6], [7,8]
#     ]
# ];


# inti_tuple = ()
# print(inti_tuple.__len__()) # by default it will give 0 


inti_tuple_a = 'a', 'b'; # by default it will converted into a tuple DS
# print(inti_tuple_a) 
# inti_tuple_b = ('a', 'b');

# print(inti_tuple_a == inti_tuple_b)

# Real life example
#     tuple -> student addmission collages (INTAKE)
#     list -> education classes


# tp1 = '1', '2';
# tp2 = ('3', '4');

# print(tp1 + tp2);

# l = [1,2,3];

# init_tuple = ('Python', )*(l.__len__()-l[::-1][0])
# # print(l.__len__())

# print(init_tuple)

# a = {
#     (1,2) : 1,
#     (2,3) : 2,
#     (4, 5) : 3,
# }

# Dict use key as a string and tuple only

# print(a[4,5]) # Value = 3

# a = {
#     'a' : 1,
#     'b' : 2,
#     'c' : 3
# };

# print(a['a', 'b']) 


# fruit = {}
# def addon(index):
#     if index in fruit:
#         fruit[index] +=1;
#     else:
#         fruit[index] = 1; # {'Apple': 1, 'Banana': 1, 'apple': 1}

# addon("Apple");
# addon("Banana");
# addon("apple");

# print(fruit)
# print("Length of fruit: ", len(fruit))


# arr = {} 
# arr[1] = 1
# arr['1'] = 2
# arr[1] +=1; # {1:2:'1':2}

# print(arr)

# sum = 0;
# for k in arr:
#     sum+=arr[k];

# print(sum)

# {1:1, '1':2, 1.0:4}

# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# # decimal number converted into a int value

# print(my_dict)

# sum = 0
# for k in my_dict:
#     sum+=my_dict[k];

# print("Result = ", sum)
# print(type([(1,2,3)]))


# my_dict = {}
# my_dict[(1,2,3)] =  8
# my_dict[(4,2,1)] =  10
# my_dict[(1,2)] = 12

# # {[1,2,4] : 8, [4,2,1]:10, [1,2]:12}
# print(my_dict)

# sumRes = 0
# for k in my_dict:
#     sumRes+=my_dict[k];

# print("Result = " , sumRes);

# box = {"b":1, "c":3, }

# jar = {"jam":4}

# creates = {"box":{"b":1, "c":3}, "jars" : {"jam":4}}


# print(len(create[box]))

# box = {}
# jars = {}
# creats = {}

# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4

# creats['box'] = box
# creats['jars'] = jars

# # print(creats)


# print(len(creats[box]))

# dict = {'c':97, 'a':96, 'b':98}

# for _ in sorted(dict):
#     print(dict[_])


# math = 50
# phy = 50

# print(id(math))
# print(id(phy))
# rec = {"Name" : "Python", "Age" : "20"}
# r = rec.copy();

# print(id(rec))
# print(id(r))

# print(id(rec) == id(r))



# rec = {"Name" : "Python", "Age" : "20"}
# id1 = id(rec);

# print("Address of rec :", id(rec))

# del rec

# rec = {"Name" : "Python", "Age" : "20"}
# id2 = id(rec);


# print(id1);
# print(id2);
# print(id1==id2);

# print("Address of id1 : ", id(id1));
# print("Address of id 2: ", id(id2))
# print("Address of rec :", id(rec))

# n1 = int(input("Enter n1 value "))
# n2 = int(input("Enter n2 value"))

# print(n1+n2)


# Typecasting

# print(int(4.21))
# print(int(True))
# print(int(False))

# print(int("9.22"))

# We can not converted complex value to int 
# we can not converted floating point value string to value


# Floating to other datatype
# print(float(1))
# print(float(True))
# print(float(False))
# print(float("2.32"))

# print(type(float(1)))
# print(type(float(True)))
# print(type(float(False)))
# print(type(float("2.21")))

# We can not convert complex value to complex 
# Can't convert string name into a float example (suraj -> can't converted)

# allways 0 or 0.0 value is converted into a False 
# Any int or float value except 0 or 0.0 is True
# by default empty () is False

# print(bool())


# l = [0, 1, 0, 3, 12]


# print(l)

# for data in l:
#         if data ==0:
#             l.remove(data);
#             l.append(data);

# print(l)


# l1 = [1,2,3]
# l2 = [2,3,4]
# l3 = [3,4,5]

# number = 0;
# for l1_data in l1:
#     if (l1_data in l2  and  l1_data in l3):
#         print(l1_data)


# data = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1,1,1,1,1,1,0, 1,1];

# countOnces = 0;
# max = 0;

# for i in data:
#     if (i==1):
#         countOnces+=1;
#         if(countOnces>max):
#             max = countOnces;
#     else:
#         countOnces=0;


# print(countOnces)
# print(max)


# data = [1,2,3,2,4];

# reverse = data[::-1]

# if data==reverse:
#     print("Its palindrom")
# else:
#     print("Not palindrom")


# emptylist = []

# for i in range(len(data), 1, -1):
#     emptylist.append(i)

# if(emptylist == data):
#     print("Its Palindrom")
# else:
#     print("Not palindrom")

# print(emptylist)


# strData= "Surajjjj";
# reverse = ""
# print("Original Data: ", strData)

# duplicate = set();

# for i in range(len(strData)-1, -1, -1):
#     reverse += strData[i];
#     duplicate.add(strData[i]);

# print("Reversed Data = " , reverse)
# # duplicate.add(reverse);

# for dp in duplicate:
#     print(dp, end = "  ");


# print(type(duplicate))

# name = "Surajjj";
# duplicate = "";

# for i in name:
#     if i not in duplicate:
#         duplicate +=i;

# print(duplicate)


size = int(input("Enter a size of list: "))

lst = [];

diff = [];

for i in range(0, size):
    n = int(input("Enter a elements: "));
    lst.append(n);
print(lst);

    
