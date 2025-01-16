# print("Dictionaries")


# empty_dict={}


# print(my_dict)


# mixed_dict={
#     1:"one",
#     "2":"two",
#     (1,2,3,4):"set"
# }

# print(mixed_dict)

# print(my_dict["age"])
# print(my_dict("hello"))
# print(my_dict.get("age"))
# print(my_dict.get("hello"),"not found")
# print(f'The sum of  {age} and {age2} is {total_age}')

# x=my_dict.keys()

# y= my_dict.values()

# z= my_dict.items()
# print(z)
# print(y)
# print(x)

# if "age" in my_dict:
#     print("Yes  ")
# age2=20
# age=my_dict.get("age")
# total_age =age+age2
# my_dict["age"]=total_age
# my_dict["address"]=input("Enter the address ")

# my_dict.pop("age")

# print(my_dict)

# for key in my_dict:
#     if key=="age":
#         print(my_dict[key])

# for x in my_dict.values():
#     print(x)

# for x,y in my_dict.items():
#     print(x,y)


# dict2 = {}

# dict2["name"] = input("Enter the name ")

# while True:
#     phone = input("Enter the phone ")
#     if len(phone) == 10 and phone.isdigit():
#         dict2["phone"] = phone
#         break
#     else:
#         print("Phone number must be exactly 10 digits. Please try again.")

# dict2["age"] = int(input("Enter the age "))
# dict2["address"] = input("Enter the address ")
# print(dict2)

# add_five = 5
# for x in dict2:
#     if x == "age":
#         if dict2[x] > 20:
#             add_five = dict2[x] + add_five
#             print(add_five)

# my_dict={
#     "name":"bibek",
#     "age":21,
#     "city":"hetauda"
# }
# dict= my_dict.copy()

# print(dict)

student={
    'name':"Alice",
    'age':20,
    'grades':{
        'math':20,
        'history':20,
        'sciemce':20
    },
    'contacts':{
        'email':"@gamil.com",
        'phone':'5964646646464'
    }
}
print(student['name'])
x=student['grades']
sum=0
for y in x.values():
    sum=sum+y
    
print(f"The total sum is {sum}")
# x=student['grades']
# print(x['math'])

# x=student['grades']['math']
# print(x[0])

squares={x: x**2 for x in range(1,6)}
print(squares)

odd_number={x: x for x in range(1,6) if x%2==0}
print(odd_number)