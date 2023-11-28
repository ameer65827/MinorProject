import csv

file = open('books.csv', 'r')
csvReader = csv.DictReader(file)

for a in csvReader:
    print(a['BOOKS'])
    # break