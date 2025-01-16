# string_line_string="Bjsdhsakdjhsadkjsa dkjasd sajdh kasjdsa \n ladkjsadkajs kdaslkdja \t " 

# print(string_line_string)




# print(string[4])
# print(string[11])

# print(string[-1])
# print(string[-2])

# """ slicing start:end """

# print(string[7:12])
# print(string[-1:-7])

# print(string[:6])
# string="Hello, world!"
# for x in range(len(string)):
#     print (string[x])
#     if(string[x]=="w"):
#         print (string[x])
#         continue

# name=input("ENter the sting ").lower()
# count=1
# if "a" in name:
#     count+=1
# if "e" in name:
#         count+=1
# if "i" in name:
#             count+=1
# if "o" in name:
#                 count+=1
# if "u" in name:
#                     count+=1
                   
# print(count)
# count=0
# for x in range(len(name)):
    
#     if name[x]=="a" or name[x]=="e" or name[x]=="i" or name[x]=="o" or name[x]=="u" :
#         count+=1
# print(count)
# st = "worldddddddaaaabbbccceee"
# name="aeiou"
# counts={'a':0,'e':0,'i':0,'o':0,'u':0}
# for x in st:
#     if x in name:
#        counts[x] = counts[x] + 1
# print("count a",counts['a'])
# print("count a",counts['e'])
# print("count a",counts['i'])
# print("count a",counts['o'])
# print("count a",counts['u'])

# string="Hello, World!".lower()
# result=""

# for x in string:
#     if x=="w":
#         continue
#     result+=x
# print(result)


# s ="Hello"

# s[0]='v'

# print(s) //type error

s="Hello world!"

# print(s.replace("Hello","Bye Bye"))

# print(s.lower())

# print(s.upper())

# print(s.title())
""" Striping methods to remove white space """

# white_space="                        Hello World!                  "

# print(white_space.lstrip())
# print(white_space.rstrip())
# print(white_space.strip())


s =" I am pythoon developer"

# name=s.split()

# join_list=['I', 'am', 'pythoon', 'developer']

# strings=" ".join(join_list)
# print(strings)
# print(name)


# s= " "

# words=["hello","wordld!"]

# print(s.join(words))


""" F-string """

a=10
b=20

# print(f"the sum of {a} and {b}  is {a+b}")


input="####################################HEllo####World########################"

# s=(name.replace("####"," "))

# for x in name:
#     if x=="#":
#         pass
#     f"""{x}+hello+####+world+{x}"""

# r=(s.strip().lower())

name_sting="hello world"

# r=name_sting.split()

# print(r)

title_output=name_sting.title().replace(" ","###")
# print(title_output)

left= input.lstrip("#")
lenght_left=len(left)

length_input= len(input)

lef=length_input-lenght_left

right= input.rstrip("#")
lenght_right=len(right)
rig=length_input-lenght_right

final_result="#"*lef+title_output+"#"*rig
# print(final_result)



input2="#################Hello########World################"

string="hello world"

string_hash=string.replace(" ","########")

input_length=len(input2)

left_stripe= input2.lstrip("#")

# print(left_stripe)

length_of_input_left=len(left_stripe)

left=input_length-length_of_input_left

# print(left*"#")

right_stripe= input2.rstrip("#")

# print(right_stripe)

length_of_input_right=len(right_stripe)

right=input_length-length_of_input_right

# print(right*"#")

total_word= left*"#"+string_hash+right*"#"

# print(total_word)








    
     
    
