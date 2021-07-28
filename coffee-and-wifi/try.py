import csv

with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    for row in csv_data:
        print(row)