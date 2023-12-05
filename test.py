import csv

# Open the CSV file
with open('DATA/books.csv', 'r') as file:
    # Create a DictReader object
    csv_reader = csv.DictReader(file)
    
    # Iterate through each row
    for row in csv_reader:
        print(row)
        # Access each column by its header
          # Replace 'column1', 'column2' with your actual column names
