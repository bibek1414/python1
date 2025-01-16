# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3= list1+list2
# print(list3)


# list4=[2,3,4,5,6,7,8,5,4,3,2,1,0]

# sort_list= sorted(list4)
# print(sort_list)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for x in matrix:
#     for y in x:
#         if y==1 or y==5 or y==9:
#             print(y,end=" ")
#             sum=sum+y
#         else:
#             print(" ",end=" ")
#     print()
# print(sum)

# print(matrix[0][0])
# print(matrix[1][2])
# print(matrix[2][2])

# result=0
# for x in matrix:
#     result  =   result+sum(x)

# print(result)

# print(sum(matrix[0])+sum(matrix[1])+sum(matrix[2]))

lst=[1,2,3,4,5,3,2,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,5,5,5,5,5,5,6,7,5,5,5,5,5,8]
output=[]
# for x in lst[:]:
#     if lst.count(x)>1:
#         lst.remove(x)
# print(lst)

for x in lst:
    if  lst.count(x)<=2 and x not in output:
        output.append(x)
print(output)
# print(lst.count(1))
            
# 2 choti vanda badi vako lai hataune


        