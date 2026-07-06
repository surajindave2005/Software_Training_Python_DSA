def binarySearch(array, target):
    low = 0;
    high = len(array)-1;

    while low<=high:
        mid = (low+high) // 2;

        if(array[mid]==target):
            return mid;
        elif(array[mid] < target):
            low = mid+1;
        else:
            high = mid-1;

    return -1;




array = [1,2,3,4,5,6,7,8,9,10,11];
print("Data -> ", array);
target = int(input("Enter a element which you want to search : "));

# print(binarySearch(array, target))

res = binarySearch(array, target)

print(res)
if(res!=-1):
    print("ELement found at index number = ", binarySearch(array, target));
else:
    print("ELement not found ");


