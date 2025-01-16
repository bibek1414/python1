# my_set={1,2,1,2,2,3,4,5,3,4,5,6}
# my_list=[1,2,1,2,2,3,4,5,3,4,5,6]

# remove_duplicate=list(set(my_list))
# print(remove_duplicate)
# print(my_set)


# a={1,"abc",True,'1212121'}
# print(a)


# for x in thisset:
#     if x=="banana":
#         print({x})

# thisset=set()
# print(type(thisset))

# .add .update anything can me merge

thisset={"apple","banana","cherry"}
mylist=["kiwi","dragon-fruit"]
mytuple=("orange","grapes")
string_n="Fruits","abc","bdh"
thisset.update(mylist)
thisset.update(mytuple)
thisset.update(string_n)

# print(thisset)

# .remove if banana not found then error // key error
# .discard doesnot throw any error

# thisset.remove("bananananananana")
thisset.discard("bananananan")



# pop can be used but remove the last element of lat element
# clear is used to make empty set
# del is used to delete all

# set1={1,2,3,4,5}
# set2={"abc","bcf","der",1,2}
# set3={'234','232',"2123","212121",1,2,3,4}

# set4= set1.union(set2,set3)
# print(set4)

# set5=set4|set1|set2|set3
# print(set5)

# set4= set1.intersection(set2,set3)
# print(set4)

# set5= set4&set1&set2&set3
# print(set5)

# set4= set1.difference(set2,set3)
# print(set4)

# set5= set1-set2-set3
# print(set5)

# set1.intersection_update(set2)
# print(set1)

# set1 = {"apple", 1,  "banana", 0, 0.1 , "cherry"}
# set2 = {False, "google", 1, "apple", 2,0.1, True}

# set3 = set1.intersection(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3={'234','232',"2123","212121",1,2,3,4,"banana","aaple"}

# set4 = set1.difference(set2,set3)

# print(set4)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)


