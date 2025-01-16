import csv


data = [
    {"Name": "Bibek", "Age": 25, "City": "New York"},
    {"Name": "Diwash", "Age": 30, "City": "Los Angeles"},
    {"Name": "No-Name", "Age": 22, "City": "Chicago"},
]


file_path = "/home/bibek/Desktop/python1/csvHandnling/output.csv"
headers = ["Name", "Age", "City"]

with open(file_path, mode="w", newline="") as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)
        
   
# delimiters