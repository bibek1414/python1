# f= open("/home/bibek/Desktop/hello.txt","r")
# print(type(f.read()))

# print(type(f.read()))

# print(str[:6])

# for s in words:
#     if s=="Hello!" or s=="testing" or s=="Good":
#      print(s)




# str=f.read()
# words = str.split()
# print(words)


# for word in words:
#     if word in ["Hello!", "testing", "Good"]:
#         print(word)
# f.close()

# f= open("text.txt","r")
# value=f.readlines()

# clean_lines = [line.strip() for line in value] 

# print(clean_lines)

# for line in value:
#     print(line.strip())
# f.close()

with open("text.txt",'r')as f:
    content=f.read()
    print(content)

