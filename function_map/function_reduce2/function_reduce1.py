from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)

max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum number:", max_number)

words = ["Hello", "World", "!"]
sentence = reduce(lambda x, y: x + " " + y, words)
print( sentence)



