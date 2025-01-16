
# tup=()
# print(type(tup))

# tup=(1,)

# tup=(1,2,3,4,5,62,2,2,2,2,2,2,3,3,3,3,7,8,9,0)

# print(tup[:])

# print(tup.count(2))
# print(tup.index(2))

# print(tup[::2])
# print(tup[::-1])

# # converting list to tuple

# my_list=[1,2,3,4,5]

# my_tuple=tuple(my_list)
# my_list=list(my_tuple)
# print(my_tuple)

# tuple_e=()
# even_numbers=[i for i in range(11) if i%2==0 ]
# tuple_e=tuple(even_numbers)
# print(tuple_e)

# # tuple unpacking
# t=(1,2,3,"red")
# (a,b,c,d)=t
# print(a)
# print(b)
# print(c)

# fruits=("aaple","bananana","grapes","mango")
fruits=("aaple","bananana","grapes","mango")


(green,yellow,*red)=fruits


# print(green)
# print(yellow)
# print(red)

mytuple=fruits*2
# print(mytuple)

numbers=[(2,3),(4,5),(7,8),(0,0),(6,6)]
sum_n=0
max_sum=0
tuple_max=()

for num in numbers:
    sum_n=sum(num)
    print(f"{num} the sum is {sum_n}")
    if sum_n>max_sum:
        max_sum=sum_n
        tuple_max=num
print(f'{tuple_max} : the maximum sum is {max_sum}')


num=[1,2,3,4,6,7,8,9,10]
max_num=max(num)
print(f'THe maximim numner in the {num}  is {max_num}')

max_n=num[0]
for x in num:
    if(x>max_n):
        max_n=x
print(f'THe maximim numner in the {num}  is {max_n}')



