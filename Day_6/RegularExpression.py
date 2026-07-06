import re;

# print("----------------------------- SEARCH ENGINE ---------------------------------")
# searchWord = input("Enter a word which you want to search it: ");

# count = 0

# # compile() function is used to find the give word which user is give it.

# pattern = re.compile(searchWord);

# # finditer() iss function meh ham paragraphs put krne wale hai jo compile function meh jo word diya hai as a input voh isme check krega 

# # iss function ko ham pattern variable se access krenge

# matcher = pattern.finditer("""
# Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
# To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
# Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
# Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
# Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.


#                       """)

# # print(matcher);

# for i  in matcher:
#     count+=1;
#     # start() -> this function is used to give a starting index of the matching word 
#     # end() -> this function is used to give a ending index of the matching word
#     # group() -> this functio is used to give a actual word which we find it.

#     print(i.start(), "....", i.end(), ".....", i.group());

# print("The number of occurrence : ", count);

# import re;

# searchWord = input("Enter a word which you want to search it: ");

# count = 0;

# matcher = re.finditer(searchWord, """

#         Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
#         To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
#         Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme. suraj indave
#         Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
#         Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.
#                       """)

# # for i in matcher:
# #     count+=1;
# #     print(i.start(), ".....", i.end(), "....", ", Found Word: ", i.group())


# # print("Word Match : ", count);



import re;

# searchWord = input("Enter a word which you want to search it: ");


# # match() -> yeh function sirf aur sirf starting ka data or word find krta hai agar usko agar voh milta hai toh voh uske respect start(), end(), group() function data provide krta hai
# # agar usko match nahi milta toh voh None return krta hai.

# mtch = re.full(searchWord, "This is my paragraph data")

# print(mtch);

# if mtch!=None:
#     print("Match found at begining..")
#     print(mtch.start(), "....", mtch.end(), ".....", ", Word: ", mtch.group())
# else:
#     print("Match not found at begining part")



# searchWord = input("Enter a word which you want to search it: ");


# fullmatch() -> yeh function pure data ko match krta hai means example is data = hello suraj and user ne agar enter kia sirf suraj toh voh None return kr dega because user ne full string enter nahi kia hai, agar user ne hello suraj enter kia toh uske start() and end() index hame return krega 
# agar usko match nahi milta toh voh None return krta hai.

# mtch = re.fullmatch(searchWord, "Hello Suraj Indave")

# print(mtch);

# if mtch!=None:
#     print("Match found at begining..")
#     print(mtch.start(), "....", mtch.end(), ".....", ", Word: ", mtch.group())
# else:
#     print("Match not found at begining part")


# search() -> Yeh sirf first occurance find krta hai means what agar hello suraj hello suraj agar data hai and hamne suraj ko find kia toh 1st occurance suraj ka data deta hai start() and end()
# searchWord = input("Enter a word which you want to search it: ");

# mtch = re.search(searchWord, "Hello Suraj Indave")

# print(mtch);

# if mtch!=None:
#     print("Match found at begining..")
#     print(mtch.start(), "....", mtch.end(), ".....", ", Word: ", mtch.group())
# else:
#     print("Match not found at begining part")


# findall() -> isko list meh convert krega output ko jo jo match hua hai voh
# we used character classes

# mtch = re.findall('[0-9]', "tsflhdalfhd@$44@@");
# mtch = re.findall('[a-z]', "tsflhdalfhd@$44@@");
# mtch = re.findall('[a-z0-9]', "tsflhdalfhd@$44@@");
# mtch = re.findall('[^a-z0-9]', "tsflhdalfhd@$44@@");
# mtch = re.findall('[^a-z0-9]', "tsflhdalfhd@$44@@ ");
# mtch = re.findall('[^a-z0-9]', "tsflhdalfhd@$44@@ ");
# mtch = re.findall('[a,b,c]', "tsflhdcbalfhd@$44@@ ");

# print(mtch)


# subsitute function -> sub(expression, replacement, data)

# encryptedData = re.sub("[a-zU-Z]", "X", "23456 sdfgASDF sdfsADFE");
# print(encryptedData)


# subsitute N function -> subn(expression, replacement, data)
# return "Data", "Count" in a tuple format 

# encryptedData = re.subn("[a-zA-Z]", "X", "23456 sdfgASDF sdfsADFE");
# print(encryptedData)


import re;

# emailId = input("Enter your Mail Id: ");

# m = re.fullmatch("\w[0-9A-Z-a-z_.]*@gmail[.]com", emailId);

# if m!=None:
#     print("Yess Valid Email Id!! ")
#     print("Your email Id: ", emailId);
# else:
#     print("Invalid emailId!!")
#     print("Your email Id: ", emailId);

# mo = input("ENter mobile number: ")
# obj = re.fullmatch("[0-9]{9}", mo);

# if obj!=None:
#     print("Yess it's valid mobile number: ")
#     print("Your Mobile number: ", mo);
# else:
#     print("Invalid mobile number: ")
#     print("Your Mobile number: ", mo);


# Regular expression with file handling

searchData = input("Enter a word which you want to find it: ")
file = open("Data.txt", "r");

content = file.read()

matchData = re.finditer(searchData, content);

for i in matchData:
    print(i.start(), "......", i.end(), ".....", " Found Word: ", i.group());
    
# if matchData!=None:
#     print("Record is found....");

#     print(matchData.start(), "......", matchData.end(), ".....", " Found Word: ", matchData.group());
# else:
#     print("No Match is found...")

