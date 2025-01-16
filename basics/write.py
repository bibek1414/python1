
with open("write.txt",'a') as f:
    user_input=input("Enter the words you want to enter to the files: ")
    f.write(user_input+'\n')
with open("write.txt","r") as f:
    print(f.read())