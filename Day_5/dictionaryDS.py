# myDict= {
#     101: "Suraj",
#     102: "Darshan",
#     "103" : "Shantanu",
#     "104" : "Vinay",
#     102 : "Ashish"
# };

# agar key duplicate hogi toh uski value change krega 
# example 102 : "Darshan" -> 102 : "Ashish" toh usne Ashish value update kia

# print(myDict);
# print(type(myDict))

# Value extract by using a key
# print(myDict[102])

# We will replace old value by new value
# myDict[101] = "Maya";
# print(myDict)

# only print key x = 0, 1

# by default looping statement access the key 
# print("---------- Keys ---------------")
# for x in myDict:
#     print(x);
#     # print(x , " -> " , myDict[x]);

# print("------------- Both ---------------");
# # if we want to display both key and value pair
# for x in myDict:
#     print(x , " -> " , myDict[x]);


# access only values in dict by using a .values()

# print("---------- Values ---------------")
# for x in myDict.values():
#     print(x)


# display both key and values using method

# print("KEYS  |  VALUES")
# print("-----------------")
# for key, value in myDict.items():
#     print(key, " -> ", value)

# if i have to add new key and vvalue pair in my dict

# myDict["Mobile_no"] = 9373308601;
# add new key and value pair using update() function
# myDict.update({"City" : "Pune"})
# print(myDict)

myDict = {
    101:"Suraj Indave",
    "Professional" : "Developer",
    "empId" : 1001 
};

# print(myDict);

# myDict.pop(101);
# print("------------ Remove a hole pair -------------")
# print(myDict)
# pop() -> remove a pair by specific key name

# Copy one dict to another dict

# newDict = myDict.copy();
# newDict.update({"city" : "Pune"})
# print(newDict)

# Task in dict


myDict = {"A" : 50, "B" : 30, "C" : 70};
# Task 1 : Check if dictionary is empty or not 
# if (myDict == {}):
#     print("Dict is empty ");
# else:
#     print("Dict is not a empty")


# Task 2: Check the max value of key
maxKey = myDict["A"]

for i in myDict: 
    if(myDict[i]>maxKey):
        maxKey = i;


print("Max Key -> ", maxKey)

print("Old Dict -> " , myDict)


# Task 3:  Write a function to reverse the key-Value pair of a dict

newMyDict = {};

for i in myDict:
    newMyDict.update({myDict[i] : i});
print("New Dict -> ", newMyDict)