numbers=[1,2,3,4,5]
# squared=list(map(lambda x:x**2,numbers))
# print(squared)

# def square(x):
#     return x**2   

# print(list(map(square,numbers)))

numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2==0, numbers))
print(even_numbers)

def even_numbers(x):
    if x %2==0:
        return x
print(list(filter(even_numbers,numbers)))
