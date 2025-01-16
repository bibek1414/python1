import csv
with open("/home/bibek/Desktop/python1/csvHandnling/data.csv",mode="r") as f:
    csv_readr= csv.DictReader(f)
    print(csv_readr)
    for row in csv_readr:
        print(row['Name'],row['Age'],row['City'])
        