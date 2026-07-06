# import re;

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


# search()
searchWord = input("Enter a word which you want to search it: ");

mtch = re.search(searchWord, "Hello Suraj Indave")

print(mtch);

if mtch!=None:
    print("Match found at begining..")
    print(mtch.start(), "....", mtch.end(), ".....", ", Word: ", mtch.group())
else:
    print("Match not found at begining part")

