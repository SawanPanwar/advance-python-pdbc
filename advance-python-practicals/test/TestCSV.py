import csv

csvfile = open('C:/Users/Lenovo/Desktop/Status/data.csv')
reader = csv.reader(csvfile)
for row in reader:
    total = int(row[2]) + int(row[3]) + int(row[4])
    if (total >= 120):
        print(row)
