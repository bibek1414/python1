import csv
file_path="/home/bibek/Desktop/python1/csvHandnling/scvfiles.csv"



with open(file_path,mode="w",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(['Name','Age','Math','Science','Total'])

while True:
    operation=input('''
1.Enter Data
2.Search Data
3.Display Data
4.Exit Data 
Choice: ''')
    if operation=="1":


            while True:
                name=input("Enter the name: ")
                age=int(input("Enter the age: "))
                math=int(input("Enter the marks in math: "))
                science=int(input("Enter the marks in science: "))
                total=math+science
                data=[name,age,math,science,total]


                with open(file_path,mode="a",newline="") as f:
                    csv_writer=csv.writer(f)
                    csv_writer.writerow(data)

                cont = input("Do you want to add more data (yes/no):").strip().lower()
                if cont != "yes":
                    break

    elif operation=="2":
        search= input("Enter the data you want to search record: ")
        found=False

        with open (file_path,mode="r",newline="") as f:
            csv_reader=csv.reader(f)
            header=next(csv_reader)
            for row in csv_reader:
                if search in row:
                        print(row)
                        found=True
        
        if not found:
         print("No mathcing record founds")

    elif operation=="3":
        with open(file_path,mode="r",newline="") as f:
            csv_reader=csv.reader(f)
            for row in csv_reader:
                print(row)

    elif operation=="4":
        print("Exiting the program")
        break