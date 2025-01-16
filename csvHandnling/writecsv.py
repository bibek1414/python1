import csv
data=[
    ['alice',32,'Kathmandu'],
    ['ram',32,'Pokhara'],
    ['Bibek',21,'H etauda']
]


with open("/home/bibek/Desktop/python1/csvHandnling/output.csv",mode='w' ,newline="") as f:
    csv_writer= csv.writer(f)
    csv_writer.writerow(['Name','Age','city'])
    # for row in csv_writer:
    csv_writer.writerow(data)