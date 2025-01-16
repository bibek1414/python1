import csv
with open("/home/bibek/Desktop/python1/csvHandnling/data.csv",mode="r") as f:
    csv_readr= csv.reader(f)
    print(csv_readr)
    header=next(csv_readr)
    for row in csv_readr:
        print(row)
        print(row[1])