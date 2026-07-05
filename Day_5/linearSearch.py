# def linearSearch(arr, target):
#     for index in range(0, len(arr)):
#         if (arr[index] == target):
#             return index;
    
#     return -1;

# arr = [1,2,3,4,80];
# print("Data -> ", arr);
# target = int(input("Enter a value which you want to search : "));
# print("Index = ", linearSearch(arr, target))

# if linearSearch(arr, target) != -1:
#     print("Element is found -> ", linearSearch(arr, target));
# else:
#     print("Element is not found -> ", linearSearch(arr, target))

# a = [1,2,43,5,4,5,1];
# minValue = a[0];
# maxValue = 0;

# for i in a:
#     if (i>maxValue):
#         maxValue = i;
#     elif(i<minValue):
#         minValue = i;

# print("Min value -> ", minValue);
# print("Max value -> ", maxValue);


a = [3,3,4,4,4,4,2,2]
majorityEle = 0;


for i in range(0, len(a)):
    for j in range(1, i+1):
        if(i!=j):
            majorityEle+=1;

print(majorityEle)