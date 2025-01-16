squares=[i**2 for i in range(6)]

# print(squares)


numbers=[1,2,3,4,5,6,7,8,9]
even_number=[i for i in numbers if i%2==0 ]
total_sum=sum([i for i in numbers if i%2==0 ])
# print(total_sum)
# print(even_number)

odd_number=[i for i in numbers if i%2!=0]
# print(odd_number)

odd_even_check=[f"{i} is even number"  if i%2==0 else f"{i} is odd numbers" for i in numbers]
 
for x in odd_even_check:
    print(x)


#     more = input("Add another student? (yes/no): ")
#     if more.lower() != 'yes':
#         break