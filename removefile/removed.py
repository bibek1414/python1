import os
# os.remove("/home/bibek/Desktop/python1/removefile/hello.txt")

# if os.path.exists("/home/bibek/Desktop/python1/removefile/hello.txt"):
#     os.remove("/home/bibek/Desktop/python1/removefile/hello.txt")
#     print("Removed Sucessfully")

# else:
#     print("File doesnot exits")
# os.remove("/home/bibek/Desktop/python1/removefile/hellofolder/remove.py")
# os.rmdir("/home/bibek/Desktop/python1/removefile/hellofolder")

# files=os.listdir()
# print(files)

# current_dir=os.getcwd()
# print(current_dir)


# new_dir="new_directory"
# os.mkdir(new_dir)
# print(f"Created Directory",{new_dir})

# files=os.listdir()
# for x in files:
#     if os.path.isdir(x):
#         print(f"{x} is a directory")
#     elif os.path.isfile(x):
#         print(f"{x} is a file")
#     else:
#         print(f"{x} is neither dile nor a directory")

# change dir

os.chdir("demo1123")
print("CHange the currern direcotty to :",os.getcwd())