# file = open("Data.txt", "w");
# print(type(file))

# print("File Name : ", file.name);
# print("File Mode : ", file.mode);

# print("File Readable " , file.readable())
# print("File Writable " , file.writable())
# print("File closed : ", file.closed)

# file.close();

# print("File closed : ", file.closed)


# 'w' mode file open
# file = open("Data.txt", "w");

# file.write("This is my line 1\n");
# file.write("This is my line 2\n");
# file.write("This is my line 3\n");
# file.write("This is my line 4\n");
# file.write("This is my line 5\n");

# file.write("Suraj");

# # 'a' mode file open
# file = open("Data.txt", "a");

# file.write("This is my line 1\n");
# file.write("This is my line 2\n");
# file.write("This is my line 3\n");
# file.write("This is my line 4\n");
# file.write("This is my line 5\n");

# file.write("Suraj");

# file.close()

# print("File operation done!")

# file = open("listData.txt", "w");
# citys = ["Pune", "Nashik", "Mumbai"];

# file.writelines(f"{citys}");

# file.close();

# Read File
# readFile = open("Data.txt", "r");
# print(readFile.read())
# readFile.close();

# with statement 

with open("test.txt", "w") as file:
    file.write("Hello world");
    print("File Closed: " , file.closed);

print("File Closed: " , file.closed);
